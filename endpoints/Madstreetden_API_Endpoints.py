"""
API endpoints for Cars 
"""

from .Base_API import Base_API
from conf import api_enpoint_conf as conf
import json

class Madstreetden_API_Endpoints(Base_API):
	"Class for madstreetden endpoints"

	def append_base_url(self,suffix=''):
		"""Append API end point to base URL"""
		return conf.demo_mad_street_den+suffix

	def get_widget(self,data,headers):
		"Get widgets"
		url = self.append_base_url('/widgets')
		json_response = self.post(url,json=data,headers=headers)
		return {
			'url':url,
			'response':json_response['json_response']
		}


	def get_recommended_product(self,data,headers,attribute_to_select='title'):
		"Get recommended product information"
		widget_data = self.get_widget(data, headers)
		deep_Select = widget_data['response']['data'][0]
		return [d[attribute_to_select] for d in deep_Select if attribute_to_select in d]
		



	