from FlaskTest import db,models
from datetime import datetime

import random

class AccuracyBarChart:
        @staticmethod
        def accuracydata(filtertype_Accuracy):

            if filtertype_Accuracy=="Top 4":
                #join us model tables together
                usmodeldata = db.session.query(models.Sport,models.Timeslot,models.Statistics).filter(models.Sport.id == models.Timeslot.sport_id) \
                                             .filter(models.Sport.id == models.Statistics.sport_id).order_by(models.Statistics.accuracy.desc()).limit(4).all()
            elif filtertype_Accuracy=="Top 6":
                 #join us model tables together
                usmodeldata = db.session.query(models.Sport,models.Timeslot,models.Statistics).filter(models.Sport.id == models.Timeslot.sport_id) \
                                             .filter(models.Sport.id == models.Statistics.sport_id).order_by(models.Statistics.accuracy.desc()).limit(6).all()
            else:
                 #join us model tables together
                usmodeldata = db.session.query(models.Sport,models.Timeslot,models.Statistics).filter(models.Sport.id == models.Timeslot.sport_id) \
                                             .filter(models.Sport.id == models.Statistics.sport_id).all()


            #get label names
            labels ="["
            for sportdata in usmodeldata:
                labels=labels + "'" + sportdata.Timeslot.team + "',"

            labels=labels[:-1] 
            labels = labels + "]"

            #get data values
            backgroundcolor = "["
            data ="["
            for sportdata in usmodeldata:
                r = lambda: random.randint(0,255)
                data=data + str(sportdata.Statistics.accuracy) + ","
                backgroundcolor=backgroundcolor + "'" + '#%02X%02X%02X' % (r(),r(),r()) + "',"



            data=data[:-1] 
            data = data + "]"

            backgroundcolor=backgroundcolor[:-1] 
            backgroundcolor = backgroundcolor + "]"

            items = {'data':  data, 'labels': labels,'backgroundcolor':backgroundcolor}
            return items
