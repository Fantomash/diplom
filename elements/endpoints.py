class Endpoints:
    PORTAL_URL = 'https://www.airbnb.com/'
    EXPECTED_PORTAL_URL = 'https://www.airbnb.cat/'
    GIFT_CARDS_URL = 'https://www.airbnb.com/giftcards'
    ACCOUNT_SETTINGS = 'https://www.airbnb.com/account-settings'
    SEARCH_URL = 'https://www.airbnb.com/api/v3/Homepage'

    search_queries_data = {
        'operationName': 'Homepage',
        'locale': 'en',
        'currency': 'EUR'
    }

    search_payload_data = {
        "operationName": "Homepage",
        "variables": {
            "staysSearchRequest": {
                "requestedPageType": "HOMEPAGE",
                "metadataOnly": False,
                "searchType": "filter_change",
                "source": "structured_search_input_header",
                "treatmentFlags": [
                    "feed_map_decouple_homepage_treatment", "stays_search_rehydration_treatment_desktop",
                    "stays_search_rehydration_treatment_moweb", "selective_query_feed_map_homepage_desktop_treatment",
                    "selective_query_feed_map_homepage_moweb_treatment"
                ],
                "rawParams": [
                    {
                        "filterName": "adults",
                        "filterValues": ["1"]
                    },
                    {
                        "filterName": "categoryBarCacheId",
                        "filterValues":
                            [
                                "NTM0OCw4NTM2LDY3Nyw4MTczLDgwNDcsNTM2Niw4MjU1LDEwNzMsODY3OCw4MTc2LDgyNTMsODUyOCw3ODksNTYzNSw4MTg2LDgyMjUsODE4OCw4MTE1LDg1MjIsODUzNSw4NjU4LDc3NjksNDEwNCw4MjI2LDg2NjEsODUzOCw4MTQ0LDgxNzUsODEwMiw4NTM0LDY3MCw4MTkyLDgxMDEsODY1Nyw4MTY2LDY3NSw2MzQsODUyNiw4MTQ4LDg2NjIsODE3NCw4NTI0LDU3MzEsODUyNSw4NjUzLDgyMjcsODY1MCw4MjMyLDgxNTksODIzMCw4MjI4LDgwNDMsODE1Nyw4NTIxLDg1NDMsODA5OSw4MTg3LDU3MDgsODI1Niw4MjI5LDc3NjU="
                            ]
                    },
                    {
                        "filterName": "categoryTag",
                        "filterValues": ["Tag:8047"]
                    },
                    {
                        "filterName": "cdnCacheSafe",
                        "filterValues": ["false"]
                    },
                    {
                        "filterName": "channel",
                        "filterValues": ["EXPLORE"]
                    },
                    {
                        "filterName": "datePickerType",
                        "filterValues": ["flexible_dates"]
                    },
                    {
                        "filterName": "flexibleTripDates",
                        "filterValues": ["april"]
                    },
                    {
                        "filterName": "flexibleTripLengths",
                        "filterValues": ["one_month"]
                    },
                    {"filterName": "itemsPerGrid",
                     "filterValues": ["20"]
                     },
                    {
                        "filterName": "monthlyLength",
                        "filterValues": ["3"]
                    },
                    {
                        "filterName": "monthlyStartDate",
                        "filterValues": ["2024-01-01"]
                    },
                    {
                        "filterName": "priceFilterInputType",
                        "filterValues": ["0"]
                    },
                    {
                        "filterName": "priceFilterNumNights", "filterValues": ["5"]
                    },
                    {
                        "filterName": "query", "filterValues": []
                    },
                    {
                        "filterName": "refinementPaths", "filterValues": ["/homes"]
                    },
                    {
                        "filterName": "screenSize", "filterValues": ["large"]
                    },
                    {
                        "filterName": "searchMode", "filterValues": ["flex_destinations_search"]
                    },
                    {
                        "filterName": "tabId", "filterValues": ["home_tab"]
                    },
                    {
                        "filterName": "version", "filterValues": ["1.8.3"]
                    }
                ],
                "maxMapItems": 0},
            "staysMapSearchRequestV2":
                {
                    "requestedPageType": "HOMEPAGE",
                    "metadataOnly": False,
                    "searchType": "filter_change",
                    "source": "structured_search_input_header",
                    "treatmentFlags": [
                        "feed_map_decouple_homepage_treatment",
                        "stays_search_rehydration_treatment_desktop",
                        "stays_search_rehydration_treatment_moweb",
                        "selective_query_feed_map_homepage_desktop_treatment",
                        "selective_query_feed_map_homepage_moweb_treatment"
                    ],
                    "rawParams": [{
                        "filterName": "adults",
                        "filterValues": ["1"]
                    },
                        {"filterName": "categoryTag",
                         "filterValues": ["Tag:8047"]},
                        {
                            "filterName": "cdnCacheSafe",
                            "filterValues": ["false"]
                        },
                        {
                            "filterName": "channel",
                            "filterValues": ["EXPLORE"]
                        },
                        {
                            "filterName": "datePickerType",
                            "filterValues": ["flexible_dates"]
                        },
                        {
                            "filterName": "flexibleTripDates",
                            "filterValues": ["april"]
                        },
                        {
                            "filterName": "flexibleTripLengths",
                            "filterValues": ["one_month"]
                        },
                        {
                            "filterName": "monthlyLength",
                            "filterValues": ["3"]
                        },
                        {"filterName": "monthlyStartDate",
                         "filterValues": ["2024-01-01"]
                         },
                        {
                            "filterName": "priceFilterInputType", "filterValues": ["0"]
                        },
                        {
                            "filterName": "priceFilterNumNights", "filterValues": ["5"]
                        },
                        {
                            "filterName": "query", "filterValues": []
                        },
                        {
                            "filterName": "refinementPaths", "filterValues": ["/homes"]
                        },
                        {
                            "filterName": "screenSize", "filterValues": ["large"]
                        },
                        {
                            "filterName": "searchMode", "filterValues": ["flex_destinations_search"]
                        },
                        {
                            "filterName": "tabId", "filterValues": ["home_tab"]
                        },
                        {
                            "filterName": "version", "filterValues": ["1.8.3"]
                        }
                    ]
                },
            "includeMapResults": False,
            "announcementRequest": {"surface": "HOMEPAGE"},
            "isPaginatedRequest": False,
            "isLeanTreatment": False
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "89fdb273ede4a1361e1d2e955f7be6fc9eb352f2d9c4f8ceb2d3f79ea2584624"
            }
        }
    }

    search_params = {
        "ss": "Longyearbyen",
        "src": "searchresults",
        "checkin": "2024-01-01",
        "checkout": "2024-01-31",
        "dest_id": 900040668,
        "dest_type": "city",
        "group_adults": 1,
        "group_children": 0,
        "no_rooms": 1,
        "lang": "en-us"
    }

