
import csv
import os
import sys
import webbrowser
from datetime import datetime

from PySide6.QtCore import Qt, QDate, QTimer, QPoint
from PySide6.QtGui import QAction, QDesktopServices, QIcon
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QLineEdit, QComboBox, QTableWidget, QTableWidgetItem,
    QAbstractItemView, QHeaderView, QMessageBox, QDialog, QFormLayout,
    QTextEdit, QDateEdit, QDialogButtonBox, QMenu, QFileDialog
)
from PySide6.QtCore import QUrl

def get_app_dir():
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

APP_DIR = get_app_dir()
CSV_FILE = os.path.join(APP_DIR, "job_applications.csv")
SETTINGS_FILE = os.path.join(APP_DIR, "tracker_settings.txt")
ICON_FILE = os.path.join(APP_DIR, "app_icon.ico")

FIELDS = [
    "Company", "Country", "Date", "Position", "Medium", "Status",
    "Last Update", "Next Follow-up", "Job URL", "Notes"
]

TABLE_FIELDS = [
    "Company", "Country", "Date", "Position",
    "Medium", "Status", "Last Update", "Next Follow-up"
]

MEDIUMS = [
    "LinkedIn", "Company Website", "Email",
    "Recruiter", "Referral", "Other"
]

STATUSES = [
    "Waiting", "Interviewing", "Follow-up",
    "Offer", "Accepted", "Rejected", "Withdrawn"
]

COUNTRIES = [
    "Mexico", "United States", "Canada", "United Kingdom", "Australia",
    "New Zealand", "Ireland", "France", "Germany", "Spain", "Italy",
    "Netherlands", "Sweden", "Denmark", "Norway", "Finland", "Belgium",
    "Switzerland", "Japan", "South Korea", "Singapore", "Other"
]

STATUS_COLORS = {
    "Waiting": "#FFF0A6",
    "Interviewing": "#B8D9FF",
    "Follow-up": "#D8C1FF",
    "Offer": "#FFD08A",
    "Accepted": "#B8E6B8",
    "Rejected": "#FFB8B8",
    "Withdrawn": "#D9D9D9",
}

