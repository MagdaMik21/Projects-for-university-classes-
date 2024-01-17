import tkinter as tk
from tkinter import ttk, messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

class ScheduleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generator Planu Zajęć")

        self.schedule_data = {day: {} for day in ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek"]}
        self.create_widgets()

    def create_widgets(self):
        # Etykieta i pole tekstowe na nazwę pliku
        self.file_label = tk.Label(self.root, text="Nazwa pliku:")
        self.file_label.grid(row=0, column=0, sticky="e")

        self.file_entry = tk.Entry(self.root)
        self.file_entry.grid(row=0, column=1)

        # Przycisk do dodawania zajęć
        self.add_button = tk.Button(self.root, text="Dodaj Zajęcia", command=self.add_schedule)
        self.add_button.grid(row=1, column=0, columnspan=2)

        # Przycisk do generowania planu PDF
        self.generate_button = tk.Button(self.root, text="Generuj PDF", command=self.generate_pdf)
        self.generate_button.grid(row=2, column=0, columnspan=2)

        # Tabela do wybierania dni tygodnia
        self.days_table = ttk.Combobox(self.root, values=["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek"])
        self.days_table.grid(row=3, column=0, columnspan=2)

    def add_schedule(self):
        # Okno do wprowadzania danych o zajęciach
        schedule_window = tk.Toplevel(self.root)
        schedule_window.title("Dodaj Zajęcia")

        day_label = tk.Label(schedule_window, text="Dzień:")
        day_label.grid(row=0, column=0)

        # Ustawienie wartości domyślnej na pierwszy dzień tygodnia
        day_entry = ttk.Combobox(schedule_window, values=["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek"])
        day_entry.grid(row=0, column=1)
        day_entry.set("Poniedziałek")

        time_label = tk.Label(schedule_window, text="Godzina rozpoczęcia:")
        time_label.grid(row=1, column=0)

        time_entry_start = tk.Entry(schedule_window)
        time_entry_start.grid(row=1, column=1)

        time_label_end = tk.Label(schedule_window, text="Godzina zakończenia:")
        time_label_end.grid(row=2, column=0)

        time_entry_end = tk.Entry(schedule_window)
        time_entry_end.grid(row=2, column=1)

        subject_label = tk.Label(schedule_window, text="Przedmiot:")
        subject_label.grid(row=3, column=0)

        subject_entry = tk.Entry(schedule_window)
        subject_entry.grid(row=3, column=1)

        # Przycisk potwierdzający dodanie zajęć
        confirm_button = tk.Button(schedule_window, text="Dodaj", command=lambda: self.confirm_schedule(
            day_entry.get(), time_entry_start.get(), time_entry_end.get(), subject_entry.get()))
        confirm_button.grid(row=4, column=0, columnspan=2)

    def confirm_schedule(self, day, time_start, time_end, subject):
        if day not in self.schedule_data:
            self.schedule_data[day] = {}

        # Sprawdzenie, czy zakres godzinowy został podany poprawnie
        try:
            time_start = float(time_start)
            time_end = float(time_end)
        except ValueError:
            print("Błąd: Godziny muszą być liczbami.")
            return

        if time_start >= time_end:
            print("Błąd: Godzina rozpoczęcia musi być wcześniej niż godzina zakończenia.")
            return

        # Sprawdzenie, czy podany zakres godzinowy nie koliduje z już istniejącymi zajęciami
        for existing_time_start, existing_time_end in self.schedule_data[day].keys():
            if (time_start < existing_time_end and time_end > existing_time_start) or \
               (existing_time_start < time_end and existing_time_end > time_start):
                print("Błąd: Kolidujące zajęcia.")
                return

        self.schedule_data[day][(time_start, time_end)] = subject
        print(f"Dodano zajęcia: {day}, {time_start:.2f}-{time_end:.2f} - {subject}")

    def generate_pdf(self):
        filename = self.file_entry.get() or 'schedule'
        output_filename = f"{filename}.pdf"

        try:
            doc = SimpleDocTemplate(output_filename, pagesize=letter)
            elements = []

            # Nagłówek z dniami tygodnia
            data = [['Dzień'] + [' '.join([str(time_start), '-', str(time_end)]) for (time_start, time_end) in self.schedule_data['Poniedziałek'].keys()]]
            for day in self.schedule_data:
                row = [day]
                for (time_start, time_end), subject in self.schedule_data[day].items():
                    row.append(f'{subject}\n{time_start:.2f}-{time_end:.2f}')
                data.append(row)

            table = Table(data)
            style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), 'grey'),
                                ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
                                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                ('GRID', (0, 0), (-1, -1), 1, 'black')])

            table.setStyle(style)
            elements.append(table)

            doc.build(elements)
            
            # Dodano komunikat po wygenerowaniu pliku PDF
            messagebox.showinfo("Generowanie PDF", f"PDF został wygenerowany do folderu: {output_filename}")

        except Exception as e:
            print(f"Wystąpił błąd podczas generowania pliku PDF: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ScheduleApp(root)
    root.mainloop()
