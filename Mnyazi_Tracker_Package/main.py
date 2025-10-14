
import os, json, threading, datetime
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk

# Try importing firebase libs (if not available, app will run in demo/local mode)
try:
    import pyrebase
    import firebase_admin
    from firebase_admin import credentials, firestore, storage, auth as admin_auth
    FIREBASE_AVAILABLE = True
except Exception as e:
    FIREBASE_AVAILABLE = False

BASE_DIR = os.path.dirname(__file__)
CONFIG_PATH = os.path.join(BASE_DIR, 'config', 'firebase_config.json')
SERVICE_ACCOUNT = os.path.join(BASE_DIR, 'config', 'serviceAccount.json')

def load_logo(path):
    try:
        img = Image.open(path)
        img = img.resize((320,80), Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception:
        return None

class App:
    def __init__(self, root):
        self.root = root
        root.title("Mnyazi Dream Decor Event Tracker")
        root.geometry("1100x700")
        self.logo = load_logo(os.path.join(BASE_DIR, 'assets', 'logo.png'))
        self.create_widgets()
        self.firebase_init()

    def firebase_init(self):
        self.fb = None
        self.db = None
        self.auth = None
        if FIREBASE_AVAILABLE and os.path.exists(CONFIG_PATH):
            try:
                with open(CONFIG_PATH, 'r') as f:
                    cfg = json.load(f)
                self.fb = pyrebase.initialize_app(cfg)
                self.auth = self.fb.auth()
                # init admin sdk if service account provided (for server-like ops)
                if os.path.exists(SERVICE_ACCOUNT):
                    cred = credentials.Certificate(SERVICE_ACCOUNT)
                    firebase_admin.initialize_app(cred, {'storageBucket': cfg.get('storageBucket')})
                    self.db = firestore.client()
                else:
                    # fallback to realtime db for client operations
                    self.db = self.fb.database()
                print("Firebase initialized")
            except Exception as ex:
                print("Firebase init error:", ex)

    def create_widgets(self):
        top = tk.Frame(self.root)
        top.pack(fill='x', pady=10)
        if self.logo:
            lbl = tk.Label(top, image=self.logo)
            lbl.pack(side='left', padx=10)
        title = tk.Label(top, text='Mnyazi Dream Decor Event Tracker', font=('Segoe UI', 18, 'bold'), fg='#C5904E')
        title.pack(side='left', padx=10)
        motto = tk.Label(top, text='Elegance in Every Detail. Stunning Decor for Every Occasion.', font=('Segoe UI', 10), fg='#777')
        motto.pack(side='left', padx=20)

        # Login area
        self.user_frame = tk.Frame(self.root, bd=1, relief='sunken', padx=10, pady=10)
        self.user_frame.pack(fill='x', padx=12, pady=6)
        tk.Label(self.user_frame, text='Email:').grid(row=0, column=0, sticky='e')
        self.email_var = tk.StringVar()
        tk.Entry(self.user_frame, textvariable=self.email_var, width=30).grid(row=0, column=1)
        tk.Label(self.user_frame, text='Password:').grid(row=0, column=2, sticky='e')
        self.pw_var = tk.StringVar()
        tk.Entry(self.user_frame, textvariable=self.pw_var, show='*', width=20).grid(row=0, column=3)
        tk.Button(self.user_frame, text='Login', command=self.login).grid(row=0, column=4, padx=6)
        tk.Button(self.user_frame, text='Demo Mode', command=self.demo_mode).grid(row=0, column=5, padx=6)

        # Main panes
        self.main_pane = tk.PanedWindow(self.root, orient='horizontal')
        self.main_pane.pack(fill='both', expand=True, padx=12, pady=8)

        # Left: booking form
        left = tk.Frame(self.main_pane, width=420)
        self.main_pane.add(left)
        tk.Label(left, text='Create Booking', font=('Segoe UI', 12, 'bold')).pack(anchor='w', pady=6)

        form = tk.Frame(left)
        form.pack(fill='x', padx=6, pady=6)
        self.client_name = tk.Entry(form, width=30); tk.Label(form, text='Client Name').grid(row=0,column=0,sticky='w'); self.client_name.grid(row=0,column=1)
        self.client_phone = tk.Entry(form, width=30); tk.Label(form, text='Phone').grid(row=1,column=0,sticky='w'); self.client_phone.grid(row=1,column=1)
        self.event_type = ttk.Combobox(form, values=['Wedding','Corporate','Birthday','Baby Shower','Other'], width=28); tk.Label(form, text='Event Type').grid(row=2,column=0,sticky='w'); self.event_type.grid(row=2,column=1)
        self.event_date = tk.Entry(form, width=30); tk.Label(form, text='Event Date (YYYY-MM-DD)').grid(row=3,column=0,sticky='w'); self.event_date.grid(row=3,column=1)
        self.venue = tk.Entry(form, width=30); tk.Label(form, text='Venue').grid(row=4,column=0,sticky='w'); self.venue.grid(row=4,column=1)
        self.package = ttk.Combobox(form, values=['Basic Decor','Premium Decor','Full Package','Catering Only'], width=28); tk.Label(form, text='Package').grid(row=5,column=0,sticky='w'); self.package.grid(row=5,column=1)
        self.tents = tk.Spinbox(form, from_=0, to=20, width=5); tk.Label(form, text='Tents').grid(row=6,column=0,sticky='w'); self.tents.grid(row=6,column=1, sticky='w')
        self.chairs = tk.Spinbox(form, from_=0, to=1000, width=8); tk.Label(form, text='Chairs').grid(row=7,column=0,sticky='w'); self.chairs.grid(row=7,column=1, sticky='w')
        self.amount = tk.Entry(form, width=15); tk.Label(form, text='Amount (KSh)').grid(row=8,column=0,sticky='w'); self.amount.grid(row=8,column=1, sticky='w')

        tk.Button(left, text='Save Booking', bg='#C5904E', fg='white', command=self.save_booking).pack(pady=8)

        # Right: listing & reports
        right = tk.Frame(self.main_pane)
        self.main_pane.add(right)
        tk.Label(right, text='Bookings', font=('Segoe UI', 12, 'bold')).pack(anchor='w', pady=6)
        # filters
        flt = tk.Frame(right); flt.pack(fill='x', padx=6)
        tk.Label(flt, text='Filter by Date:').grid(row=0,column=0); self.filter_date = tk.Entry(flt); self.filter_date.grid(row=0,column=1)
        tk.Button(flt, text='Apply', command=self.load_bookings).grid(row=0,column=2, padx=6)
        # treeview
        cols = ('id','client','phone','type','date','venue','package','tents','chairs','amount','status')
        self.tree = ttk.Treeview(right, columns=cols, show='headings', height=20)
        for c in cols:
            self.tree.heading(c, text=c.title())
            self.tree.column(c, width=90, anchor='center')
        self.tree.pack(fill='both', expand=True, padx=6, pady=6)
        # buttons
        btns = tk.Frame(right)
        btns.pack(fill='x', padx=6, pady=6)
        tk.Button(btns, text='Edit', command=self.edit_selected).pack(side='left', padx=4)
        tk.Button(btns, text='Delete', command=self.delete_selected).pack(side='left', padx=4)
        tk.Button(btns, text='Export Excel', command=self.export_excel).pack(side='left', padx=4)
        tk.Button(btns, text='Monthly Report', command=self.monthly_report).pack(side='left', padx=4)

        # local storage fallback
        self.local_data = []
        self.user = None

    def demo_mode(self):
        # Demo login without Firebase - local mode
        self.user = {'email':'demo@local','role':'Admin'}
        messagebox.showinfo('Demo Mode', 'Running in local demo mode. Data is stored locally.')
        self.load_bookings()

    def login(self):
        email = self.email_var.get().strip()
        pw = self.pw_var.get().strip()
        if not email or not pw:
            messagebox.showwarning('Input', 'Please enter email and password')
            return
        if self.auth:
            try:
                user = self.auth.sign_in_with_email_and_password(email, pw)
                self.user = user
                messagebox.showinfo('Logged in', f'Welcome {email}')
                self.load_bookings()
            except Exception as ex:
                messagebox.showerror('Auth error', str(ex))
        else:
            messagebox.showwarning('Auth unavailable', 'Firebase auth not configured. Use Demo Mode.')

    def save_booking(self):
        record = {
            'client': self.client_name.get().strip(),
            'phone': self.client_phone.get().strip(),
            'type': self.event_type.get(),
            'date': self.event_date.get().strip(),
            'venue': self.venue.get().strip(),
            'package': self.package.get(),
            'tents': int(self.tents.get() or 0),
            'chairs': int(self.chairs.get() or 0),
            'amount': float(self.amount.get() or 0.0),
            'status': 'Pending',
            'created_at': datetime.datetime.utcnow().isoformat()
        }
        # basic validation
        if not record['client'] or not record['date']:
            messagebox.showwarning('Validation', 'Client and Date required')
            return
        # push to firebase if available
        if self.db and FIREBASE_AVAILABLE:
            try:
                if isinstance(self.db, type(self.db).client): # firestore client check - naive
                    doc = self.db.collection('bookings').add(record)
                else:
                    self.db.child('bookings').push(record)
                messagebox.showinfo('Saved', 'Booking saved to cloud')
                self.clear_form()
                self.load_bookings()
                return
            except Exception as ex:
                print('Cloud save error', ex)
                messagebox.showwarning('Cloud error', 'Failed to save to cloud; saving locally')
        # fallback: save locally in memory and to a local JSON file
        self.local_data.append(record)
        try:
            path = os.path.join(BASE_DIR, 'local_data.json')
            import json
            with open(path, 'w') as f:
                json.dump(self.local_data, f, indent=2)
        except Exception as e:
            print('Local save error', e)
        messagebox.showinfo('Saved', 'Booking saved locally (offline mode)')
        self.clear_form()
        self.load_bookings()

    def clear_form(self):
        self.client_name.delete(0, 'end'); self.client_phone.delete(0,'end'); self.event_date.delete(0,'end'); self.venue.delete(0,'end'); self.amount.delete(0,'end')

    def load_bookings(self):
        # clear tree
        for r in self.tree.get_children(): self.tree.delete(r)
        # try cloud first
        if self.db and FIREBASE_AVAILABLE:
            try:
                if hasattr(self.db, 'collection'): # firestore
                    docs = self.db.collection('bookings').stream()
                    rows = [doc.to_dict() | {'id': doc.id} for doc in docs]
                else:
                    rows = []
                    data = self.db.child('bookings').get().val() or {}
                    for k,v in data.items():
                        v['id']=k; rows.append(v)
                for r in rows:
                    self.tree.insert('', 'end', values=(r.get('id',''), r.get('client',''), r.get('phone',''), r.get('type',''), r.get('date',''), r.get('venue',''), r.get('package',''), r.get('tents',''), r.get('chairs',''), r.get('amount',''), r.get('status','')))
                return
            except Exception as ex:
                print('Cloud load err', ex)
        # fallback to local_data file
        try:
            path = os.path.join(BASE_DIR, 'local_data.json')
            import json
            if os.path.exists(path):
                with open(path,'r') as f:
                    rows = json.load(f)
            else:
                rows = []
            for idx, r in enumerate(rows, start=1):
                self.tree.insert('', 'end', values=(idx, r.get('client',''), r.get('phone',''), r.get('type',''), r.get('date',''), r.get('venue',''), r.get('package',''), r.get('tents',''), r.get('chairs',''), r.get('amount',''), r.get('status','')))
        except Exception as e:
            print('Local load err', e)

    def edit_selected(self):
        sel = self.tree.focus()
        if not sel:
            messagebox.showwarning('Select', 'Please select a booking')
            return
        vals = self.tree.item(sel,'values')
        # naive edit: prompt to change status
        new = tk.simpledialog.askstring('Edit Status', 'Enter new status', initialvalue=vals[-1])
        if new:
            # For cloud we'd update document; for local, modify JSON
            messagebox.showinfo('Updated', 'Status updated (local demo or cloud update not implemented in this simple demo)')

    def delete_selected(self):
        sel = self.tree.focus()
        if not sel:
            messagebox.showwarning('Select', 'Please select a booking')
            return
        vals = self.tree.item(sel,'values')
        if messagebox.askyesno('Confirm', f'Delete booking for {vals[1]}?'):
            # For cloud, delete; for local, remove from file
            path = os.path.join(BASE_DIR, 'local_data.json')
            try:
                import json
                if os.path.exists(path):
                    with open(path,'r') as f:
                        rows = json.load(f)
                    # remove first matching by client and date - naive
                    rows2 = [r for r in rows if not (r.get('client')==vals[1] and r.get('date')==vals[4])]
                    with open(path,'w') as f:
                        json.dump(rows2, f, indent=2)
                self.load_bookings()
                messagebox.showinfo('Deleted', 'Booking removed')
            except Exception as e:
                print('Delete err', e)

    def export_excel(self):
        try:
            from openpyxl import Workbook
            wb = Workbook()
            ws = wb.active
            ws.append(['Client','Phone','Type','Date','Venue','Package','Tents','Chairs','Amount','Status'])
            for r in self.tree.get_children():
                ws.append(self.tree.item(r,'values')[1:])
            path = filedialog.asksaveasfilename(defaultextension='.xlsx', filetypes=[('Excel','*.xlsx')])
            if path:
                wb.save(path)
                messagebox.showinfo('Export', f'Excel saved to {path}')
        except Exception as e:
            messagebox.showerror('Export error', str(e))

    def monthly_report(self):
        # simple aggregation from current view: totals by type and revenue
        totals = {}
        revenue = 0.0
        for r in self.tree.get_children():
            vals = self.tree.item(r,'values')
            typ = vals[3]; amt = float(vals[9] or 0)
            totals[typ] = totals.get(typ,0) + 1
            revenue += amt
        txt = f'Monthly report (from current view)\\nTotal revenue: KSh {revenue:.2f}\\n'
        for k,v in totals.items():
            txt += f'{k}: {v}\\n'
        messagebox.showinfo('Monthly report', txt)

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
