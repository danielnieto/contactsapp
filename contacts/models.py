from django.db import models
from enum import StrEnum, auto
from threading import Thread
import time
from .managers import ContactManager


class Contact(models.Model):
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)  # Assuming phone numbers as strings
    email = models.EmailField(unique=True)
    objects = ContactManager()

    def __str__(self):
        return f"{self.first} {self.last}"


class ArchiverStatus(StrEnum):
    WAITING = auto()
    RUNNING = auto()
    COMPLETE = auto()


class Archiver:
    _instance = None
    status = ArchiverStatus.WAITING
    progress = 0
    thread = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def run(self):
        if self.status == ArchiverStatus.WAITING:
            self.status = ArchiverStatus.RUNNING
            self.progress = 0
            self.thread = Thread(target=self.run_impl)
            self.thread.start()

    def run_impl(self):
        while self.progress < 100:
            time.sleep(0.4)
            self.progress += 10
        self.status = ArchiverStatus.COMPLETE

    def reset(self):
        self.status = ArchiverStatus.WAITING
        self.progress = 0
        self.thread = None
