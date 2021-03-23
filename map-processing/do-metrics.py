import multiprocessing, time
from multiprocessing import Pool, Process, Manager
import pylandstats as pls
import sys, os


csvfile = '/Users/daveism/capstone/maps/metics-for-capstone.csv'
dir = '/Users/daveism/capstone/maps/map-for-s3-tifs-georef'

LandscapeMetrics=[
    'total_area',
    'number_of_patches',
    'patch_density',
    'effective_mesh_size',
    'contagion',
    'area_mn',
    'perimeter_mn',
    'perimeter_area_ratio_mn',
    'shape_index_mn',
    'fractal_dimension_mn',
    'euclidean_nearest_neighbor_mn'
]

def createMetric(args):
    file = args[0]
    metrics = args[1]
    csvfile = args[2]
    start_time = args[3]
    ls = pls.Landscape(file)
    landscape_metrics_df = ls.compute_landscape_metrics_df(metrics=metrics)
    landscape_metrics_df['image'] = file
    landscape_metrics_df['start_time'] = start_time
    landscape_metrics_df['write_time'] = time.time()

    landscape_metrics_df.to_csv(csvfile, mode='a', header=False)
    print('----------------------------------------')
    print('createMetric', file, metrics, csvfile)
    print('----------------------------------------')

if __name__ == '__main__':
    num_workers = multiprocessing.cpu_count() * 2
    pool = multiprocessing.Pool(num_workers)

    for root, dirs, files in os.walk(dir):
        for file in files:
            complete_file_path = os.path.join(root, file)
            start_time = time.time()
            arg = (complete_file_path,)
            arg +=(LandscapeMetrics,)
            arg +=(csvfile,)
            arg +=(start_time,)
            pool.apply_async(createMetric, args=(arg,))


        pool.close()
        pool.join()
