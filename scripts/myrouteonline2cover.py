#!/usr/bin/python

import csv
import pystache
import sys

# Parse routes
routes = {}

with open(sys.argv[1], 'r') as routes_file:
    routes_csv_file = csv.DictReader(routes_file)

    for row in routes_csv_file:
        # If it has a record id assigned (it's in the Territory col)
        if 'Territory' in row and row['Territory'] is not '':
            route_num = int(row['Route'])
            request_id = int(row['Territory'])
            # print 'Route %s, #%d' % (route_num, request_id,)

            # Init the list if it doesn't exist
            if route_num not in routes.keys():
                routes[route_num] = []

            # Append the request id, in order
            routes[route_num].append(request_id)

    # print routes


# Parse requests
requests = {}
with open(sys.argv[2], 'r') as requests_file:
    requests_csv_file = csv.DictReader(requests_file)

    for row in requests_csv_file:
        request_id = int(row['id'])

        requests[request_id] = row

    # print requests.keys()

# Assemble template data
template_data = []
for route_key in routes:
    route_requests = [requests[id] for id in routes[route_key]]
    distribution_site = route_requests[0].get('distribution_site')

    template_data.append({
        'id': route_key,
        'distribution_site': distribution_site,
        'requests': route_requests
    })

template_data = {'routes': template_data}

# print template_data
with open(sys.argv[3], 'r') as template_file:
    template_str = template_file.read()

    print pystache.render(template_str, template_data)
