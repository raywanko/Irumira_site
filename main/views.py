from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django import forms

# --- 既存 HomeView ---
class HomeView(TemplateView):
    template_name = 'main/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company_name'] = '株式会社イルネラ'
        context['services'] = [
            {'title': '社長挨拶', 'subtitle': 'PRESIDENT MESSAGE'},
            {'title': '会社概要・役員一覧', 'subtitle': 'COMPANY PROFILE'},
            {'title': '沿革', 'subtitle': 'HISTORY'},
            {'title': '経営報告', 'subtitle': 'REPORT'}
        ]
        return context

# --- CONTACT 用フォーム ---
class ContactForm(forms.Form):
    name = forms.CharField(label='お名前', max_length=100, widget=forms.TextInput(attrs={'class':'form-input'}))
    email = forms.EmailField(label='メールアドレス', widget=forms.EmailInput(attrs={'class':'form-input'}))
    message = forms.CharField(label='お問い合わせ内容', widget=forms.Textarea(attrs={'class':'form-textarea'}))

class ContactView(FormView):
    template_name = 'main/contact.html'
    form_class = ContactForm
    success_url = '/contact/success/'

    def form_valid(self, form):
        # メール送信やDB保存はここに追加
        return super().form_valid(form)

class ContactSuccessView(TemplateView):
    template_name = 'main/contact_success.html'
