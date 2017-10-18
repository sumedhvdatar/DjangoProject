from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from photos.models import Photos,AppUsers
import logging


logging.basicConfig(filename='activity.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

def manage(request):
    all_photos = Photos.objects.all()
    context = {'all_photos': all_photos, }
    return render(request, 'photos/login.html',context)


def index(request):
    template = loader.get_template('photos/login.html')
    all_photos = Photos.objects.all()
    context = {'all_photos' : all_photos, }
    return render(request,'photos/home.html',context)
    #return HttpResponse(template.render(context,request))

def login(request):
    try:
        logging.debug("reached here")
        #return render(request,'photos/home.html')
        if request.method == 'GET':
            context = {}
            dict = {}
            username = request.GET['username']
            logging.debug(username)
            password = request.GET['password']
            user_full_details = []
            user_list = AppUsers.objects.filter(username = username)
            if user_list:
                logging.debug("reachedd the if condition")
                for user in user_list:
                    if user.password == password:
                        all_photos = Photos.objects.all()
                        dict['all_photos'] = all_photos
                        dict['username'] = user.username
                        # user_full_details.append(db_username)
                        dict['password'] = user.password
                        # user_full_details.append(db_password)
                        dict['permission'] = user.permission
                        # user_full_details.append(db_permission)
                        # context = {'all_photos' : user }
                        logging.debug("Done")
                        logging.debug(user_full_details)
                        break
                    else:
                        logging.debug("Invalid username")
            else:
                logging.debug("please try again")
            logging.debug("Returning to UI")

            return render(request,'photos/home.html',dict)
        else:
            return render(request, 'photos/login.html')
    except Exception as e:
        return render(request,'photos/login.html')

