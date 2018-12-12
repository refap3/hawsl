button_obj = hass.states.get('sensor.living_room_remote_status') 
button = button_obj.state 
if button == '1': 
   hass.services.call('light', 'turn_on', { "entity_id" : 'light.tv', 'color_name': 'green' }) 
elif button == '2': 
  hass.services.call('light', 'turn_on', { "entity_id" : 'light.tv', 'color_name': 'red' }) 
elif button == '3': 
  hass.services.call('light', 'turn_on', { "entity_id" : 'light.tv', 'color_name': 'purple' }) 
elif button == '4': 
  hass.services.call('light', 'turn_on', { "entity_id" : 'light.tv', 'color_name': 'yellow' }) 