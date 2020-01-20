from django.db import models
from dashboard.models import DecisionTree
from django.contrib.auth.models import User

class PublishedTree(models.Model):
    url             = models.SlugField(unique=True, default="")
    decision_tree   = models.ForeignKey(DecisionTree, on_delete=models.CASCADE)
    tree_data       = models.TextField(null=True, blank=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    owner           = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