THEMES = {
    "Windows Light": """
        QWidget {
            background: #F5F5F5;
            color: #202020;
            font-family: "Segoe UI";
            font-size: 10pt;
        }
        QMainWindow { background: #F5F5F5; }
        QLineEdit, QComboBox, QTextEdit, QDateEdit {
            background: #FFFFFF;
            border: 1px solid #C8C8C8;
            border-radius: 6px;
            padding: 6px;
            min-height: 24px;
        }
        QLineEdit:focus, QComboBox:focus, QTextEdit:focus, QDateEdit:focus {
            border: 1px solid #0067C0;
        }
        QPushButton {
            background: #FFFFFF;
            border: 1px solid #C8C8C8;
            border-radius: 6px;
            padding: 7px 14px;
        }
        QPushButton:hover { background: #F0F0F0; }
        QPushButton#primaryButton {
            background: #0067C0;
            color: white;
            border: none;
        }
        QPushButton#primaryButton:hover { background: #005AA8; }
        QTableWidget {
            background: #FFFFFF;
            alternate-background-color: #FAFAFA;
            gridline-color: #E8E8E8;
            border: 1px solid #D6D6D6;
            border-radius: 8px;
            selection-background-color: #CCE8FF;
            selection-color: #202020;
        }
        QHeaderView::section {
            background: #F2F2F2;
            border: none;
            border-bottom: 1px solid #D6D6D6;
            padding: 8px;
            font-weight: 600;
        }
        QTableCornerButton::section { background: #F2F2F2; border: none; }
        QMenu {
            background: #FFFFFF;
            border: 1px solid #D0D0D0;
            padding: 4px;
        }
        QMenu::item { padding: 7px 24px; border-radius: 4px; }
        QMenu::item:selected { background: #E5F1FB; }
    """,
    "Dark": """
        QWidget {
            background: #202020;
            color: #F2F2F2;
            font-family: "Segoe UI";
            font-size: 10pt;
        }
        QMainWindow { background: #202020; }
        QLineEdit, QComboBox, QTextEdit, QDateEdit {
            background: #2B2B2B;
            border: 1px solid #4A4A4A;
            border-radius: 6px;
            padding: 6px;
            min-height: 24px;
            color: #F2F2F2;
        }
        QLineEdit:focus, QComboBox:focus, QTextEdit:focus, QDateEdit:focus {
            border: 1px solid #60CDFF;
        }
        QPushButton {
            background: #2D2D2D;
            border: 1px solid #4A4A4A;
            border-radius: 6px;
            padding: 7px 14px;
            color: #F2F2F2;
        }
        QPushButton:hover { background: #383838; }
        QPushButton#primaryButton {
            background: #0F6CBD;
            color: white;
            border: none;
        }
        QPushButton#primaryButton:hover { background: #115EA3; }
        QTableWidget {
            background: #252526;
            alternate-background-color: #2A2A2A;
            gridline-color: #3A3A3A;
            border: 1px solid #3F3F3F;
            border-radius: 8px;
            selection-background-color: #094771;
            selection-color: #FFFFFF;
        }
        QHeaderView::section {
            background: #2D2D30;
            color: #F2F2F2;
            border: none;
            border-bottom: 1px solid #444444;
            padding: 8px;
            font-weight: 600;
        }
        QTableCornerButton::section { background: #2D2D30; border: none; }
        QMenu {
            background: #2B2B2B;
            color: #F2F2F2;
            border: 1px solid #4A4A4A;
            padding: 4px;
        }
        QMenu::item { padding: 7px 24px; border-radius: 4px; }
        QMenu::item:selected { background: #094771; }
    """,
    "Slate": """
        QWidget {
            background: #E9EEF3;
            color: #1F2937;
            font-family: "Segoe UI";
            font-size: 10pt;
        }
        QMainWindow { background: #E9EEF3; }
        QLineEdit, QComboBox, QTextEdit, QDateEdit {
            background: #F8FAFC;
            border: 1px solid #CBD5E1;
            border-radius: 6px;
            padding: 6px;
            min-height: 24px;
        }
        QLineEdit:focus, QComboBox:focus, QTextEdit:focus, QDateEdit:focus {
            border: 1px solid #475569;
        }
        QPushButton {
            background: #F8FAFC;
            border: 1px solid #CBD5E1;
            border-radius: 6px;
            padding: 7px 14px;
        }
        QPushButton:hover { background: #EEF2F7; }
        QPushButton#primaryButton {
            background: #475569;
            color: white;
            border: none;
        }
        QTableWidget {
            background: #F8FAFC;
            alternate-background-color: #F1F5F9;
            gridline-color: #E2E8F0;
            border: 1px solid #CBD5E1;
            border-radius: 8px;
            selection-background-color: #CBD5E1;
            selection-color: #1F2937;
        }
        QHeaderView::section {
            background: #E2E8F0;
            border: none;
            border-bottom: 1px solid #CBD5E1;
            padding: 8px;
            font-weight: 600;
        }
    """
}


def ensure_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="", encoding="utf-8-sig") as f:
            csv.DictWriter(f, fieldnames=FIELDS).writeheader()


def load_applications():
    ensure_csv()
    with open(CSV_FILE, "r", newline="", encoding="utf-8-sig") as f:
        return [{field: row.get(field, "") for field in FIELDS} for row in csv.DictReader(f)]


