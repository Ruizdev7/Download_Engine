import core.ngin_core as ngin_core
 
agent = ngin_core.Report_Generator("Harvest Batches")
agent.logIn()
agent.locateAnalyticsModule()
agent.downloadHarvestBatchDetails()

print(agent.__rep__)