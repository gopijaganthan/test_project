"""
API endpoints for Cars 
"""

from .Base_API import Base_API
from conf import api_enpoint_conf as conf
import json

class Eu_Speedy_Madstreetden_API_Endpoints(Base_API):
	"Class for madstreetden endpoints"

	def append_base_url(self,suffix=''):
		"""Append API end point to base URL"""
		return conf.eu_central+suffix

	def get_config(self,data,headers):
		"Get configuration"
		url = self.append_base_url('/get_config')
		json_response = self.post(url,json=data,headers=headers)

		return {
			'url':url,
			'response':json_response['json_response']
		}