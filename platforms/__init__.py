"""Platforms package"""
from .email_sender import send_email
from .whatsapp import send_whatsapp

__all__ = ['send_email', 'send_whatsapp']
