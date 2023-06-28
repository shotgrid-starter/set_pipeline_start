name = 'ww'

version = '1.0.0'

description = 'This is Custom packages. 개발 초기 사용할 패키지들을 패키징함.'

authors = ['SungWoo Park', 'HeeJeong Im', 'SunJun Park', 'EunJin Kang', 'WonGyu Lee', 'EuiMin Lee']

tools = []

requires = [
	'python',
	'pycharm',
	'shotgun_api3',
	'openpyxl',
	'ffmpeg',
	'ffmpeg_python',
	'PySide2',
	'Fileseq',
	'et_xmlfile',
	'OpenEXR',
	'Pillow'
]

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/python")
