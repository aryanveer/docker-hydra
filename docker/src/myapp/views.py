from builtins import dict
from django.views.generic import TemplateView
from .tasks import show_hello_world
from django.http import HttpResponse
from django.shortcuts import render_to_response,render
from math import floor, ceil
import json
# Create your views here.

class ShowHelloWorld(TemplateView):
    template_name='hello_world.html'

    def get(self, *args, **kwargs):
        show_hello_world.apply()
        return super().get(*args, **kwargs)


def home(request,id=None):
    data = dict()

    data["graph_data"] = "10,10,10,20,20,20,30,30,30,40,40,40,10"

    data["wordcloud_list"] = ['hello','blah','kashmir','article370','blah','blah']

    data["top_influencer"] = [{"image":"/static/img/avatar1.jpg", "name":'AAA'},
							{"image":"/static/img/avatar1.jpg", "name":'BBB'},
							{"image":"/static/img/avatar1.jpg", "name":'CCC'},
							{"image":"/static/img/avatar1.jpg", "name":'DDD'},
							{"image":"/static/img/avatar1.jpg", "name":'EEE'},
							{"image":"/static/img/avatar1.jpg", "name":'FFF'},]

    data["top_mentions"] = [{"image":"/static/img/avatar3.jpg", "name":'AAA'},
							{"image":"/static/img/avatar3.jpg", "name":'BBB'},
							{"image":"/static/img/avatar3.jpg", "name":'CCC'},
							{"image":"/static/img/avatar3.jpg", "name":'DDD'},
							{"image":"/static/img/avatar3.jpg", "name":'EEE'},
							{"image":"/static/img/avatar3.jpg", "name":'FFF'},]

    heading = "Heading"
    content = "Content Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s"
    badge = ["xyz","abc"]
    badge2 = ["blah", "hello"]
    badge3 = ["foo", "bar"]

    data["themes"] = [ {'heading': heading,
		 'content': content,
		 'badge': badge},
		{'heading': heading,
		 'content': content,
		 'badge': badge},
		{'heading': heading,
		 'content': content,
		 'badge': badge},
		{'heading': heading,
		 'content': content,
		 'badge': badge},
		{'heading': heading,
		 'content': content,
		 'badge': badge} ]

    data["headlines"] = [{'heading': heading,
			   'content': content,
			   'badge': badge},
			  {'heading': heading,
			   'content': content,
			   'badge': badge2},
			  {'heading': heading,
			   'content': content,
			   'badge': badge3}]

    data["events"] = [{"date":"21st Jan, 2019",
					   'events': [{'time':'11:55 am',
								   'content': "Added John Silver as a friend"},
								  {'time': '11:55 am',
								   'content': "Added John Silver as a friend"},
								  {'time': '11:55 am',
								   'content': "Added John Silver as a friend"},
								  ]},
					  {"date": "3rd Feb, 2019",
					   'events': [{'time': '11:55 am',
								   'content': "Added John Silver as a friend"},
								  {'time': '11:55 am',
								   'content': "Added John Silver as a friend"},
								  {'time': '11:55 am',
								   'content': "Added John Silver as a friend"},
								  ]},
					  {"date": "9th Mar, 2019",
					   'events': [{'time': '11:55 am',
								   'content': "Added John Silver as a friend"},
								  {'time': '11:55 am',
								   'content': "Added John Silver as a friend"},
								  {'time': '11:55 am',
								   'content': "Added John Silver as a friend"},
								  ]},
					  ]


    count_data = [{"count": "2.39 L",
					"source": "Facebook"},
					{"count": "1.74 L",
					"source": "Twitter"},
					{"count": "4.82 L",
					"source": "Youtube"},
					{"count": "1.22 L",
					"source": "Tumblr"},
					{"count": "1.87 L",
					"source": "Pastebin"},
					{"count": "1.02 L",
					"source": "Instagram"}]

    data["crawled_count"] = {"total_count": "72,354,69",
							 "first_part": count_data[:ceil(len(count_data)/2)],
							 "second_part": count_data[ceil(len(count_data)/2):]
							 }

    data["posts_count"] = [{"count": "7.484",
						   "source": "Textual Posts",
						   "percent": "12%"},
						  {"count": "3,248",
						   "source": "Multimedia",
						   "percent": "12%"},
						  {"count": "784.12",
						   "source": "Users",
						   "percent": "12%"},
						  {"count": "41561",
						   "source": "Alerts",
						   "percent": "12%"},
						  {"count": "79265",
						   "source": "Hashtags",
						   "percent": "12%"},
						  {"count": "45643",
						   "source": "Tabloid",
						   "percent": "12%"}]

    return render(request, 'index.html', data)
