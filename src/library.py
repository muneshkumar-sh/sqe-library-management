def fine_tier(days_overdue):
    if days_overdue < 0:
        raise ValueError("Days overdue cannot be negative")
    elif days_overdue == 0:
        return "None"
    elif days_overdue <= 7:
        return "Low"
    elif days_overdue <= 14:
        return "Medium"
    elif days_overdue <= 30:
        return "High"
    else:
        return "Severe"

class Library:
    def __init__(self):
        self.loans = {}

    def borrow_book(self, member_id, isbn):
        current_books = self.loans.get(member_id, 0)

        if current_books >= 5:
            raise ValueError("Borrow limit exceeded")

        self.loans[member_id] = current_books + 1