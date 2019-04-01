import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
config=pygal.Config()
print('Status code : ',r.status_code)
response_dict=r.json()
print(response_dict.keys())
print("Total count ",response_dict["total_count"])
repo_dicts=response_dict['items']
print("Repo returned "+str(len(repo_dicts)))
repo_dict=repo_dicts[0]
print("\n keys",len(repo_dict))
names,plot_dicts=[],[]
config.show_legend=False
config.x_label_rotation=45
config.title_font_size=24
config.label_font_size = 14
config.major_label_font_size = 18
config.truncate_label = 15
config.show_y_guides = False
config.width = 1000
for i in repo_dicts:
    plot_dict={'value':i['stargazers_count'],
    'label':i['description']}
    plot_dicts.append(plot_dict)
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(config,style=my_style)
chart.title="Most py stars in github"
chart.x_labels=names
chart.add("",plot_dicts)
chart.render_to_file("pyRequest.svg")
