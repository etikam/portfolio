from __future__ import annotations

from django import forms

from blog.models import Comment


class CommentForm(forms.ModelForm):
    """Form definition for Comment."""

    class Meta:
        """Meta definition for Commentform."""

        model = Comment
        fields = ("content",)
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "placeholder": "Laissez votre commentaire ici",
                    "rows": "10",
                    "class": "form-control",
                }
            )
        }
