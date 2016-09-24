#coding=utf-8
#version:1.0.1
'''
Copyright (c) 2013-2014 LG Electronics, Inc.

Confidential computer software. Valid license from LG required for
possession, use or copying. Consistent with FAR 12.211 and 12.212,
Commercial Computer Software, Computer Software Documentation, and
Technical Data for Commercial Items are licensed to the U.S. Government
under vendor's standard commercial license.
'''
import unittest
import time
import os
import sys
import paramiko
import re
import json
from socket import timeout as SocketTimeout
import xml.etree.ElementTree as et
import os.path

class Scenario_test (unittest.TestCase):
	INPUT_GENERATOR_SERVICE = "com.lge.inputgenerator"
	INPUT_GENERATOR_API_PUSH_MOUSE_EVENT = "pushMouseEvent"
	INPUT_GENERATOR_API_PUSH_KEY_EVENT ="pushKeyEvent"

	CAPTURE_WIDTH = 800
	CAPTURE_HEIGHT = 600
	CAPTURE_SERVICE = "com.webos.service.tv.capture"
	CAPTURE_API_EXECUTE_ONE_SHOT = "executeOneShot"

	CAPTURE_PATH = "/media/cam/capture"

	iCnt = 0
	szLogDir = ''
	_Log = None
	_outFolder = None
	_fileFolder = None
	_testName = None
	_config = None
	_sshConnector = None
	_captureFiles = []
	testType = 0
	bCloseAllApps = False


	@classmethod
	def setUpClass(cls):
		cls._testName = os.path.splitext(os.path.basename(os.path.abspath(__file__)))[0]
		cls._Log = Logger()
		cls._config = Config()
		cls.szLogDir = cls._config.get_ssh_settings().get("workspace") + '/temp/scenario_log/'
		cls.szSceneDir = '/home/root/scenario_test'
		cls.szPmLogDir = '/home/root/scenario_test/logs'		
		if not os.path.isdir(cls.szLogDir):
			os.mkdir(cls.szLogDir)
		if not os.path.isdir(os.path.join(cls.szLogDir, 'resource')):
			os.mkdir(os.path.join(cls.szLogDir, 'resource'))				
		cls._sshConnector = SSHConnector(cls._config.get_ssh_settings())
		now = time.localtime()
		now_time = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
		cls._sshConnector.addCommandSend('date -s \'%s\'' % now_time)
		cls._sshConnector.addCommandSend('rm -f /var/log/messages*')


	def setUp(self):
		self._outFolder = None
		self._fileFolder = None

		self._Log._testName = self._testName
		self._Log.PrintTestCaseLog("TEST_START")
		self._Log.PrintRaw("----------------------------------------------------------------------")


	@classmethod
	def tearDownClass(cls):
		cls._Log.PrintTestCaseLog("TEST_END")
		''' write log file '''
		ts = int(time.time())
		szPmlogName = "pmlog_" + str(ts)+ ".log"
		if cls._outFolder is not None :
			f = open("%s/%s.log" % (cls._outFolder, cls._testName +"_" + str(ts)), "a")
		elif cls._fileFolder is not None :
			f = open("%s/%s.log" % (cls._fileFolder, cls._testName+"_" + str(ts)), "a")
		else :
			szPath = os.path.join(cls.szLogDir, cls._testName+"_" + str(ts)+ ".log")
			f = open(szPath, "a")
			szPmlogPath = cls.szPmLogDir+"/"+ szPmlogName
			cls._sshConnector.addCommandSend('cp /var/log/messages '+ szPmlogPath)
			cls._sshConnector.bulkSend()
			cls.ScpDownloadCls(szPmlogPath, os.path.join(cls.szLogDir,'resource', szPmlogName))


		cls._Log.PrintLog("FilePath|"+f.name)
		cls._Log.PrintLog("PmLogPath|"+szPmlogName)
		for line in cls._Log._printBuffer :
			f.write(line+"\n")

		f.close()
		time.sleep(1)


	'''
	@TestType: 0
	@Step : 
	@Expected : 
	'''
	def test_scenario(self):
		self._funcName = sys._getframe().f_code.co_name
		self._Log._testMethodName = self._funcName
		print 'python>> scenario_test_2.py'
		self.PRINT_LOG('TestType|Scenario|0')
		self.PRINT_LOG('Step|')
		self.PRINT_LOG('Expected|')
		 
		# Initialize
		self.bCloseAllApps = False
		self.scenarioInit()
		 
		# Test Scenario
		self.scenarioMousePosition(960, 541) # mouse move : 960,541
		self.scenarioMousePosition(601, 361) # mouse move : 601,361
		self.scenarioMousePosition(994, 344) # mouse move : 994,344
		self.scenarioKeyCodeNum(773, 'key') # key press : [773] home
		self.scenarioSleep(3) # sleep for action
		self.scenarioMousePosition(805, 422) # mouse move : 805,422
		self.scenarioKeyCodeNum(773, 'key') # key press : [773] home
		self.scenarioSleep(3) # sleep for action
		self.scenarioMousePosition(703, 481) # mouse move : 703,481
		self.scenarioKeyCodeNum(773, 'key') # key press : [773] home
		self.scenarioSleep(3) # sleep for action
		self.scenarioMousePosition(879, 413) # mouse move : 879,413
		self.scenarioKeyCodeNum(773, 'key') # key press : [773] home
		self.scenarioSleep(3) # sleep for action
		self.scenarioMousePosition(1043, 402) # mouse move : 1043,402
		self.scenarioKeyCodeNum(773, 'key') # key press : [773] home
		self.scenarioSleep(3) # sleep for action
		self.scenarioMousePosition(1058, 408) # mouse move : 1058,408
		self.scenarioKeyCodeNum(773, 'key') # key press : [773] home
		self.scenarioSleep(3) # sleep for action
		self.scenarioMousePosition(1101, 403) # mouse move : 1101,403
		self.scenarioKeyCodeNum(773, 'key') # key press : [773] home
		self.scenarioSleep(3) # sleep for action
		self.scenarioKeyCodeNum(773, 'key') # key press : [773] home
		self.scenarioSleep(3) # sleep for action
		self.scenarioKeyCodeNum(773, 'key') # key press : [773] home
		self.scenarioSleep(3) # sleep for action
		self.scenarioKeyCodeNum(773, 'key') # key press : [773] home
		self.scenarioSleep(3) # sleep for action
		self.scenarioMousePosition(1155, 472) # mouse move : 1155,472
		self.scenarioMousePosition(1914, 930) # mouse move : 1914,930
		self.scenarioSleep(5) # sleep for capture
		self.scenarioScreenCapture(self.getScrName(), True , 'CAPTURE') # screen capture
		 
		# Finalize
		self.scenarioClose()


	@classmethod
	def ScpDownloadCls(cls, remote_file, local_file ):
		SSHIp= cls._config.get_ssh_settings().get("hostname")
		SSHPort= cls._config.get_ssh_settings().get("port")
		SSHId= cls._config.get_ssh_settings().get("username")
		SSHPasswd= cls._config.get_ssh_settings().get("password")
		SSH = paramiko.SSHClient()
		SSH.set_missing_host_key_policy(paramiko.AutoAddPolicy())

		try :
			SSH.connect(hostname=SSHIp, port=SSHPort, username=SSHId)
		except :
			try :
				SSH.connect(hostname=SSHIp, port=SSHPort, username=SSHId, password=SSHPasswd)
			except :
				cls._Log.PrintRaw("SCP ScpDownloadCls error")
				return False

		scp = SCPClient(SSH.get_transport())
		scp.get(remote_file, local_file)
		SSH.close()
		return True


	def ScpUpload(self, local_file, remote_file, log=True):
		SSHIp= self._config.get_ssh_settings().get("hostname")
		SSHPort= self._config.get_ssh_settings().get("port")
		SSHId= self._config.get_ssh_settings().get("username")
		SSHPasswd= self._config.get_ssh_settings().get("password")
		SSH = paramiko.SSHClient()
		SSH.set_missing_host_key_policy(paramiko.AutoAddPolicy())

		try :
			SSH.connect(hostname=SSHIp, port=SSHPort, username=SSHId)
		except :
			try :
				SSH.connect(hostname=SSHIp, port=SSHPort, username=SSHId, password=SSHPasswd)
			except :
				if log:
					self.PRINT_LOG("ERROR|SSH ScpUpload error "+ local_file)
				return False

		scp = SCPClient(SSH.get_transport())
		scp.put(local_file, remote_file)
		SSH.close()
		return True


	def ScpDownload(self, remote_file, local_file, log, msg="CAPTURE"):
		SSHIp= self._config.get_ssh_settings().get("hostname")
		SSHPort= self._config.get_ssh_settings().get("port")
		SSHId= self._config.get_ssh_settings().get("username")
		SSHPasswd= self._config.get_ssh_settings().get("password")
		SSH = paramiko.SSHClient()
		SSH.set_missing_host_key_policy(paramiko.AutoAddPolicy())

		try :
			SSH.connect(hostname=SSHIp, port=SSHPort, username=SSHId)
		except :
			try :
				SSH.connect(hostname=SSHIp, port=SSHPort, username=SSHId, password=SSHPasswd)
			except :
				if log:
					self.PRINT_LOG("ERROR|SSH ScpDownload error "+ local_file)
				return False

		scp = SCPClient(SSH.get_transport())
		scp.get(remote_file, local_file)
		SSH.close()
		if log:
			self.PRINT_LOG(msg+"|"+local_file)
		return True


	def ScpDownloads(self):
		SSHIp= self._config.get_ssh_settings().get("hostname")
		SSHPort= self._config.get_ssh_settings().get("port")
		SSHId= self._config.get_ssh_settings().get("username")
		SSHPasswd= self._config.get_ssh_settings().get("password")
		SSH = paramiko.SSHClient()
		SSH.set_missing_host_key_policy(paramiko.AutoAddPolicy())

		try :
			SSH.connect(hostname=SSHIp, port=SSHPort, username=SSHId)
		except :
			try :
				SSH.connect(hostname=SSHIp, port=SSHPort, username=SSHId, password=SSHPasswd)
			except :
				if path['log']:
					self.PRINT_LOG("ERROR|SSH ScpDownload error ")
				return False

		scp = SCPClient(SSH.get_transport())
		for path in self._captureFiles :
			scp.get(path['remote'], path['local'])
		SSH.close()
		return True


	def is_app_launch(self, aAppId):
		bRes = self.the_app_is_running(aAppId)
		szResult = 'Fail'
		if(bRes):
			szResult = 'Pass'
			self.PRINT_LOG("AppLaunch|"+ aAppId+"|"+ szResult)
		else:
			szCapture = self.getScrName()
			fName = os.path.basename(szCapture)
			self.PRINT_LOG("AppLaunch|"+ aAppId+"|"+ szResult +"|"+fName)
			self.scenarioScreenCapture(szCapture, False , "applaunch fail" )
			self.scenarioClose()

		self.assertTrue(bRes ,"%s app is not launched!" % (aAppId))

	# 1) Function Usage
	#     self.assertFalse(self.the_app_is_running(app_id[0]), "%s app is still running!" % (app_id[0]))
	# 2) Function Response : True or False
	def the_app_is_running (self, app_id):
		#time.sleep(3)
		resp = self.running_application_list()
		print resp
		is_running = False
		for i in xrange(len(resp)):
			if str(resp[i]["id"]) == app_id:
				is_running = True
		return is_running


	def running_application_list(self):
		'''
		Returns information about current running applications on the target

		:rtype: [Dictionary]
		'''
		service = 'com.webos.applicationManager'
		api = 'running'
		parameters = '{\'subscribe\': False}'

		self._sshConnector.addLunaSend(service, api, parameters)
		response = self._sshConnector.bulkLunaSend()
		return Util.get_default_value(response, 'running', [])


	def getScrName(self):
		## Extract file name
		ts = int(time.time())

		fullPathFile = self._testName +"_" + str(ts) + "_"+ str(self.iCnt) + ".jpg"
		resp = self.szSceneDir+ '/'+ fullPathFile
		self.iCnt += 1
		return resp


	''' This function is log printing that is the parameter of 'msg' to ANCHOR ENGINE '''
	def PRINT_LOG(self, msg) :
		self._Log.PrintLog(msg)


	def scenarioInit(self) :
		self._sshConnector.addCommandSend('rm -rf ~/performance_test')
		self._sshConnector.addCommandSend('rm -rf ~/scenario_test')
		self._sshConnector.addCommandSend('mkdir ~/scenario_test')
		self._sshConnector.addCommandSend('mkdir ~/scenario_test/logs')
		if self.bCloseAllApps is True:
			self._sshConnector.addCommandSend("luna-send -n 1 palm://com.webos.applicationManager/closeAllApps '{}'")
			self._sshConnector.bulkSend()
			time.sleep(3)


	def scenarioSend(self, cmd):
		self._sshConnector.addCommandSend(cmd)


	# COMMAND  : luna-send -P -n 1 palm://com.palm.applicationManager/launch '{"id":"com.webos.app.scheduler", "params":{}}'
	# RESPONSE : {'action': 'ran', 'returnValue': True}
	def scenarioAppLaunch(self, appId) :
		self._sshConnector.addCommandSend("luna-send -P -n 1 palm://com.palm.applicationManager/launch '{\"id\":\""+appId+"\", \"params\":{}}'")


	# COMMAND  : luna-send -n 1 palm://com.lge.inputgenerator/pushMouseEvent '{"y": 800, "eventtype": "setpos", "reserve": false, "x": 280}'
	# RESPONSE : {'action': 'ran', 'returnValue': True}
	def scenarioMouseWheel(self, direction) :
		self._sshConnector.addCommandSend("luna-send -n 1 palm://com.lge.inputgenerator/pushMouseEvent '{\"scroll\": "+str(direction)+", \"eventtype\": \"wheel\"}'")


	# COMMAND  : luna-send -n 1 palm://com.lge.inputgenerator/pushMouseEvent '{"y": 800, "eventtype": "setpos", "reserve": false, "x": 280}'
	# RESPONSE : {'action': 'ran', 'returnValue': True}
	def scenarioMousePosition(self, x, y) :
		self._sshConnector.addCommandSend("luna-send -n 1 palm://com.lge.inputgenerator/pushMouseEvent '{\"x\": "+str(x)+", \"y\": "+str(y)+", \"eventtype\": \"setpos\", \"reserve\": false}'")


	# COMMAND  : luna-send -n 1 palm://com.lge.inputgenerator/pushMouseEvent '{"eventtype": "click"}'
	# RESPONSE : {'action': 'ran', 'returnValue': True}
	def scenarioMouseClick(self) :
		self._sshConnector.addCommandSend("luna-send -n 1 palm://com.lge.inputgenerator/pushMouseEvent '{\"eventtype\": \"click\"}'")

	# luna-send -f -n 1 luna://com.lge.inputgenerator/pushKeyEvent '{"keycodenum": 412, "eventtype":"key", "reserve": false}'
	# {'action': 'ran', 'returnValue': True}
	def scenarioKeyCodeNum(self, key_code_num, key_type) :
		self._sshConnector.addCommandSend("luna-send -f -n 1 luna://com.lge.inputgenerator/pushKeyEvent '{\"keycodenum\": "+str(key_code_num)+", \"eventtype\": \""+key_type+"\", \"reserve\": false}'")


	# COMMAND  : luna-send -n 1 palm://com.webos.service.tv.capture/executeOneShot '{"width": 1280, "path": "/tmp/_temp_screenshot_for_video_test_3.jpg", "format": "JPEG", "method": "DISPLAY", "height": 720}'
	# RESPONSE : { "returnValue": true }
	def scenarioScreenCapture(self, path , log =True , msg = 'CAPTURE') :
		self._sshConnector.addCommandSend("luna-send -n 1 palm://com.webos.service.tv.capture/executeOneShot '{\"width\": "+str(self.CAPTURE_WIDTH)+", \"height\": "+str(self.CAPTURE_HEIGHT)+", \"path\": \""+path+"\", \"format\": \"JPEG\", \"method\": \"DISPLAY\"}'")
		fName = os.path.basename(path)
		self._captureFiles.append({'remote':path, 'local':os.path.join(self.szLogDir + 'resource/', fName), 'log': log , 'msg': msg})
		if log:
			self.PRINT_LOG(msg+"|"+fName)


	def scenarioSleep(self, seconds) :
		self._sshConnector.bulkSend()
		time.sleep(seconds)


	def scenarioClose(self) :
		self._sshConnector.bulkSend()
		self.ScpDownloads()



