from django.db import models


# Creates model of University Class

class UniversityCampus(models.Model):
    name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_id = models.IntegerField(default="", blank=True, null=False)

    # Creates model manager
    object = models.Manager()

    def __str__(self):
        # Returns the input value of the campus id and name
        # field as tuple to display in the browser instead of the default titles
        display_name = '{0.campus_id}: {0.name}'
        return display_name.format(self)

    # Displays the model class as 'University Campus' instead of 'UniversityCampus'
    # Creates readable name for object in plural form
    class Meta:
        verbose_name = "University Campus"
        verbose_name_plural = "University Campuses"
