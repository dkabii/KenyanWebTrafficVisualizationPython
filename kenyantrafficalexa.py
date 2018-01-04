import untangle
import matplotlib.pyplot as plt
class Site():
		def __init__(self,name,daily_time,daily_pageviews,percentage_search,sites_linkedin):
				self.name=name
				self.daily_time=daily_time
				self.daily_pageviews=daily_pageviews
				self.percentage_search=percentage_search
				self.sites_linkedin=sites_linkedin
		def __str__():
				str_site=("{name: %s,daily_time: %s,daily_pageviews: %s,percentage_search: %s,sites_linkedin: %s}" % 
					self.name,self.daily_time,self.daily_pageviews,self.percentage_search,self.sites_linkedin)
				return str_site

def printBreak(msg=''):
		print('********************* '+msg+' **********************')

def process_head(ele):
		tr=ele.children[0]
		for ele in tr.children:
				i=0

def process_listing(ele,arr_sites):
		sites=arr_sites
		#retrieve site name
		ele_p=ele.children[1].children[0]
		site_name=ele_p.children[0].cdata

		#retrieve daily time on site
		ele_daily_time_on_site=ele.children[2]
		site_daily_time=ele_daily_time_on_site.children[0].cdata

		#retrieve daily pageviews per visitor
		ele_daily_pageviews_per_visitor=ele.children[3]
		site_daily_pageviews_per_visitor=ele_daily_pageviews_per_visitor.children[0].cdata

		#percentage of traffic from search
		ele_search_traffic_percentage=ele.children[4]
		site_search_traffic_percentage=ele_search_traffic_percentage.children[0].cdata

		#total sites linking in
		ele_sites_linking_in=ele.children[5]
		site_sites_linkin_in=ele_sites_linking_in.children[0].cdata
		site=Site(site_name,site_daily_time,site_daily_pageviews_per_visitor,site_search_traffic_percentage,site_sites_linkin_in)
		sites.append(site)

data_obj=untangle.parse('kenyantrafficalexa.xml')
sites=[]
#divs from root element with the head of the table
divs=data_obj.children[0].children
for ele in divs:
		if(ele['class']=='thead'):
				process_head(ele)
#divs from root element with the body of the table
for div in divs[1:]:
		process_listing(div,sites)
#print(sites)

arr_names=[site.name for site in sites]
#print(arr_names)
arr_daily_times=[site.daily_time for site in sites]
#printBreak("arr_daily_times")
#print(arr_daily_times)
arr_site_daily_pageviews_per_visitor=[site.daily_pageviews for site in sites]
#printBreak("arr_site_daily_pageviews_per_visitor")
#print(arr_site_daily_pageviews_per_visitor)
arr_percentage_search=[site.percentage_search for site in sites]
arr_percentage_search_cleaned=[]
for percent in arr_percentage_search:
		percent_cleaned=percent[0:len(percent)-1]
		arr_percentage_search_cleaned.append(percent_cleaned)
#printBreak("arr_percentage_search")
#print(arr_percentage_search)
#printBreak("arr_percentage_search_cleaned")
#print(arr_percentage_search_cleaned)

arr_daily_times_secs=[]
arr_daily_times_mins=[]
for i,time in enumerate(arr_daily_times):
		time_arr=time.split(":")
		mins=int(time_arr[0])
		secs=int(time_arr[1])
		secs=mins*60+secs
		mins=mins+secs/60
		arr_daily_times_secs.append(secs)
		arr_daily_times_mins.append(secs)

#printBreak("arr_daily_times_secs")
#print(arr_daily_times_secs)
#printBreak("arr_daily_times_mins")
#print(arr_daily_times_mins)

arr_daily_pageviews=[float(site.daily_pageviews) for site in sites]
#printBreak("arr_daily_pageviews")
#print(arr_daily_pageviews)
arr_sites_linkedin=[site.sites_linkedin for site in sites]
#print(arr_sites_linkedin)
for i,str_nums in enumerate(arr_sites_linkedin):
		str_nums=str_nums.replace(',','')
		arr_sites_linkedin[i]=str_nums

x=[i+1.1 for i,_ in enumerate(arr_names)]
print(x)

#plots the daily views
def plot_daily_views(arr):
		arr_daily_pageviews=arr[:20]
		for i,pageviews in enumerate(arr_daily_pageviews):
				plt.bar([x[i]],[pageviews],label=arr_names[i])
		for i in range(21,40):
				plt.bar([i],[0])
		plt.title("Site pageviews")
		plt.ylabel("Site")
		plt.legend(loc=1)
		plt.show()

def plot_sites_linkedin(arr):
		arr_sites_linkedin=arr[:20]
		for i,linkedin_sites in enumerate(arr_sites_linkedin):
				plt.bar([x[i]],[linkedin_sites],label=arr_names[i])
		for i in range(21,40):
				plt.bar([i],[0])
		plt.title("Sites linked in")
		plt.ylabel("Site")
		plt.legend(loc=1)
		plt.show()

def plot_daily_time_secs(arr):
		arr=arr[:20]
		for i,daily_time_secs in enumerate(arr):
				plt.bar([x[i]],[daily_time_secs],label=arr_names[i])
		for i in range(21,40):
				plt.bar([i],[0])
		plt.title("Daily time on site in secs")
		plt.ylabel("Site")
		plt.legend(loc=1)
		plt.show()

#plots the values and title passed
def plot_values(arr,atitle):
		arr=arr[:20]
		for i,value in enumerate(arr):
				plt.bar([x[i]],[value],label=arr_names[i])
		for i in range(21,40):
				plt.bar([i],[0])
		plt.title(atitle)
		plt.ylabel("Site")
		plt.legend(loc=1)
		plt.show()

plot_daily_views(arr_daily_pageviews)
plot_sites_linkedin(arr_sites_linkedin)
plot_daily_time_secs(arr_daily_times_secs)
plot_values(arr_daily_times_mins,"Daily time on site in mins")
plot_values(arr_site_daily_pageviews_per_visitor,"Daily pageviews per visitor")
plot_values(arr_percentage_search_cleaned,"Daily percentage traffic from search")

