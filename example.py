            
import logging
from datetime import datetime
from src.recon_client import ReconSession

# onReady handler         
def onReady(tools):
    logging.debug("Session established [%s]" % str(datetime.now()))
    print("Session ready!")

# main message handler
def messageHandler_all(ws, message):
    print("\n\nGOT MESSAGE:\n", message) 
    
# Example of a custom promise-handler - for tool execution
def messageHandler_geoIp(result):
    print("\n\nGeo-IP Result: \n", result)

api_key = "YOUR_API_KEY"

# Create a ReconSession object - For development purposes, we are using wss://test.recon.us.com:2096, recon.us.com is not API-enabled yet. 
rs = ReconSession(messageHandler_all, apiKey = api_key, onReady = onReady, api = "wss://test.recon.us.com:2096")

# Test tool execution
rs.tool_exec('geoip', 'google.com', handler = messageHandler_geoIp)