class Logger(object):

	_enableTestCaseLog = True
	_enableDebugLog = False
	_testMethodName = ""
	_testName = ""
	_printBuffer = []

	''' Initialize '''
	def __init__(self, testname = "", method = ""):

		self._testName = testname
		self._testMethodName = method


	def EnableTestcaseLog(self, flag):
		self._enableTestCaseLog = flag


	def EnableDebug(self, flag):
		if flag is None :
			self._enableDebugLog = False
		else :
			self._enableDebugLog = flag


	def GetLogHeader(self):
		now = time.localtime()
		return "[%04d-%02d-%02d %02d:%02d:%02d]" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)


	def PrintTestLog(self, keyword):
		log = "%s|%s" % (self._testName, keyword)
		print log
		sys.stdout.flush()
		self._printBuffer.append("%s %s" % (self.GetLogHeader(), log))


	def PrintRaw(self, msg="None"):
		print msg
		sys.stdout.flush()
		self._printBuffer.append("%s %s" % (self.GetLogHeader(), msg))


	def PrintTestCaseLog(self, keyword, msg="", flag = False):
		if self._enableTestCaseLog or flag :
			if len(self._testMethodName) > 0 :
				if len(msg) > 0 :
					log = "%s|%s|%s|%s" % (self._testName, self._testMethodName, keyword, msg)
				else :
					log = "%s|%s|%s" % (self._testName, self._testMethodName, keyword)
			else :
				if len(msg) > 0 :
					log = "%s|%s|%s" % (self._testName, keyword, msg)
				else :
					log = "%s|%s" % (self._testName, keyword)
			print log
			sys.stdout.flush()
			self._printBuffer.append("%s %s" % (self.GetLogHeader(), log))


	def PrintDebugLog(self, msg):
		self.PrintTestCaseLog("DEBUG", msg.rstrip())


	def PrintWarningLog(self, msg):
		self.PrintTestCaseLog("WARNING", msg.rstrip(), True)


	def PrintErrorLog(self, msg):
		self.PrintTestCaseLog("ERROR", msg.rstrip(), True)


	def PrintLog(self, msg="None"):
		self.PrintTestCaseLog("LOG", msg, True)
