from rest_framework import serializers
from .models import Poll

class PollSerializer(serializers.ModelSerializer):

    agreeRate = serializers.SerializerMethodField()
    disagreeRate = serializers.SerializerMethodField()
    
    def get_agreeRate(self, obj):

        agrees = obj.agree
        disagrees = obj.disagree
        
        if agrees == 0:
            return 0
        else:
            return agrees / (agrees + disagrees)
        
    def get_disagreeRate(self, obj):

        agrees = obj.agree
        disagrees = obj.disagree
        
        if disagrees == 0:
            return 0
        else:
            return disagrees / (agrees + disagrees)
    
    class Meta:

        model = Poll
        fields = (
            'id',
            'title',
            'description',
            'agree',
            'disagree',
            'agreeRate',
            'disagreeRate',
            'createdAt'
            )
        
          
         