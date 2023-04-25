import dask
dask.config.set(scheduler='threads')
import dask.dataframe as dd

# read data
data = dd.read_json(f"/pfs/work7/workspace/scratch/tu_zxobe27-hiwi_project/data/downloads/extracted/*", lines = False)

# process and export data
data.query("year >= 2010").loc[:,["id", "title", "paperAbstract", "year", "journalName", "doi"]].to_csv("/pfs/work7/workspace/scratch/tu_zxobe27-hiwi_project/data/reduced")