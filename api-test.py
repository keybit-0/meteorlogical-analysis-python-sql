import cdsapi

import datetime
c = cdsapi.Client()
time = str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
c.retrieve(
    'reanalysis-era5-land-monthly-means',
    {
        'format': 'grib',
        'product_type': 'monthly_averaged_reanalysis',
        'variable': '2m_temperature',
        'year': '2019',
        'month': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
        ],
        'time': '00:00',
        'area': [
            53.37, -9.06, 53.27,
            -8.86,
        ],
    },
    ''+time+'_testtempGalway.grib')