# this is quote from the shlex module, added in py3.3
_find_unsafe = re.compile(r'[^\w@%+=:,./~-]').search


def _sh_quote(s):
	"""Return a shell-escaped version of the string *s*."""
	if not s:
		return ""
	if _find_unsafe(s) is None:
		return s

	# use single quotes, and put single quotes into double quotes
	# the string $'b is then quoted as '$'"'"'b'
	return "'" + s.replace("'", "'\"'\"'") + "'"


class SCPClient(object):
	"""
	An scp1 implementation, compatible with openssh scp.
	Raises SCPException for all transport related errors. Local filesystem
	and OS errors pass through.

	Main public methods are .put and .get
	The get method is controlled by the remote scp instance, and behaves
	accordingly. This means that symlinks are resolved, and the transfer is
	halted after too many levels of symlinks are detected.
	The put method uses os.walk for recursion, and sends files accordingly.
	Since scp doesn't support symlinks, we send file symlinks as the file
	(matching scp behaviour), but we make no attempt at symlinked directories.
	"""
	def __init__(self, transport, buff_size=16384, socket_timeout=5.0,
				 progress=None, sanitize=_sh_quote):
		"""
		Create an scp1 client.

		@param transport: an existing paramiko L{Transport}
		@type transport: L{Transport}
		@param buff_size: size of the scp send buffer.
		@type buff_size: int
		@param socket_timeout: channel socket timeout in seconds
		@type socket_timeout: float
		@param progress: callback - called with (filename, size, sent) during
			transfers
		@param sanitize: function - called with filename, should return
			safe or escaped string.  Uses _sh_quote by default.
		@type progress: function(string, int, int)
		"""
		self.transport = transport
		self.buff_size = buff_size
		self.socket_timeout = socket_timeout
		self.channel = None
		self.preserve_times = False
		self._progress = progress
		self._recv_dir = ''
		self._rename = False
		self._utime = None
		self.sanitize = sanitize
		self._dirtimes = {}


	def put(self, files, remote_path='.',
			recursive=False, preserve_times=False):
		"""
		Transfer files to remote host.

		@param files: A single path, or a list of paths to be transfered.
			recursive must be True to transfer directories.
		@type files: string OR list of strings
		@param remote_path: path in which to receive the files on the remote
			host. defaults to '.'
		@type remote_path: str
		@param recursive: transfer files and directories recursively
		@type recursive: bool
		@param preserve_times: preserve mtime and atime of transfered files
			and directories.
		@type preserve_times: bool
		"""
		self.preserve_times = preserve_times
		self.channel = self.transport.open_session()
		self.channel.settimeout(self.socket_timeout)
		scp_command = ('scp -t %s', 'scp -r -t %s')[recursive]
		self.channel.exec_command(scp_command % self.sanitize(remote_path))
		self._recv_confirm()

		if not isinstance(files, (list, tuple)):
			files = [files]

		if recursive:
			self._send_recursive(files)
		else:
			self._send_files(files)

		if self.channel:
			self.channel.close()


	def get(self, remote_path, local_path='',
			recursive=False, preserve_times=False):
		"""
		Transfer files from remote host to localhost

		@param remote_path: path to retreive from remote host. since this is
			evaluated by scp on the remote host, shell wildcards and
			environment variables may be used.
		@type remote_path: str
		@param local_path: path in which to receive files locally
		@type local_path: str
		@param recursive: transfer files and directories recursively
		@type recursive: bool
		@param preserve_times: preserve mtime and atime of transfered files
			and directories.
		@type preserve_times: bool
		"""
		if not isinstance(remote_path, (list, tuple)):
			remote_path = [remote_path]
		remote_path = [self.sanitize(r) for r in remote_path]
		self._recv_dir = local_path or os.getcwd()
		self._rename = len(remote_path) == 1 and not os.path.isdir(local_path)
		if len(remote_path) > 1:
			if not os.path.exists(self._recv_dir):
				msg = "Local path '%s' does not exist" % self._recv_dir
				raise SCPException(msg)
			elif not os.path.isdir(self._recv_dir):
				msg = "Local path '%s' is not a directory" % self._recv_dir
				raise SCPException(msg)
		rcsv = ('', ' -r')[recursive]
		prsv = ('', ' -p')[preserve_times]
		self.channel = self.transport.open_session()
		self.channel.settimeout(self.socket_timeout)
		self.channel.exec_command("scp%s%s -f %s" % (rcsv, prsv,
													 ' '.join(remote_path)))
		try:
			self._recv_all()
		except :
			print sys.exc_info()[0]

		if self.channel:
			self.channel.close()


	def _read_stats(self, name):
		"""return just the file stats needed for scp"""
		stats = os.stat(name)
		mode = oct(stats.st_mode)[-4:]
		size = stats.st_size
		atime = int(stats.st_atime)
		mtime = int(stats.st_mtime)
		return (mode, size, mtime, atime)


	def _send_files(self, files):
		for name in files:
			basename = os.path.basename(name)
			(mode, size, mtime, atime) = self._read_stats(name)
			if self.preserve_times:
				self._send_time(mtime, atime)
			file_hdl = open(name, 'rb')

			# The protocol can't handle \n in the filename.
			# Quote them as the control sequence \^J for now,
			# which is how openssh handles it.
			self.channel.sendall("C%s %d %s\n" %
								 (mode, size, basename.replace('\n', '\\^J')))
			self._recv_confirm()
			file_pos = 0
			if self._progress:
				if size == 0:
					# avoid divide-by-zero
					self._progress(basename, 1, 1)
				else:
					self._progress(basename, size, 0)
			buff_size = self.buff_size
			chan = self.channel
			while file_pos < size:
				chan.sendall(file_hdl.read(buff_size))
				file_pos = file_hdl.tell()
				if self._progress:
					self._progress(basename, size, file_pos)
			chan.sendall('\x00')
			file_hdl.close()
			self._recv_confirm()


	def _send_recursive(self, files):
		for base in files:
			if not os.path.isdir(base):
				# filename mixed into the bunch
				self._send_files([base])
				continue
			last_dir = base
			for root, dirs, fls in os.walk(base):
				self._chdir(last_dir, root)
				self._send_files([os.path.join(root, f) for f in fls])
				last_dir = root
			# back out of the directory
			for i in range(len(os.path.split(last_dir))):
				self._send_popd()


	def _send_pushd(self, directory):
		(mode, size, mtime, atime) = self._read_stats(directory)
		basename = os.path.basename(directory)
		if self.preserve_times:
			self._send_time(mtime, atime)
		self.channel.sendall('D%s 0 %s\n' %
							 (mode, basename.replace('\n', '\\^J')))
		self._recv_confirm()


	def _send_popd(self):
		self.channel.sendall('E\n')
		self._recv_confirm()


	def _send_time(self, mtime, atime):
		self.channel.sendall('T%d 0 %d 0\n' % (mtime, atime))
		self._recv_confirm()


	def _recv_confirm(self):
		# read scp response
		msg = ''
		try:
			msg = self.channel.recv(512)
		except SocketTimeout:
			raise SCPException('Timout waiting for scp response')
		# slice off the first byte, so this compare will work in python2 and python3
		if msg and msg[0:1] == b'\x00':
			return
		elif msg and msg[0:1] == b'\x01':
			raise SCPException(msg[1:])
		elif self.channel.recv_stderr_ready():
			msg = self.channel.recv_stderr(512)
			raise SCPException(msg)
		elif not msg:
			raise SCPException('No response from server')
		else:
			raise SCPException('Invalid response from server', msg)


	def _recv_all(self):
		# loop over scp commands, and recive as necessary
		command = {b'C': self._recv_file,
				   b'T': self._set_time,
				   b'D': self._recv_pushd,
				   b'E': self._recv_popd}
		while not self.channel.closed:
			# wait for command as long as we're open
			self.channel.sendall('\x00')
			msg = self.channel.recv(1024)
			if not msg:  # chan closed while recving
				break
			code = msg[0:1]
			try:
				command[code](msg[1:])
			except KeyError:
				raise SCPException(str(msg).strip())
		# directory times can't be set until we're done writing files
		self._set_dirtimes()


	def _set_time(self, cmd):
		try:
			times = cmd.split()
			mtime = int(times[0])
			atime = int(times[2]) or mtime
		except:
			self.channel.send(b'\x01')
			raise SCPException('Bad time format')
		# save for later
		self._utime = (atime, mtime)


	def _recv_file(self, cmd):
		chan = self.channel
		parts = cmd.strip().split(' ', 2)
		try:
			mode = int(parts[0], 8)
			size = int(parts[1])
			path = os.path.join(self._recv_dir, parts[2])
			if self._rename:
				path = self._recv_dir
				self._rename = False
		except:
			chan.send('\x01')
			chan.close()
			raise SCPException('Bad file format')

		try:
			file_hdl = open(path, 'wb')
		except IOError as e:
			chan.send(b'\x01' + str(e).encode())
			chan.close()
			raise

		if self._progress:
			if size == 0:
				# avoid divide-by-zero
				self._progress(path, 1, 1)
			else:
				self._progress(path, size, 0)
		buff_size = self.buff_size
		pos = 0
		chan.send(b'\x00')
		try:
			while pos < size:
				# we have to make sure we don't read the final byte
				if size - pos <= buff_size:
					buff_size = size - pos
				file_hdl.write(chan.recv(buff_size))
				pos = file_hdl.tell()
				if self._progress:
					self._progress(path, size, pos)

			msg = chan.recv(512)
			if msg and msg[0:1] != b'\x00':
				raise SCPException(msg[1:])
		except SocketTimeout:
			chan.close()
			raise SCPException('Error receiving, socket.timeout')

		file_hdl.truncate()
		try:
			os.utime(path, self._utime)
			self._utime = None
			os.chmod(path, mode)
			# should we notify the other end?
		finally:
			file_hdl.close()
		# '\x00' confirmation sent in _recv_all


	def _recv_pushd(self, cmd):
		parts = cmd.split()
		try:
			mode = int(parts[0], 8)
			path = os.path.join(self._recv_dir, parts[2])
			if self._rename:
				path = self._recv_dir
				self._rename = False
		except:
			self.channel.send(b'\x01')
			raise SCPException('Bad directory format')
		try:
			if not os.path.exists(path):
				os.mkdir(path, mode)
			elif os.path.isdir(path):
				os.chmod(path, mode)
			else:
				raise SCPException('%s: Not a directory' % path)
			self._dirtimes[path] = (self._utime)
			self._utime = None
			self._recv_dir = path
		except (OSError, SCPException) as e:
			self.channel.send(b'\x01' + str(e).encode())
			raise


	def _recv_popd(self, *cmd):
		self._recv_dir = os.path.split(self._recv_dir)[0]


	def _set_dirtimes(self):
		try:
			for d in self._dirtimes:
				os.utime(d, self._dirtimes[d])
		finally:
			self._dirtimes = {}



