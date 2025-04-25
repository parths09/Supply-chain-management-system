from decimal import Decimal

orders_data = [
    {
        "order_id": 1001,
        "customer_id": 1,
        "total_amount": Decimal('3900.00'),
        "status": "Pending",
        "shippings": [
            {
                "shipping_id": 5001,
                "tracking_number": "TRK001",
                "status": "Pending",
                "items": [
                    {"inventory_id": 1, "quantity": 2, "amount": Decimal('900.00')},
                    {"inventory_id": 2, "quantity": 1, "amount": Decimal('450.00')}
                ]
            },
            {
                "shipping_id": 5002,
                "tracking_number": "TRK002",
                "status": "Pending",
                "items": [
                    {"inventory_id": 3, "quantity": 3, "amount": Decimal('2550.00')}
                ]
            }
        ]
    },
    {
        "order_id": 1002,
        "customer_id": 2,
        "total_amount": Decimal('850.00'),
        "status": "Pending",
        "shippings": [
            {
                "shipping_id": 5003,
                "tracking_number": "TRK003",
                "status": "Pending",
                "items": [
                    {"inventory_id": 5, "quantity": 2, "amount": Decimal('550.00')},
                    {"inventory_id": 6, "quantity": 1, "amount": Decimal('300.00')}
                ]
            }
        ]
    },
    {
        "order_id": 1003,
        "customer_id": 3,
        "total_amount": Decimal('40150.00'),
        "status": "Pending",
        "shippings": [
            {
                "shipping_id": 5004,
                "tracking_number": "TRK004",
                "status": "Pending",
                "items": [
                    {"inventory_id": 8, "quantity": 4, "amount": Decimal('39200.00')},
                    {"inventory_id": 9, "quantity": 1, "amount": Decimal('950.00')}
                ]
            }
        ]
    },
    {
        "order_id": 1004,
        "customer_id": 4,
        "total_amount": Decimal('3600.00'),
        "status": "Pending",
        "shippings": [
            {
                "shipping_id": 5005,
                "tracking_number": "TRK005",
                "status": "Pending",
                "items": [
                    {"inventory_id": 12, "quantity": 1, "amount": Decimal('1400.00')},
                    {"inventory_id": 13, "quantity": 1, "amount": Decimal('2200.00')}
                ]
            }
        ]
    },
    {
        "order_id": 1005,
        "customer_id": 5,
        "total_amount": Decimal('90000.00'),
        "status": "Pending",
        "shippings": [
            {
                "shipping_id": 5006,
                "tracking_number": "TRK006",
                "status": "Pending",
                "items": [
                    {"inventory_id": 10, "quantity": 5, "amount": Decimal('90000.00')}
                ]
            }
        ]
    },
    {
        "order_id": 1006,
        "customer_id": 1,
        "total_amount": Decimal('2250.00'),
        "status": "Pending",
        "shippings": [
            {
                "shipping_id": 5007,
                "tracking_number": "TRK007",
                "status": "Pending",
                "items": [
                    {"inventory_id": 16, "quantity": 2, "amount": Decimal('1500.00')},
                    {"inventory_id": 17, "quantity": 1, "amount": Decimal('750.00')}
                ]
            }
        ]
    },
    {
        "order_id": 1007,
        "customer_id": 2,
        "total_amount": Decimal('6230.00'),
        "status": "Pending",
        "shippings": [
            {
                "shipping_id": 5008,
                "tracking_number": "TRK008",
                "status": "Pending",
                "items": [
                    {"inventory_id": 18, "quantity": 1, "amount": Decimal('5990.00')},
                    {"inventory_id": 4, "quantity": 2, "amount": Decimal('240.00')}
                ]
            }
        ]
    },
    {
        "order_id": 1008,
        "customer_id": 3,
        "total_amount": Decimal('1575.00'),
        "status": "Pending",
        "shippings": [
            {
                "shipping_id": 5009,
                "tracking_number": "TRK009",
                "status": "Pending",
                "items": [
                    {"inventory_id": 11, "quantity": 2, "amount": Decimal('1300.00')},
                    {"inventory_id": 5, "quantity": 1, "amount": Decimal('275.00')}
                ]
            }
        ]
    },
    {
        "order_id": 1009,
        "customer_id": 4,
        "total_amount": Decimal('21400.00'),
        "status": "Pending",
        "shippings": [
            {
                "shipping_id": 5010,
                "tracking_number": "TRK010",
                "status": "Pending",
                "items": [
                    {"inventory_id": 19, "quantity": 1, "amount": Decimal('3400.00')},
                    {"inventory_id": 10, "quantity": 1, "amount": Decimal('18000.00')}
                ]
            }
        ]
    },
    {
        "order_id": 1010,
        "customer_id": 5,
        "total_amount": Decimal('15500.00'),
        "status": "Pending",
        "shippings": [
            {
                "shipping_id": 5011,
                "tracking_number": "TRK011",
                "status": "Pending",
                "items": [
                    {"inventory_id": 7, "quantity": 1, "amount": Decimal('15500.00')}
                ]
            }
        ]
    }
]
