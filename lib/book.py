#!/usr/bin/env python3

class Book:
    # Constructor
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
        self.current_page = 0

    # Property getter for page_count
    @property
    def page_count(self):
        return self._page_count

    # Property setter for page_count with validation
    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value
   
    # Turn the page by one
    def turn_page(self):
        if self.current_page < self.page_count:
            self.current_page += 1
            print("Flipping the page...wow, you read fast!")