class SCPException(Exception):
	"""SCP exception class"""
	pass



class SSHConnector(object):
	_ssh_settings = None
	_commandBuffer = []

	def __init__(self, ssh_settings):
		self._ssh_settings = ssh_settings


	def _addCommand(self, command):
		self._commandBuffer.append(command)


	def addLunaSend(self, package, api, parameter, options="-n 1"):
		json_param = json.dumps(parameter)
		command = "luna-send {0} palm://{1}/{2} '{3}'".format(options, package, api, json_param)
		self._addCommand(command)


	def addCommandSend(self, command):
		self._addCommand(command)


	def bulkLunaSend(self):
		if(len(self._commandBuffer) <= 0) :
			return
		client = paramiko.SSHClient()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

		try :
			client.connect(hostname=self._ssh_settings['hostname'],
							port=self._ssh_settings['port'],
							username=self._ssh_settings['username'],
							timeout=self._ssh_settings['timeout'])
		except :
			client.connect(hostname=self._ssh_settings['hostname'],
							port=self._ssh_settings['port'],
							username=self._ssh_settings['username'],
							password=self._ssh_settings['password'],
							timeout=self._ssh_settings['timeout'])

		for command in self._commandBuffer :
			time.sleep(0.5)
			print command
			stdin, stdout, stderr = client.exec_command(command)
			result_dict = json.load(stdout)
			for line in stdout:
				print line

		stdin.close()
		stdout.close()
		stderr.close()
		client.close()
		self._commandBuffer = []
		return result_dict


	def bulkSend(self):
		result_list = []

		if(len(self._commandBuffer) <= 0) :
			return
		client = paramiko.SSHClient()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

		try :
			client.connect(hostname=self._ssh_settings['hostname'],
							port=self._ssh_settings['port'],
							username=self._ssh_settings['username'],
							timeout=self._ssh_settings['timeout'])
		except :
			client.connect(hostname=self._ssh_settings['hostname'],
							port=self._ssh_settings['port'],
							username=self._ssh_settings['username'],
							password=self._ssh_settings['password'],
							timeout=self._ssh_settings['timeout'])

		for command in self._commandBuffer :
			time.sleep(0.5)
			print command
			stdin, stdout, stderr = client.exec_command(command)
			for line in stdout:
				result_list.append(line)
				print line

		stdin.close()
		stdout.close()
		stderr.close()
		client.close()
		self._commandBuffer = []
		return result_list



class Util(object):
	'''
	A class includes utility functions.
	'''
	@staticmethod
	def is_empty(sequence):
		if (len(sequence) == 0):
			return True
		else:
			return False


	@staticmethod
	def get_default_value(dictionary, key, default_value):
		if (dictionary and key in dictionary and dictionary[key]):
			return dictionary[key]
		else:
			return default_value



class Config(object):

	def __init__(self):
		config_root = self._read_config_file().getroot()
		self._ssh_settings = self._read_ssh_settings(config_root)


	def _read_config_file(self):
		return et.parse('config.xml')


	def _read_ssh_settings(self, config_root):
		ssh_settings = {}

		hostname = config_root.find('./SSHIp').text
		if (not hostname):
			raise Exception('There is no host name in config.xml file.')

		ssh_settings['hostname'] = hostname
		ssh_settings['port'] = int(config_root.find('./SSHPort').text) or 22
		ssh_settings['username'] = config_root.find('./SSHID').text or 'root'
		ssh_settings['password'] = config_root.find('./SSHPasswd').text or ''
		ssh_settings['workspace'] = config_root.find('./Workspace').text or './'
		ssh_settings['timeout'] = 5000

		return ssh_settings


	def get_ssh_settings(self):
		return self._ssh_settings



if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()

