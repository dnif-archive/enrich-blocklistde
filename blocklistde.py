import requests
import yaml
import os

inteltype = ['INTEL_ADDR']
path = os.environ["WORKDIR"]
with open(path + "/enrichment_plugins/blocklistde/dnifconfig.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)


def import_ip_intel():
    try:
        source = cfg['enrichment_plugin']['BLOCKLISTDE_IP_SOURCE']
        response = requests.get(source)
    except Exception, e:
        print 'Api Request Error %s' % e
    try:
        lines = []
        for line in response.iter_lines():
            line = line.strip()
            tmp_dict = {}
            tmp_dict["EvtType"] = "IPv4"
            tmp_dict["EvtName"] = line
            tmp_dict2 = {}
            tmp_dict2["IntelRef"] = ["BLOCKLIST"]
            tmp_dict2["IntelRefURL"] = [source]
            tmp_dict2["ThreatType"] = ["blacklist"]
            tmp_dict["AddFields"] = tmp_dict2
            lines.append(tmp_dict)
    except:
        lines = []
    return lines,'INTEL_ADDR'