def save_applications(rows):
    with open(CSV_FILE, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def load_theme():
    try:
        value = open(SETTINGS_FILE, "r", encoding="utf-8").read().strip()
        return value if value in THEMES else "Windows Light"
    except OSError:
        return "Windows Light"


def save_theme(name):
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        f.write(name)


def qdate_from_string(value, fallback_today=False):
    value = (value or "").strip()
    if value:
        qd = QDate.fromString(value, "yyyy-MM-dd")
        if qd.isValid():
            return qd
    return QDate.currentDate() if fallback_today else QDate()


class ApplicationDialog(QDialog):
    def __init__(self, parent=None, application=None):
        super().__init__(parent)
        self.application = application or {}
        self.setWindowTitle("Edit Application" if application else "Add Application")
        self.resize(520, 520)

        layout = QVBoxLayout(self)
        form = QFormLayout()
        form.setLabelAlignment(Qt.AlignRight)

        self.company = QLineEdit(self.application.get("Company", ""))
        self.country = QComboBox()
        self.country.setEditable(True)
        self.country.addItems(COUNTRIES)
        self.country.setCurrentText(self.application.get("Country", "") or "Mexico")

        self.application_date = QDateEdit()
        self.application_date.setCalendarPopup(True)
        self.application_date.setDisplayFormat("yyyy-MM-dd")
        self.application_date.setDate(qdate_from_string(self.application.get("Date"), True))

        self.position = QLineEdit(self.application.get("Position", ""))

        self.medium = QComboBox()
        self.medium.addItems(MEDIUMS)
        self.medium.setCurrentText(self.application.get("Medium", "") or MEDIUMS[0])

        self.status = QComboBox()
        self.status.addItems(STATUSES)
        self.status.setCurrentText(self.application.get("Status", "") or STATUSES[0])

        self.last_update = QDateEdit()
        self.last_update.setCalendarPopup(True)
        self.last_update.setDisplayFormat("yyyy-MM-dd")
        self.last_update.setDate(qdate_from_string(self.application.get("Last Update"), True))

        self.followup_enabled = QComboBox()
        self.followup_enabled.addItems(["No follow-up date", "Set follow-up date"])

        self.followup = QDateEdit()
        self.followup.setCalendarPopup(True)
        self.followup.setDisplayFormat("yyyy-MM-dd")
        existing_followup = self.application.get("Next Follow-up", "")
        if existing_followup:
            self.followup_enabled.setCurrentIndex(1)
            self.followup.setDate(qdate_from_string(existing_followup, True))
        else:
            self.followup.setDate(QDate.currentDate())

        self.url = QLineEdit(self.application.get("Job URL", ""))
        self.notes = QTextEdit()
        self.notes.setPlainText(self.application.get("Notes", ""))

        form.addRow("Company:", self.company)
        form.addRow("Country:", self.country)
        form.addRow("Date of application:", self.application_date)
        form.addRow("Position:", self.position)
        form.addRow("Application medium:", self.medium)
        form.addRow("Status:", self.status)
        form.addRow("Last update:", self.last_update)
        form.addRow("Follow-up:", self.followup_enabled)
        form.addRow("Follow-up date:", self.followup)
        form.addRow("Job posting URL:", self.url)
        form.addRow("Notes:", self.notes)

        layout.addLayout(form)

        buttons = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.validate_and_accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def validate_and_accept(self):
        if not self.company.text().strip():
            QMessageBox.warning(self, "Missing information", "Please enter a company.")
            return
        if not self.position.text().strip():
            QMessageBox.warning(self, "Missing information", "Please enter a position.")
            return
        self.accept()

    def get_data(self):
        followup = ""
        if self.followup_enabled.currentIndex() == 1:
            followup = self.followup.date().toString("yyyy-MM-dd")

        return {
            "Company": self.company.text().strip(),
            "Country": self.country.currentText().strip(),
            "Date": self.application_date.date().toString("yyyy-MM-dd"),
            "Position": self.position.text().strip(),
            "Medium": self.medium.currentText(),
            "Status": self.status.currentText(),
            "Last Update": self.last_update.date().toString("yyyy-MM-dd"),
            "Next Follow-up": followup,
            "Job URL": self.url.text().strip(),
            "Notes": self.notes.toPlainText().strip(),
        }


class JobTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Easy Tracker")
        self.resize(1280, 760)
        self.applications = load_applications()
        self.filtered_indices = list(range(len(self.applications)))
        self.theme_name = load_theme()
        self.sort_column = None
        self.sort_ascending = True

        self.hover_row = -1
        self.hover_global_pos = QPoint()
        self.note_tooltip = None
        self.hover_timer = QTimer(self)
        self.hover_timer.setSingleShot(True)
        self.hover_timer.setInterval(2000)
        self.hover_timer.timeout.connect(self.show_note_tooltip)

        self.build_ui()
        self.apply_theme(self.theme_name)
        self.refresh_table()

    def build_ui(self):
        root = QWidget()
        self.setCentralWidget(root)
        main = QVBoxLayout(root)
        main.setContentsMargins(18, 18, 18, 18)
        main.setSpacing(12)

        top = QHBoxLayout()

        title_box = QVBoxLayout()
        title = QLabel("EASY TRACKER")
        title.setStyleSheet("font-size: 21px; font-weight: 700;")
        subtitle = QLabel("Keep all your applications in one place.")
        subtitle.setStyleSheet("opacity: 0.7;")
        title_box.addWidget(title)
        title_box.addWidget(subtitle)
        top.addLayout(title_box)
        top.addStretch()

        self.add_button = QPushButton("+ Add Application")
        self.add_button.setObjectName("primaryButton")
        self.add_button.clicked.connect(self.add_application)
        top.addWidget(self.add_button)

        main.addLayout(top)

        controls = QHBoxLayout()
        controls.addWidget(QLabel("Search:"))

        self.search = QLineEdit()
        self.search.setPlaceholderText("Company, position, country, status...")
        self.search.setMinimumWidth(320)
        self.search.textChanged.connect(self.refresh_table)
        controls.addWidget(self.search)

        controls.addSpacing(12)
        controls.addWidget(QLabel("Appearance:"))

        self.theme_combo = QComboBox()
        self.theme_combo.addItems(THEMES.keys())
        self.theme_combo.setCurrentText(self.theme_name)
        self.theme_combo.currentTextChanged.connect(self.change_theme)
        controls.addWidget(self.theme_combo)

        controls.addStretch()

        self.selection_hint = QLabel("Ctrl/Shift-click for multi-select")
        self.selection_hint.setStyleSheet("opacity: 0.65;")
        controls.addWidget(self.selection_hint)
        main.addLayout(controls)

        self.table = QTableWidget(0, len(TABLE_FIELDS))
        self.table.setHorizontalHeaderLabels(TABLE_FIELDS)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setAlternatingRowColors(True)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionsClickable(True)
        self.table.horizontalHeader().sectionClicked.connect(self.sort_by_column)

        stretch_cols = {0: 1, 1: 1, 2: 1, 3: 2, 4: 1, 5: 1, 6: 1, 7: 1}
        for col, stretch in stretch_cols.items():
            mode = QHeaderView.Stretch if stretch > 0 else QHeaderView.ResizeToContents
            self.table.horizontalHeader().setSectionResizeMode(col, mode)

        self.table.doubleClicked.connect(self.edit_selected)
        self.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(self.open_context_menu)

        self.table.setMouseTracking(True)
        self.table.viewport().setMouseTracking(True)
        self.table.viewport().installEventFilter(self)

        main.addWidget(self.table)

        actions = QHBoxLayout()
        self.edit_button = QPushButton("Edit Selected")
        self.delete_button = QPushButton("Delete Selected")
        self.open_button = QPushButton("Open Job URL(s)")

        self.edit_button.clicked.connect(self.edit_selected)
        self.delete_button.clicked.connect(self.delete_selected)
        self.open_button.clicked.connect(self.open_selected_urls)

        actions.addWidget(self.edit_button)
        actions.addWidget(self.delete_button)
        actions.addWidget(self.open_button)
        actions.addStretch()
        main.addLayout(actions)

        self.stats = QLabel()
        self.stats.setStyleSheet("font-weight: 600;")
        main.addWidget(self.stats)

        delete_action = QAction(self)
        delete_action.setShortcut("Delete")
        delete_action.triggered.connect(self.delete_selected)
        self.addAction(delete_action)

    def apply_theme(self, name):
        QApplication.instance().setStyleSheet(THEMES[name])

    def change_theme(self, name):
        self.theme_name = name
        save_theme(name)
        self.apply_theme(name)

    def get_filtered_indices(self):
        q = self.search.text().strip().lower()

        if not q:
            indices = list(range(len(self.applications)))
        else:
            indices = []
            for i, app in enumerate(self.applications):
                haystack = " ".join(app.get(field, "") for field in FIELDS).lower()
                if q in haystack:
                    indices.append(i)

        if self.sort_column is not None:
            field = TABLE_FIELDS[self.sort_column]

            def sort_key(index):
                value = self.applications[index].get(field, "").strip()

                if field in ("Date", "Last Update", "Next Follow-up"):
                    if not value:
                        return (1, "")
                    try:
                        return (0, datetime.strptime(value, "%Y-%m-%d"))
                    except ValueError:
                        return (0, value.lower())

                return (0, value.lower())

            indices.sort(key=sort_key, reverse=not self.sort_ascending)

        return indices

    def sort_by_column(self, column):
        if self.sort_column == column:
            self.sort_ascending = not self.sort_ascending
        else:
            self.sort_column = column
            self.sort_ascending = True

        self.refresh_table()

    def refresh_table(self):
        self.filtered_indices = self.get_filtered_indices()
        self.table.setRowCount(len(self.filtered_indices))

        for row, app_index in enumerate(self.filtered_indices):
            app = self.applications[app_index]
            for col, field in enumerate(TABLE_FIELDS):
                item = QTableWidgetItem(app.get(field, ""))
                item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(row, col, item)

            status = app.get("Status", "")
            if status in STATUS_COLORS:
                color = STATUS_COLORS[status]
                from PySide6.QtGui import QColor, QBrush
                status_item = self.table.item(row, TABLE_FIELDS.index("Status"))
                status_item.setBackground(QBrush(QColor(color)))
                status_item.setForeground(QBrush(QColor("#000000")))

        counts = {s: sum(a.get("Status") == s for a in self.applications) for s in STATUSES}
        self.stats.setText(
            f"Total: {len(self.applications)}   |   "
            f"Waiting: {counts['Waiting']}   |   "
            f"Interviewing: {counts['Interviewing']}   |   "
            f"Follow-up: {counts['Follow-up']}   |   "
            f"Offers: {counts['Offer']}   |   "
            f"Accepted: {counts['Accepted']}   |   "
            f"Rejected: {counts['Rejected']}"
        )

    def selected_app_indices(self):
        selected_rows = sorted({index.row() for index in self.table.selectionModel().selectedRows()})
        return [self.filtered_indices[row] for row in selected_rows]

    def add_application(self):
        dlg = ApplicationDialog(self)
        if dlg.exec() == QDialog.Accepted:
            self.applications.append(dlg.get_data())
            save_applications(self.applications)
            self.refresh_table()

    def edit_selected(self):
        indices = self.selected_app_indices()
        if not indices:
            QMessageBox.information(self, "No selection", "Select an application first.")
            return
        if len(indices) > 1:
            QMessageBox.information(self, "Multiple selection", "Select only one application to edit.")
            return

        i = indices[0]
        dlg = ApplicationDialog(self, self.applications[i])
        if dlg.exec() == QDialog.Accepted:
            self.applications[i] = dlg.get_data()
            save_applications(self.applications)
            self.refresh_table()

    def delete_selected(self):
        indices = self.selected_app_indices()
        if not indices:
            QMessageBox.information(self, "No selection", "Select one or more applications first.")
            return

        reply = QMessageBox.question(
            self,
            "Delete application(s)?",
            f"Delete {len(indices)} selected application(s)?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            for i in sorted(indices, reverse=True):
                del self.applications[i]
            save_applications(self.applications)
            self.refresh_table()

    def open_selected_urls(self):
        indices = self.selected_app_indices()
        if not indices:
            QMessageBox.information(self, "No selection", "Select one or more applications first.")
            return

        opened = 0
        missing = 0
        for i in indices:
            url = self.applications[i].get("Job URL", "").strip()
            if not url:
                missing += 1
                continue
            if not url.startswith(("http://", "https://")):
                url = "https://" + url
            QDesktopServices.openUrl(QUrl(url))
            opened += 1

        if opened == 0:
            QMessageBox.information(self, "No URLs", "None of the selected applications has a Job URL.")
        elif missing:
            QMessageBox.information(
                self, "Some URLs missing",
                f"Opened {opened} link(s). {missing} selected application(s) had no URL."
            )

    def eventFilter(self, obj, event):
        if obj is self.table.viewport():
            if event.type() == event.Type.MouseMove:
                index = self.table.indexAt(event.pos())
                row = index.row()

                if row != self.hover_row:
                    self.hide_note_tooltip()
                    self.hover_timer.stop()
                    self.hover_row = row

                    if row >= 0:
                        self.hover_global_pos = self.table.viewport().mapToGlobal(event.pos())
                        self.hover_timer.start()

                elif row >= 0:
                    self.hover_global_pos = self.table.viewport().mapToGlobal(event.pos())

            elif event.type() in (
                event.Type.Leave,
                event.Type.MouseButtonPress,
                event.Type.Wheel
            ):
                self.hover_timer.stop()
                self.hover_row = -1
                self.hide_note_tooltip()

        return super().eventFilter(obj, event)

    def show_note_tooltip(self):
        if self.hover_row < 0 or self.hover_row >= len(self.filtered_indices):
            return

        app_index = self.filtered_indices[self.hover_row]
        notes = self.applications[app_index].get("Notes", "").strip()

        if not notes:
            return

        self.hide_note_tooltip()

        tooltip = QLabel(None, Qt.ToolTip)
        tooltip.setText(notes)
        tooltip.setWordWrap(True)
        tooltip.setMaximumWidth(360)
        tooltip.setMinimumWidth(220)
        tooltip.setStyleSheet("""
            QLabel {
                background: #FFFDF2;
                color: #202020;
                border: 1px solid #B8B8B8;
                border-radius: 6px;
                padding: 10px;
                font-family: "Segoe UI";
                font-size: 9pt;
            }
        """)

        tooltip.adjustSize()
        tooltip.move(self.hover_global_pos + QPoint(18, 18))
        tooltip.show()
        self.note_tooltip = tooltip

    def hide_note_tooltip(self):
        if self.note_tooltip is not None:
            self.note_tooltip.close()
            self.note_tooltip.deleteLater()
            self.note_tooltip = None

    def open_context_menu(self, pos):
        menu = QMenu(self)
        edit_action = menu.addAction("Edit")
        open_action = menu.addAction("Open Job URL(s)")
        delete_action = menu.addAction("Delete")

        action = menu.exec(self.table.viewport().mapToGlobal(pos))
        if action == edit_action:
            self.edit_selected()
        elif action == open_action:
            self.open_selected_urls()
        elif action == delete_action:
            self.delete_selected()


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Easy Tracker")
    app.setStyle("Fusion")

    if os.path.exists(ICON_FILE):
        app.setWindowIcon(QIcon(ICON_FILE))

    window = JobTracker()
    if os.path.exists(ICON_FILE):
        window.setWindowIcon(QIcon(ICON_FILE))
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
