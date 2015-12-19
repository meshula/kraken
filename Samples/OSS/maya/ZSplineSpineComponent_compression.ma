//Maya ASCII 2016 scene
//Name: ZSplineSpineComponent_compression.ma
//Last modified: Fri, Dec 18, 2015 07:40:04 PM
//Codeset: 1252
requires maya "2016";
requires -nodeType "decomposeMatrix" "matrixNodes" "1.0";
requires -nodeType "ilrOptionsNode" -nodeType "ilrUIOptionsNode" -nodeType "ilrBakeLayerManager"
		 -nodeType "ilrBakeLayer" "Turtle" "2016.0.0";
requires "stereoCamera" "10.0";
requires -nodeType "dfgMayaNode" -dataType "FabricSpliceMayaData" "FabricMaya" "2.0.1";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2016";
fileInfo "version" "2016";
fileInfo "cutIdentifier" "201508242200-969261";
fileInfo "osv" "Microsoft Windows 7 Enterprise Edition, 64-bit Windows 7 Service Pack 1 (Build 7601)\n";
createNode transform -s -n "persp";
	rename -uid "8942B32E-4850-22CF-1407-C5ADC6896DB7";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 11.124526979362802 16.192174315400457 11.763857445574104 ;
	setAttr ".r" -type "double3" -14.738352729606833 43.400000000002414 2.1887321486263971e-015 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "151FDC0E-4F62-590A-ACF7-A39F8E0651C3";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 16.741684752835571;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 0 11.933 0 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "282CE5DE-4E05-5CC5-9F45-E5A9F9CF974C";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 100.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "44141217-4C7F-03E3-4874-3BB340D38F0C";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 18.077483697736881;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "3DE259C4-410E-556A-7242-04964318CCB9";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1.8671213991769533 10.497065843621398 100.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "22335FCB-48F6-E5CD-AACE-7797420D7D2E";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 19.318518518518516;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "1A9A6E7A-405C-E329-60D4-CD92A20599A0";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 100.1 0 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "3CB37D73-4DBC-5A86-5ACF-84A32979F104";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "MyRig";
	rename -uid "AF0E0863-4F5A-F3A2-2A9B-CFB5428DC082";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "MyRig_controls" -p "MyRig";
	rename -uid "ED4F24CF-4D10-BDE9-66B1-AB83ABCB19C6";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "spine_M_cmp" -p "MyRig_controls";
	rename -uid "9D91D209-4E6A-E0E8-CFCC-E1AC82C3A16E";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "M_inputs_hrc" -p "|MyRig|MyRig_controls|spine_M_cmp";
	rename -uid "B9FE3198-4FC7-9469-D0D1-059825C3F2A8";
	addAttr -ci true -k true -sn "inputs" -ln "inputs" -nn "inputs" -min 0 -max 0 -en 
		"-----" -at "enum";
	addAttr -ci true -k true -sn "drawDebug" -ln "drawDebug" -nn "drawDebug" -min 0 
		-max 1 -at "bool";
	addAttr -ci true -k true -sn "rigScale" -ln "rigScale" -nn "rigScale" -dv 1 -at "float";
	addAttr -ci true -k true -sn "numDeformers" -ln "numDeformers" -nn "numDeformers" 
		-dv 6 -min 0 -max 12 -at "long";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -l on -k on ".inputs";
	setAttr -k on ".drawDebug";
	setAttr -k on ".rigScale";
	setAttr -k on ".numDeformers";
createNode transform -n "M_mainSrt_cmpIn" -p "M_inputs_hrc";
	rename -uid "58A1CBB5-402A-2E44-C19F-5EA3431840B8";
createNode locator -n "M_mainSrt_cmpInShape" -p "M_mainSrt_cmpIn";
	rename -uid "420E38E1-4418-5E15-8D82-22BB48F8408B";
	setAttr -k off ".v" no;
createNode transform -n "M_outputs_hrc" -p "|MyRig|MyRig_controls|spine_M_cmp";
	rename -uid "C2C4C7C5-4826-4B8D-926E-F5B50E20C16B";
	addAttr -ci true -k true -sn "outputs" -ln "outputs" -nn "outputs" -min 0 -max 
		0 -en "-----" -at "enum";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -l on -k on ".outputs";
createNode transform -n "M_cog_cmpOut" -p "M_outputs_hrc";
	rename -uid "5EB67645-43B3-28F3-0AFF-F5998158AD47";
createNode locator -n "M_cog_cmpOutShape" -p "M_cog_cmpOut";
	rename -uid "0F448296-430A-2671-8639-30B343E337B6";
	setAttr -k off ".v" no;
createNode parentConstraint -n "cog_To_cog_par_cns" -p "M_cog_cmpOut";
	rename -uid "2562D435-4F0C-B8E5-4D51-66B0495FE951";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "M_cog_ctrlW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".rst" -type "double3" 0 10 0 ;
	setAttr -k on ".w0";
createNode scaleConstraint -n "cog_To_cog_scl_cns" -p "M_cog_cmpOut";
	rename -uid "C47DCB81-4450-DD94-72BA-B7B8EA0D8753";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "M_cog_ctrlW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -k on ".w0";
createNode transform -n "M_spineBase_cmpOut" -p "M_outputs_hrc";
	rename -uid "E70CDB39-47FE-A747-1E0F-038ED3D2ECB0";
createNode locator -n "M_spineBase_cmpOutShape" -p "M_spineBase_cmpOut";
	rename -uid "69281512-4863-1A84-6EAD-B889FCCF288F";
	setAttr -k off ".v" no;
createNode parentConstraint -n "spineBase_To_spineBase_par_cns" -p "M_spineBase_cmpOut";
	rename -uid "19F05B2A-41E5-CFAD-3077-D3BBCB1E64C4";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "M_spine01_cmpOutW0" -dv 1 -min 0 
		-at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".lr" -type "double3" 180 0 90.000006830188369 ;
	setAttr ".rst" -type "double3" 0 9 0 ;
	setAttr ".rsrr" -type "double3" 180 0 90.000006830188369 ;
	setAttr -k on ".w0";
createNode scaleConstraint -n "spineBase_To_spineBase_scl_cns" -p "M_spineBase_cmpOut";
	rename -uid "B8A3644C-4DE6-9FC4-272F-6AAF3A3AEFB9";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "M_spine01_cmpOutW0" -dv 1 -min 0 
		-at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -k on ".w0";
createNode transform -n "M_pelvis_cmpOut" -p "M_outputs_hrc";
	rename -uid "EB56050F-4681-6832-1658-0F9A0D0721F3";
createNode locator -n "M_pelvis_cmpOutShape" -p "M_pelvis_cmpOut";
	rename -uid "DD98747E-4A18-1B30-0194-0C8FB2837758";
	setAttr -k off ".v" no;
createNode parentConstraint -n "pelvis_To_pelvis_par_cns" -p "M_pelvis_cmpOut";
	rename -uid "C80CAB87-4C24-2A9C-D19C-50B694F1CB74";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "M_pelvis_ctrlSpaceW0" -dv 1 -min 
		0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".rst" -type "double3" 0 9 0 ;
	setAttr -k on ".w0";
createNode scaleConstraint -n "pelvis_To_pelvis_scl_cns" -p "M_pelvis_cmpOut";
	rename -uid "C23CA68F-4740-519B-2134-06901A33545B";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "M_pelvis_ctrlSpaceW0" -dv 1 -min 
		0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -k on ".w0";
createNode transform -n "M_spineEnd_cmpOut" -p "M_outputs_hrc";
	rename -uid "11875A9B-4944-7E4F-3DB6-6EAF56B876E6";
createNode locator -n "M_spineEnd_cmpOutShape" -p "M_spineEnd_cmpOut";
	rename -uid "A371BC0A-404A-2432-D4AD-109EA4F076B1";
	setAttr -k off ".v" no;
createNode parentConstraint -n "spineEnd_To_spineEnd_par_cns" -p "M_spineEnd_cmpOut";
	rename -uid "12289BE3-4E85-06E6-46D9-F1BC73E2CF1C";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "M_spine06_cmpOutW0" -dv 1 -min 0 
		-at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".lr" -type "double3" 180 0 90.000006830188369 ;
	setAttr ".rst" -type "double3" 0 15 0 ;
	setAttr ".rsrr" -type "double3" 180 0 90.000006830188369 ;
	setAttr -k on ".w0";
createNode scaleConstraint -n "spineEnd_To_spineEnd_scl_cns" -p "M_spineEnd_cmpOut";
	rename -uid "D0C743EB-40D3-C17E-62BA-3C961C644964";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "M_spine06_cmpOutW0" -dv 1 -min 0 
		-at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -k on ".w0";
createNode transform -n "M_spine01_cmpOut" -p "M_outputs_hrc";
	rename -uid "7B6BBA18-48F2-A37C-08FE-A3AF237A744C";
createNode locator -n "M_spine01_cmpOutShape" -p "M_spine01_cmpOut";
	rename -uid "DEDBBBB6-4C35-F1F8-A844-39B4CE946F73";
	setAttr -k off ".v" no;
createNode transform -n "M_spine02_cmpOut" -p "M_outputs_hrc";
	rename -uid "31CD46C2-47FA-A638-5033-8DAFA9F24835";
createNode locator -n "M_spine02_cmpOutShape" -p "M_spine02_cmpOut";
	rename -uid "F8399638-4E6F-E196-C993-BE94E2B6DBC6";
	setAttr -k off ".v" no;
createNode transform -n "M_spine03_cmpOut" -p "M_outputs_hrc";
	rename -uid "D7D802A1-4D29-9AA7-38F0-0D85557E8E9C";
createNode locator -n "M_spine03_cmpOutShape" -p "M_spine03_cmpOut";
	rename -uid "D853AEDF-421F-A0D6-09F0-E4A2F779FA39";
	setAttr -k off ".v" no;
createNode transform -n "M_spine04_cmpOut" -p "M_outputs_hrc";
	rename -uid "EBE225B2-45F9-5E24-32B1-4D807A0AE1FB";
createNode locator -n "M_spine04_cmpOutShape" -p "M_spine04_cmpOut";
	rename -uid "49DA8A08-49CE-0D53-46C8-A2B7134511A2";
	setAttr -k off ".v" no;
createNode transform -n "M_spine05_cmpOut" -p "M_outputs_hrc";
	rename -uid "BAB147D9-46E8-7BA8-B72A-5498D3086824";
createNode locator -n "M_spine05_cmpOutShape" -p "M_spine05_cmpOut";
	rename -uid "F9BCEBAD-46B6-2469-0698-E4A89401747B";
	setAttr -k off ".v" no;
createNode transform -n "M_spine06_cmpOut" -p "M_outputs_hrc";
	rename -uid "1BB3601A-46CB-0ABD-009A-41AB598C76F5";
createNode locator -n "M_spine06_cmpOutShape" -p "M_spine06_cmpOut";
	rename -uid "2BD2B574-402A-3461-0078-3EBDEC07B3BB";
	setAttr -k off ".v" no;
createNode transform -n "M_cog_ctrlSpace" -p "|MyRig|MyRig_controls|spine_M_cmp";
	rename -uid "FB51D255-4A96-1786-1365-70A02EE61954";
createNode transform -n "M_cog_ctrl" -p "M_cog_ctrlSpace";
	rename -uid "84758882-4369-D3B9-6479-31B389551033";
	setAttr ".ove" yes;
	setAttr ".ovc" 12;
createNode nurbsCurve -n "M_cog_ctrlShape" -p "M_cog_ctrl";
	rename -uid "697F1107-464E-E3A2-9DE9-C9A94C92C73E";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 8 2 no 3
		9 0 1 2 3 4 5 6 7 8
		9
		2.0999999999999996 0 -2.0999999999999996
		3 0 0
		2.0999999999999996 0 2.0999999999999996
		0 0 3
		-2.0999999999999996 0 2.0999999999999996
		-3 0 0
		-2.0999999999999996 0 -2.0999999999999996
		0 0 -3
		2.0999999999999996 0 -2.0999999999999996
		;
createNode transform -n "M_hip_ctrlSpace" -p "M_cog_ctrl";
	rename -uid "2FA13A64-4677-5AF8-5B42-A68D0C476205";
createNode transform -n "M_hip01_ctrl" -p "M_cog_ctrl";
	rename -uid "1C67C0D4-40FF-CDDD-4269-DF95754B9AED";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
createNode nurbsCurve -n "M_hip01_ctrlShape" -p "M_hip01_ctrl";
	rename -uid "E9968373-4CCD-4E12-97CC-D1ABE1D556DD";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 2 no 3
		5 0 1 2 3 4
		5
		-2.25 -2 -1.25
		-2.25 0 -1.25
		2.25 0 -1.25
		2.25 -2 -1.25
		-2.25 -2 -1.25
		;
createNode nurbsCurve -n "M_hip01_ctrlShape1" -p "M_hip01_ctrl";
	rename -uid "39506C38-44D7-0DC2-0C10-D782BF21485C";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 2 no 3
		5 0 1 2 3 4
		5
		-2.25 -2 1.25
		-2.25 0 1.25
		2.25 0 1.25
		2.25 -2 1.25
		-2.25 -2 1.25
		;
createNode nurbsCurve -n "M_hip01_ctrlShape2" -p "M_hip01_ctrl";
	rename -uid "5D866A45-4EC3-D375-D571-3E92562B73C2";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		-2.25 -2 -1.25
		-2.25 -2 1.25
		;
createNode nurbsCurve -n "M_hip01_ctrlShape3" -p "M_hip01_ctrl";
	rename -uid "942F0549-4E13-1936-822D-2EB8568C56D7";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		2.25 -2 -1.25
		2.25 -2 1.25
		;
createNode nurbsCurve -n "M_hip01_ctrlShape4" -p "M_hip01_ctrl";
	rename -uid "F15A07D7-4C3B-1458-72B6-7A988C4DF6BC";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		-2.25 0 -1.25
		-2.25 0 1.25
		;
createNode nurbsCurve -n "M_hip01_ctrlShape5" -p "M_hip01_ctrl";
	rename -uid "107C6391-4CB4-A7CD-A32D-C2A251FBE880";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		2.25 0 -1.25
		2.25 0 1.25
		;
createNode transform -n "M_pelvis_ctrlSpace" -p "M_hip01_ctrl";
	rename -uid "5D343424-4D5B-EF51-843D-1AA5101CEB9E";
	setAttr ".t" -type "double3" 0 -1 0 ;
createNode transform -n "M_torso_ctrlSpace" -p "M_cog_ctrl";
	rename -uid "A10DC968-46E7-4FC3-0436-4C990FC91641";
createNode transform -n "M_torso_ctrl" -p "M_torso_ctrlSpace";
	rename -uid "562D94EF-493A-94F9-60DE-FA8E779333FE";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
createNode nurbsCurve -n "M_torso_ctrlShape" -p "M_torso_ctrl";
	rename -uid "D340B0E0-4C6E-1C9E-FB03-C487A2EFBE27";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 2 no 3
		5 0 1 2 3 4
		5
		2.5 0 -1.5
		2.5 0 1.5
		-2.5 0 1.5
		-2.5 0 -1.5
		2.5 0 -1.5
		;
createNode transform -n "M_chest_ctrlSpace" -p "M_torso_ctrl";
	rename -uid "10BDCD9E-4F8E-F5AA-3930-46B5ABCF2AFE";
	setAttr ".t" -type "double3" 0 2 0 ;
createNode transform -n "M_chest_ctrl" -p "M_chest_ctrlSpace";
	rename -uid "DE49CC93-46D8-17A3-F519-31B61F737F06";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
createNode nurbsCurve -n "M_chest_ctrlShape" -p "M_chest_ctrl";
	rename -uid "5B954CC7-499F-A461-FAAF-D9B294BAA5E0";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 2 no 3
		5 0 1 2 3 4
		5
		2.5 0 -1.5
		2.5 0 1.5
		-2.5 0 1.5
		-2.5 0 -1.5
		2.5 0 -1.5
		;
createNode transform -n "M_upChest_ctrlSpace" -p "M_chest_ctrl";
	rename -uid "7C78983F-4605-0F0F-05A4-16B86CC5F33F";
	setAttr ".t" -type "double3" 0 2 0 ;
createNode transform -n "M_upChest_ctrl" -p "M_upChest_ctrlSpace";
	rename -uid "2C034C53-45D5-1D50-2105-2D8F95C3C88D";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
createNode nurbsCurve -n "M_upChest_ctrlShape" -p "M_upChest_ctrl";
	rename -uid "4274CB9B-4E0D-C875-A145-AA8689FCA6E2";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 2 no 3
		5 0 1 2 3 4
		5
		2.5 0 -1.5
		2.5 0 1.5
		-2.5 0 1.5
		-2.5 0 -1.5
		2.5 0 -1.5
		;
createNode transform -n "M_neck_ctrlSpace" -p "M_upChest_ctrl";
	rename -uid "EC07AD07-4B68-BF47-A573-80BACFFEA6C0";
	setAttr ".t" -type "double3" 0 1 0 ;
createNode parentConstraint -n "cog_To_mainSrt_par_cns" -p "M_cog_ctrlSpace";
	rename -uid "CD6FB99E-4091-9CED-2670-4685B4DAC7B1";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "M_mainSrt_cmpInW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 10 0 ;
	setAttr ".rst" -type "double3" 0 10 0 ;
	setAttr -k on ".w0";
createNode scaleConstraint -n "cog_To_mainSrt_scl_cns" -p "M_cog_ctrlSpace";
	rename -uid "2B53B311-4B5C-23FB-EBD2-32B10816F1FD";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "M_mainSrt_cmpInW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -k on ".w0";
createNode transform -n "MyRig_deformers" -p "MyRig";
	rename -uid "8EDC0F12-4B10-5081-7A80-49B87C860A92";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "spine_M_cmp" -p "MyRig_deformers";
	rename -uid "96C1B01B-42BE-8A87-173C-79BA23DA9C12";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode joint -n "M_spine01_def" -p "|MyRig|MyRig_deformers|spine_M_cmp";
	rename -uid "6EDCB16F-400D-9B74-B81C-28A01A17D8E0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".dla" yes;
	setAttr ".bps" -type "matrix" -1.1920928977282503e-007 1.0000001192092896 0 0 1.0000001192092896 1.192092895507804e-007 1.2246469451366369e-016 0
		 1.2246470911258943e-016 1.4598929226474285e-023 -1.0000002384185791 0 0 9 0 1;
createNode joint -n "M_spine02_def" -p "|MyRig|MyRig_deformers|spine_M_cmp";
	rename -uid "2CFA71C4-4FDD-A9C9-4089-F88F92FF071D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".dla" yes;
	setAttr ".bps" -type "matrix" -1.1920928977282503e-007 1.0000001192092896 0 0 1.0000001192092896 1.192092895507804e-007 1.2246469451366369e-016 0
		 1.2246470911258943e-016 1.4598929226474285e-023 -1.0000002384185791 0 0 10.199999809265137 0 1;
createNode joint -n "M_spine03_def" -p "|MyRig|MyRig_deformers|spine_M_cmp";
	rename -uid "BCB0EA5A-4B57-B8C3-642C-EB8ED9FA685A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".dla" yes;
	setAttr ".bps" -type "matrix" -1.1920928977282503e-007 1.0000001192092896 0 0 1.0000001192092896 1.192092895507804e-007 1.2246469451366369e-016 0
		 1.2246470911258943e-016 1.4598929226474285e-023 -1.0000002384185791 0 0 11.40000057220459 0 1;
createNode joint -n "M_spine04_def" -p "|MyRig|MyRig_deformers|spine_M_cmp";
	rename -uid "4E04BA29-4F4C-5FDB-8494-ADA5469857B9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".dla" yes;
	setAttr ".bps" -type "matrix" -1.1920928977282503e-007 1.0000001192092896 0 0 1.0000001192092896 1.192092895507804e-007 1.2246469451366369e-016 0
		 1.2246470911258943e-016 1.4598929226474285e-023 -1.0000002384185791 0 0 12.600000381469727 0 1;
createNode joint -n "M_spine05_def" -p "|MyRig|MyRig_deformers|spine_M_cmp";
	rename -uid "7FA18320-46D7-81D8-EC8C-37B2095672F4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".dla" yes;
	setAttr ".bps" -type "matrix" -1.1920928977282503e-007 1.0000001192092896 0 0 1.0000001192092896 1.192092895507804e-007 1.2246469451366369e-016 0
		 1.2246470911258943e-016 1.4598929226474285e-023 -1.0000002384185791 0 0 13.800000190734863 0 1;
createNode joint -n "M_spine06_def" -p "|MyRig|MyRig_deformers|spine_M_cmp";
	rename -uid "21387B16-496C-14B3-257D-648D22CDFCCF";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".dla" yes;
	setAttr ".bps" -type "matrix" -1.1920928977282503e-007 1.0000001192092896 0 0 1.0000001192092896 1.192092895507804e-007 1.2246469451366369e-016 0
		 1.2246470911258943e-016 1.4598929226474285e-023 -1.0000002384185791 0 0 15 0 1;
createNode transform -n "transform1";
	rename -uid "6E969E8A-4EE2-B288-D6F2-D4B1E9861C01";
createNode transform -n "pPipe1";
	rename -uid "4CF29B0D-4022-74EC-4250-F4A9C36A8A40";
	setAttr ".t" -type "double3" 0 12.121572174091401 0 ;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode mesh -n "pPipeShape1" -p "pPipe1";
	rename -uid "DDAD40E1-4192-F9EE-05E7-E2B9C2FDDC5B";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".vcs" 2;
createNode mesh -n "pPipeShape1Orig" -p "pPipe1";
	rename -uid "4AE2F6A7-4301-B42A-8C50-3B91486035E4";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 630 ".uvst[0].uvsp";
	setAttr ".uvst[0].uvsp[0:249]" -type "float2" 0 0.50000048 0.050000001 0.50000048
		 0.1 0.50000048 0.15000001 0.50000048 0.2 0.50000048 0.25 0.50000048 0.30000001 0.50000048
		 0.35000002 0.50000048 0.40000004 0.50000048 0.45000005 0.50000048 0.50000006 0.50000048
		 0.55000007 0.50000048 0.60000008 0.50000048 0.6500001 0.50000048 0.70000011 0.50000048
		 0.75000012 0.50000048 0.80000013 0.50000048 0.85000014 0.50000048 0.90000015 0.50000048
		 0.95000017 0.50000048 1.000000119209 0.50000048 0 0.4833338 0.050000001 0.4833338
		 0.1 0.4833338 0.15000001 0.4833338 0.2 0.4833338 0.25 0.4833338 0.30000001 0.4833338
		 0.35000002 0.4833338 0.40000004 0.4833338 0.45000005 0.4833338 0.50000006 0.4833338
		 0.55000007 0.4833338 0.60000008 0.4833338 0.6500001 0.4833338 0.70000011 0.4833338
		 0.75000012 0.4833338 0.80000013 0.4833338 0.85000014 0.4833338 0.90000015 0.4833338
		 0.95000017 0.4833338 1.000000119209 0.4833338 0 0.46666712 0.050000001 0.46666712
		 0.1 0.46666712 0.15000001 0.46666712 0.2 0.46666712 0.25 0.46666712 0.30000001 0.46666712
		 0.35000002 0.46666712 0.40000004 0.46666712 0.45000005 0.46666712 0.50000006 0.46666712
		 0.55000007 0.46666712 0.60000008 0.46666712 0.6500001 0.46666712 0.70000011 0.46666712
		 0.75000012 0.46666712 0.80000013 0.46666712 0.85000014 0.46666712 0.90000015 0.46666712
		 0.95000017 0.46666712 1.000000119209 0.46666712 0 0.45000044 0.050000001 0.45000044
		 0.1 0.45000044 0.15000001 0.45000044 0.2 0.45000044 0.25 0.45000044 0.30000001 0.45000044
		 0.35000002 0.45000044 0.40000004 0.45000044 0.45000005 0.45000044 0.50000006 0.45000044
		 0.55000007 0.45000044 0.60000008 0.45000044 0.6500001 0.45000044 0.70000011 0.45000044
		 0.75000012 0.45000044 0.80000013 0.45000044 0.85000014 0.45000044 0.90000015 0.45000044
		 0.95000017 0.45000044 1.000000119209 0.45000044 0 0.43333375 0.050000001 0.43333375
		 0.1 0.43333375 0.15000001 0.43333375 0.2 0.43333375 0.25 0.43333375 0.30000001 0.43333375
		 0.35000002 0.43333375 0.40000004 0.43333375 0.45000005 0.43333375 0.50000006 0.43333375
		 0.55000007 0.43333375 0.60000008 0.43333375 0.6500001 0.43333375 0.70000011 0.43333375
		 0.75000012 0.43333375 0.80000013 0.43333375 0.85000014 0.43333375 0.90000015 0.43333375
		 0.95000017 0.43333375 1.000000119209 0.43333375 0 0.41666707 0.050000001 0.41666707
		 0.1 0.41666707 0.15000001 0.41666707 0.2 0.41666707 0.25 0.41666707 0.30000001 0.41666707
		 0.35000002 0.41666707 0.40000004 0.41666707 0.45000005 0.41666707 0.50000006 0.41666707
		 0.55000007 0.41666707 0.60000008 0.41666707 0.6500001 0.41666707 0.70000011 0.41666707
		 0.75000012 0.41666707 0.80000013 0.41666707 0.85000014 0.41666707 0.90000015 0.41666707
		 0.95000017 0.41666707 1.000000119209 0.41666707 0 0.40000039 0.050000001 0.40000039
		 0.1 0.40000039 0.15000001 0.40000039 0.2 0.40000039 0.25 0.40000039 0.30000001 0.40000039
		 0.35000002 0.40000039 0.40000004 0.40000039 0.45000005 0.40000039 0.50000006 0.40000039
		 0.55000007 0.40000039 0.60000008 0.40000039 0.6500001 0.40000039 0.70000011 0.40000039
		 0.75000012 0.40000039 0.80000013 0.40000039 0.85000014 0.40000039 0.90000015 0.40000039
		 0.95000017 0.40000039 1.000000119209 0.40000039 0 0.38333371 0.050000001 0.38333371
		 0.1 0.38333371 0.15000001 0.38333371 0.2 0.38333371 0.25 0.38333371 0.30000001 0.38333371
		 0.35000002 0.38333371 0.40000004 0.38333371 0.45000005 0.38333371 0.50000006 0.38333371
		 0.55000007 0.38333371 0.60000008 0.38333371 0.6500001 0.38333371 0.70000011 0.38333371
		 0.75000012 0.38333371 0.80000013 0.38333371 0.85000014 0.38333371 0.90000015 0.38333371
		 0.95000017 0.38333371 1.000000119209 0.38333371 0 0.36666703 0.050000001 0.36666703
		 0.1 0.36666703 0.15000001 0.36666703 0.2 0.36666703 0.25 0.36666703 0.30000001 0.36666703
		 0.35000002 0.36666703 0.40000004 0.36666703 0.45000005 0.36666703 0.50000006 0.36666703
		 0.55000007 0.36666703 0.60000008 0.36666703 0.6500001 0.36666703 0.70000011 0.36666703
		 0.75000012 0.36666703 0.80000013 0.36666703 0.85000014 0.36666703 0.90000015 0.36666703
		 0.95000017 0.36666703 1.000000119209 0.36666703 0 0.35000035 0.050000001 0.35000035
		 0.1 0.35000035 0.15000001 0.35000035 0.2 0.35000035 0.25 0.35000035 0.30000001 0.35000035
		 0.35000002 0.35000035 0.40000004 0.35000035 0.45000005 0.35000035 0.50000006 0.35000035
		 0.55000007 0.35000035 0.60000008 0.35000035 0.6500001 0.35000035 0.70000011 0.35000035
		 0.75000012 0.35000035 0.80000013 0.35000035 0.85000014 0.35000035 0.90000015 0.35000035
		 0.95000017 0.35000035 1.000000119209 0.35000035 0 0.33333367 0.050000001 0.33333367
		 0.1 0.33333367 0.15000001 0.33333367 0.2 0.33333367 0.25 0.33333367 0.30000001 0.33333367
		 0.35000002 0.33333367 0.40000004 0.33333367 0.45000005 0.33333367 0.50000006 0.33333367
		 0.55000007 0.33333367 0.60000008 0.33333367 0.6500001 0.33333367 0.70000011 0.33333367
		 0.75000012 0.33333367 0.80000013 0.33333367 0.85000014 0.33333367 0.90000015 0.33333367
		 0.95000017 0.33333367 1.000000119209 0.33333367 0 0.31666699 0.050000001 0.31666699
		 0.1 0.31666699 0.15000001 0.31666699 0.2 0.31666699 0.25 0.31666699 0.30000001 0.31666699
		 0.35000002 0.31666699 0.40000004 0.31666699 0.45000005 0.31666699 0.50000006 0.31666699
		 0.55000007 0.31666699 0.60000008 0.31666699 0.6500001 0.31666699 0.70000011 0.31666699
		 0.75000012 0.31666699 0.80000013 0.31666699 0.85000014 0.31666699 0.90000015 0.31666699;
	setAttr ".uvst[0].uvsp[250:499]" 0.95000017 0.31666699 1.000000119209 0.31666699
		 0 0.30000031 0.050000001 0.30000031 0.1 0.30000031 0.15000001 0.30000031 0.2 0.30000031
		 0.25 0.30000031 0.30000001 0.30000031 0.35000002 0.30000031 0.40000004 0.30000031
		 0.45000005 0.30000031 0.50000006 0.30000031 0.55000007 0.30000031 0.60000008 0.30000031
		 0.6500001 0.30000031 0.70000011 0.30000031 0.75000012 0.30000031 0.80000013 0.30000031
		 0.85000014 0.30000031 0.90000015 0.30000031 0.95000017 0.30000031 1.000000119209
		 0.30000031 0 0.28333363 0.050000001 0.28333363 0.1 0.28333363 0.15000001 0.28333363
		 0.2 0.28333363 0.25 0.28333363 0.30000001 0.28333363 0.35000002 0.28333363 0.40000004
		 0.28333363 0.45000005 0.28333363 0.50000006 0.28333363 0.55000007 0.28333363 0.60000008
		 0.28333363 0.6500001 0.28333363 0.70000011 0.28333363 0.75000012 0.28333363 0.80000013
		 0.28333363 0.85000014 0.28333363 0.90000015 0.28333363 0.95000017 0.28333363 1.000000119209
		 0.28333363 0 0.26666695 0.050000001 0.26666695 0.1 0.26666695 0.15000001 0.26666695
		 0.2 0.26666695 0.25 0.26666695 0.30000001 0.26666695 0.35000002 0.26666695 0.40000004
		 0.26666695 0.45000005 0.26666695 0.50000006 0.26666695 0.55000007 0.26666695 0.60000008
		 0.26666695 0.6500001 0.26666695 0.70000011 0.26666695 0.75000012 0.26666695 0.80000013
		 0.26666695 0.85000014 0.26666695 0.90000015 0.26666695 0.95000017 0.26666695 1.000000119209
		 0.26666695 0 0.25000027 0.050000001 0.25000027 0.1 0.25000027 0.15000001 0.25000027
		 0.2 0.25000027 0.25 0.25000027 0.30000001 0.25000027 0.35000002 0.25000027 0.40000004
		 0.25000027 0.45000005 0.25000027 0.50000006 0.25000027 0.55000007 0.25000027 0.60000008
		 0.25000027 0.6500001 0.25000027 0.70000011 0.25000027 0.75000012 0.25000027 0.80000013
		 0.25000027 0.85000014 0.25000027 0.90000015 0.25000027 0.95000017 0.25000027 1.000000119209
		 0.25000027 0 0.2333336 0.050000001 0.2333336 0.1 0.2333336 0.15000001 0.2333336 0.2
		 0.2333336 0.25 0.2333336 0.30000001 0.2333336 0.35000002 0.2333336 0.40000004 0.2333336
		 0.45000005 0.2333336 0.50000006 0.2333336 0.55000007 0.2333336 0.60000008 0.2333336
		 0.6500001 0.2333336 0.70000011 0.2333336 0.75000012 0.2333336 0.80000013 0.2333336
		 0.85000014 0.2333336 0.90000015 0.2333336 0.95000017 0.2333336 1.000000119209 0.2333336
		 0 0.21666694 0.050000001 0.21666694 0.1 0.21666694 0.15000001 0.21666694 0.2 0.21666694
		 0.25 0.21666694 0.30000001 0.21666694 0.35000002 0.21666694 0.40000004 0.21666694
		 0.45000005 0.21666694 0.50000006 0.21666694 0.55000007 0.21666694 0.60000008 0.21666694
		 0.6500001 0.21666694 0.70000011 0.21666694 0.75000012 0.21666694 0.80000013 0.21666694
		 0.85000014 0.21666694 0.90000015 0.21666694 0.95000017 0.21666694 1.000000119209
		 0.21666694 0 0.20000027 0.050000001 0.20000027 0.1 0.20000027 0.15000001 0.20000027
		 0.2 0.20000027 0.25 0.20000027 0.30000001 0.20000027 0.35000002 0.20000027 0.40000004
		 0.20000027 0.45000005 0.20000027 0.50000006 0.20000027 0.55000007 0.20000027 0.60000008
		 0.20000027 0.6500001 0.20000027 0.70000011 0.20000027 0.75000012 0.20000027 0.80000013
		 0.20000027 0.85000014 0.20000027 0.90000015 0.20000027 0.95000017 0.20000027 1.000000119209
		 0.20000027 0 0.18333361 0.050000001 0.18333361 0.1 0.18333361 0.15000001 0.18333361
		 0.2 0.18333361 0.25 0.18333361 0.30000001 0.18333361 0.35000002 0.18333361 0.40000004
		 0.18333361 0.45000005 0.18333361 0.50000006 0.18333361 0.55000007 0.18333361 0.60000008
		 0.18333361 0.6500001 0.18333361 0.70000011 0.18333361 0.75000012 0.18333361 0.80000013
		 0.18333361 0.85000014 0.18333361 0.90000015 0.18333361 0.95000017 0.18333361 1.000000119209
		 0.18333361 0 0.16666694 0.050000001 0.16666694 0.1 0.16666694 0.15000001 0.16666694
		 0.2 0.16666694 0.25 0.16666694 0.30000001 0.16666694 0.35000002 0.16666694 0.40000004
		 0.16666694 0.45000005 0.16666694 0.50000006 0.16666694 0.55000007 0.16666694 0.60000008
		 0.16666694 0.6500001 0.16666694 0.70000011 0.16666694 0.75000012 0.16666694 0.80000013
		 0.16666694 0.85000014 0.16666694 0.90000015 0.16666694 0.95000017 0.16666694 1.000000119209
		 0.16666694 0 0.15000027 0.050000001 0.15000027 0.1 0.15000027 0.15000001 0.15000027
		 0.2 0.15000027 0.25 0.15000027 0.30000001 0.15000027 0.35000002 0.15000027 0.40000004
		 0.15000027 0.45000005 0.15000027 0.50000006 0.15000027 0.55000007 0.15000027 0.60000008
		 0.15000027 0.6500001 0.15000027 0.70000011 0.15000027 0.75000012 0.15000027 0.80000013
		 0.15000027 0.85000014 0.15000027 0.90000015 0.15000027 0.95000017 0.15000027 1.000000119209
		 0.15000027 0 0.13333361 0.050000001 0.13333361 0.1 0.13333361 0.15000001 0.13333361
		 0.2 0.13333361 0.25 0.13333361 0.30000001 0.13333361 0.35000002 0.13333361 0.40000004
		 0.13333361 0.45000005 0.13333361 0.50000006 0.13333361 0.55000007 0.13333361 0.60000008
		 0.13333361 0.6500001 0.13333361 0.70000011 0.13333361 0.75000012 0.13333361 0.80000013
		 0.13333361 0.85000014 0.13333361 0.90000015 0.13333361 0.95000017 0.13333361 1.000000119209
		 0.13333361 0 0.11666694 0.050000001 0.11666694 0.1 0.11666694 0.15000001 0.11666694
		 0.2 0.11666694 0.25 0.11666694 0.30000001 0.11666694 0.35000002 0.11666694 0.40000004
		 0.11666694 0.45000005 0.11666694 0.50000006 0.11666694 0.55000007 0.11666694 0.60000008
		 0.11666694 0.6500001 0.11666694 0.70000011 0.11666694 0.75000012 0.11666694 0.80000013
		 0.11666694;
	setAttr ".uvst[0].uvsp[500:629]" 0.85000014 0.11666694 0.90000015 0.11666694
		 0.95000017 0.11666694 1.000000119209 0.11666694 0 0.10000028 0.050000001 0.10000028
		 0.1 0.10000028 0.15000001 0.10000028 0.2 0.10000028 0.25 0.10000028 0.30000001 0.10000028
		 0.35000002 0.10000028 0.40000004 0.10000028 0.45000005 0.10000028 0.50000006 0.10000028
		 0.55000007 0.10000028 0.60000008 0.10000028 0.6500001 0.10000028 0.70000011 0.10000028
		 0.75000012 0.10000028 0.80000013 0.10000028 0.85000014 0.10000028 0.90000015 0.10000028
		 0.95000017 0.10000028 1.000000119209 0.10000028 0 0.083333611 0.050000001 0.083333611
		 0.1 0.083333611 0.15000001 0.083333611 0.2 0.083333611 0.25 0.083333611 0.30000001
		 0.083333611 0.35000002 0.083333611 0.40000004 0.083333611 0.45000005 0.083333611
		 0.50000006 0.083333611 0.55000007 0.083333611 0.60000008 0.083333611 0.6500001 0.083333611
		 0.70000011 0.083333611 0.75000012 0.083333611 0.80000013 0.083333611 0.85000014 0.083333611
		 0.90000015 0.083333611 0.95000017 0.083333611 1.000000119209 0.083333611 0 0.066666946
		 0.050000001 0.066666946 0.1 0.066666946 0.15000001 0.066666946 0.2 0.066666946 0.25
		 0.066666946 0.30000001 0.066666946 0.35000002 0.066666946 0.40000004 0.066666946
		 0.45000005 0.066666946 0.50000006 0.066666946 0.55000007 0.066666946 0.60000008 0.066666946
		 0.6500001 0.066666946 0.70000011 0.066666946 0.75000012 0.066666946 0.80000013 0.066666946
		 0.85000014 0.066666946 0.90000015 0.066666946 0.95000017 0.066666946 1.000000119209
		 0.066666946 0 0.05000028 0.050000001 0.05000028 0.1 0.05000028 0.15000001 0.05000028
		 0.2 0.05000028 0.25 0.05000028 0.30000001 0.05000028 0.35000002 0.05000028 0.40000004
		 0.05000028 0.45000005 0.05000028 0.50000006 0.05000028 0.55000007 0.05000028 0.60000008
		 0.05000028 0.6500001 0.05000028 0.70000011 0.05000028 0.75000012 0.05000028 0.80000013
		 0.05000028 0.85000014 0.05000028 0.90000015 0.05000028 0.95000017 0.05000028 1.000000119209
		 0.05000028 0 0.033333614 0.050000001 0.033333614 0.1 0.033333614 0.15000001 0.033333614
		 0.2 0.033333614 0.25 0.033333614 0.30000001 0.033333614 0.35000002 0.033333614 0.40000004
		 0.033333614 0.45000005 0.033333614 0.50000006 0.033333614 0.55000007 0.033333614
		 0.60000008 0.033333614 0.6500001 0.033333614 0.70000011 0.033333614 0.75000012 0.033333614
		 0.80000013 0.033333614 0.85000014 0.033333614 0.90000015 0.033333614 0.95000017 0.033333614
		 1.000000119209 0.033333614 0 0.016666947 0.050000001 0.016666947 0.1 0.016666947
		 0.15000001 0.016666947 0.2 0.016666947 0.25 0.016666947 0.30000001 0.016666947 0.35000002
		 0.016666947 0.40000004 0.016666947 0.45000005 0.016666947 0.50000006 0.016666947
		 0.55000007 0.016666947 0.60000008 0.016666947 0.6500001 0.016666947 0.70000011 0.016666947
		 0.75000012 0.016666947 0.80000013 0.016666947 0.85000014 0.016666947 0.90000015 0.016666947
		 0.95000017 0.016666947 1.000000119209 0.016666947;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 600 ".vt";
	setAttr ".vt[0:165]"  1 3.2750001 7.271961e-016 0.95105654 3.2750001 -0.309017
		 0.809017 3.2750001 -0.5877853 0.58778524 3.2750001 -0.80901706 0.30901697 3.2750001 -0.9510566
		 -2.9802322e-008 3.2750001 -1.000000119209 -0.30901706 3.2750001 -0.95105666 -0.58778536 3.2750001 -0.80901712
		 -0.80901718 3.2750001 -0.58778536 -0.95105678 3.2750001 -0.30901706 -1.000000238419 3.2750001 7.271961e-016
		 -0.95105678 3.2750001 0.30901706 -0.80901724 3.2750001 0.58778542 -0.58778548 3.2750001 0.8090173
		 -0.30901715 3.2750001 0.95105696 0 3.2750001 1.000000476837 0.30901715 3.2750001 0.95105702
		 0.5877856 3.2750001 0.80901748 0.80901754 3.2750001 0.5877856 0.95105714 3.2750001 0.30901718
		 1 3.049138069 6.7704466e-016 0.95105654 3.049138069 -0.309017 0.809017 3.049138069 -0.5877853
		 0.58778524 3.049138069 -0.80901706 0.30901697 3.049138069 -0.9510566 -2.9802322e-008 3.049138069 -1.000000119209
		 -0.30901706 3.049138069 -0.95105666 -0.58778536 3.049138069 -0.80901712 -0.80901718 3.049138069 -0.58778536
		 -0.95105678 3.049138069 -0.30901706 -1.000000238419 3.049138069 6.7704466e-016 -0.95105678 3.049138069 0.30901706
		 -0.80901724 3.049138069 0.58778542 -0.58778548 3.049138069 0.8090173 -0.30901715 3.049138069 0.95105696
		 0 3.049138069 1.000000476837 0.30901715 3.049138069 0.95105702 0.5877856 3.049138069 0.80901748
		 0.80901754 3.049138069 0.5877856 0.95105714 3.049138069 0.30901718 1 2.8232758 6.2689316e-016
		 0.95105654 2.8232758 -0.309017 0.809017 2.8232758 -0.5877853 0.58778524 2.8232758 -0.80901706
		 0.30901697 2.8232758 -0.9510566 -2.9802322e-008 2.8232758 -1.000000119209 -0.30901706 2.8232758 -0.95105666
		 -0.58778536 2.8232758 -0.80901712 -0.80901718 2.8232758 -0.58778536 -0.95105678 2.8232758 -0.30901706
		 -1.000000238419 2.8232758 6.2689316e-016 -0.95105678 2.8232758 0.30901706 -0.80901724 2.8232758 0.58778542
		 -0.58778548 2.8232758 0.8090173 -0.30901715 2.8232758 0.95105696 0 2.8232758 1.000000476837
		 0.30901715 2.8232758 0.95105702 0.5877856 2.8232758 0.80901748 0.80901754 2.8232758 0.5877856
		 0.95105714 2.8232758 0.30901718 1 2.59741378 5.7674172e-016 0.95105654 2.59741378 -0.309017
		 0.809017 2.59741378 -0.5877853 0.58778524 2.59741378 -0.80901706 0.30901697 2.59741378 -0.9510566
		 -2.9802322e-008 2.59741378 -1.000000119209 -0.30901706 2.59741378 -0.95105666 -0.58778536 2.59741378 -0.80901712
		 -0.80901718 2.59741378 -0.58778536 -0.95105678 2.59741378 -0.30901706 -1.000000238419 2.59741378 5.7674172e-016
		 -0.95105678 2.59741378 0.30901706 -0.80901724 2.59741378 0.58778542 -0.58778548 2.59741378 0.8090173
		 -0.30901715 2.59741378 0.95105696 0 2.59741378 1.000000476837 0.30901715 2.59741378 0.95105702
		 0.5877856 2.59741378 0.80901748 0.80901754 2.59741378 0.5877856 0.95105714 2.59741378 0.30901718
		 1 2.37155175 5.2659027e-016 0.95105654 2.37155175 -0.309017 0.809017 2.37155175 -0.5877853
		 0.58778524 2.37155175 -0.80901706 0.30901697 2.37155175 -0.9510566 -2.9802322e-008 2.37155175 -1.000000119209
		 -0.30901706 2.37155175 -0.95105666 -0.58778536 2.37155175 -0.80901712 -0.80901718 2.37155175 -0.58778536
		 -0.95105678 2.37155175 -0.30901706 -1.000000238419 2.37155175 5.2659027e-016 -0.95105678 2.37155175 0.30901706
		 -0.80901724 2.37155175 0.58778542 -0.58778548 2.37155175 0.8090173 -0.30901715 2.37155175 0.95105696
		 0 2.37155175 1.000000476837 0.30901715 2.37155175 0.95105702 0.5877856 2.37155175 0.80901748
		 0.80901754 2.37155175 0.5877856 0.95105714 2.37155175 0.30901718 1 2.14568973 4.7643883e-016
		 0.95105654 2.14568973 -0.309017 0.809017 2.14568973 -0.5877853 0.58778524 2.14568973 -0.80901706
		 0.30901697 2.14568973 -0.9510566 -2.9802322e-008 2.14568973 -1.000000119209 -0.30901706 2.14568973 -0.95105666
		 -0.58778536 2.14568973 -0.80901712 -0.80901718 2.14568973 -0.58778536 -0.95105678 2.14568973 -0.30901706
		 -1.000000238419 2.14568973 4.7643883e-016 -0.95105678 2.14568973 0.30901706 -0.80901724 2.14568973 0.58778542
		 -0.58778548 2.14568973 0.8090173 -0.30901715 2.14568973 0.95105696 0 2.14568973 1.000000476837
		 0.30901715 2.14568973 0.95105702 0.5877856 2.14568973 0.80901748 0.80901754 2.14568973 0.5877856
		 0.95105714 2.14568973 0.30901718 1 1.9198277 4.2628738e-016 0.95105654 1.9198277 -0.309017
		 0.809017 1.9198277 -0.5877853 0.58778524 1.9198277 -0.80901706 0.30901697 1.9198277 -0.9510566
		 -2.9802322e-008 1.9198277 -1.000000119209 -0.30901706 1.9198277 -0.95105666 -0.58778536 1.9198277 -0.80901712
		 -0.80901718 1.9198277 -0.58778536 -0.95105678 1.9198277 -0.30901706 -1.000000238419 1.9198277 4.2628738e-016
		 -0.95105678 1.9198277 0.30901706 -0.80901724 1.9198277 0.58778542 -0.58778548 1.9198277 0.8090173
		 -0.30901715 1.9198277 0.95105696 0 1.9198277 1.000000476837 0.30901715 1.9198277 0.95105702
		 0.5877856 1.9198277 0.80901748 0.80901754 1.9198277 0.5877856 0.95105714 1.9198277 0.30901718
		 1 1.69396555 3.7613591e-016 0.95105654 1.69396555 -0.309017 0.809017 1.69396555 -0.5877853
		 0.58778524 1.69396555 -0.80901706 0.30901697 1.69396555 -0.9510566 -2.9802322e-008 1.69396555 -1.000000119209
		 -0.30901706 1.69396555 -0.95105666 -0.58778536 1.69396555 -0.80901712 -0.80901718 1.69396555 -0.58778536
		 -0.95105678 1.69396555 -0.30901706 -1.000000238419 1.69396555 3.7613591e-016 -0.95105678 1.69396555 0.30901706
		 -0.80901724 1.69396555 0.58778542 -0.58778548 1.69396555 0.8090173 -0.30901715 1.69396555 0.95105696
		 0 1.69396555 1.000000476837 0.30901715 1.69396555 0.95105702 0.5877856 1.69396555 0.80901748
		 0.80901754 1.69396555 0.5877856 0.95105714 1.69396555 0.30901718 1 1.46810353 3.2598447e-016
		 0.95105654 1.46810353 -0.309017 0.809017 1.46810353 -0.5877853 0.58778524 1.46810353 -0.80901706
		 0.30901697 1.46810353 -0.9510566 -2.9802322e-008 1.46810353 -1.000000119209;
	setAttr ".vt[166:331]" -0.30901706 1.46810353 -0.95105666 -0.58778536 1.46810353 -0.80901712
		 -0.80901718 1.46810353 -0.58778536 -0.95105678 1.46810353 -0.30901706 -1.000000238419 1.46810353 3.2598447e-016
		 -0.95105678 1.46810353 0.30901706 -0.80901724 1.46810353 0.58778542 -0.58778548 1.46810353 0.8090173
		 -0.30901715 1.46810353 0.95105696 0 1.46810353 1.000000476837 0.30901715 1.46810353 0.95105702
		 0.5877856 1.46810353 0.80901748 0.80901754 1.46810353 0.5877856 0.95105714 1.46810353 0.30901718
		 1 1.2422415 2.7583302e-016 0.95105654 1.2422415 -0.309017 0.809017 1.2422415 -0.5877853
		 0.58778524 1.2422415 -0.80901706 0.30901697 1.2422415 -0.9510566 -2.9802322e-008 1.2422415 -1.000000119209
		 -0.30901706 1.2422415 -0.95105666 -0.58778536 1.2422415 -0.80901712 -0.80901718 1.2422415 -0.58778536
		 -0.95105678 1.2422415 -0.30901706 -1.000000238419 1.2422415 2.7583302e-016 -0.95105678 1.2422415 0.30901706
		 -0.80901724 1.2422415 0.58778542 -0.58778548 1.2422415 0.8090173 -0.30901715 1.2422415 0.95105696
		 0 1.2422415 1.000000476837 0.30901715 1.2422415 0.95105702 0.5877856 1.2422415 0.80901748
		 0.80901754 1.2422415 0.5877856 0.95105714 1.2422415 0.30901718 1 1.016379356 2.2568155e-016
		 0.95105654 1.016379356 -0.309017 0.809017 1.016379356 -0.5877853 0.58778524 1.016379356 -0.80901706
		 0.30901697 1.016379356 -0.9510566 -2.9802322e-008 1.016379356 -1.000000119209 -0.30901706 1.016379356 -0.95105666
		 -0.58778536 1.016379356 -0.80901712 -0.80901718 1.016379356 -0.58778536 -0.95105678 1.016379356 -0.30901706
		 -1.000000238419 1.016379356 2.2568155e-016 -0.95105678 1.016379356 0.30901706 -0.80901724 1.016379356 0.58778542
		 -0.58778548 1.016379356 0.8090173 -0.30901715 1.016379356 0.95105696 0 1.016379356 1.000000476837
		 0.30901715 1.016379356 0.95105702 0.5877856 1.016379356 0.80901748 0.80901754 1.016379356 0.5877856
		 0.95105714 1.016379356 0.30901718 1 0.79051727 1.755301e-016 0.95105654 0.79051727 -0.309017
		 0.809017 0.79051727 -0.5877853 0.58778524 0.79051727 -0.80901706 0.30901697 0.79051727 -0.9510566
		 -2.9802322e-008 0.79051727 -1.000000119209 -0.30901706 0.79051727 -0.95105666 -0.58778536 0.79051727 -0.80901712
		 -0.80901718 0.79051727 -0.58778536 -0.95105678 0.79051727 -0.30901706 -1.000000238419 0.79051727 1.755301e-016
		 -0.95105678 0.79051727 0.30901706 -0.80901724 0.79051727 0.58778542 -0.58778548 0.79051727 0.8090173
		 -0.30901715 0.79051727 0.95105696 0 0.79051727 1.000000476837 0.30901715 0.79051727 0.95105702
		 0.5877856 0.79051727 0.80901748 0.80901754 0.79051727 0.5877856 0.95105714 0.79051727 0.30901718
		 1 0.5646553 1.2537866e-016 0.95105654 0.5646553 -0.309017 0.809017 0.5646553 -0.5877853
		 0.58778524 0.5646553 -0.80901706 0.30901697 0.5646553 -0.9510566 -2.9802322e-008 0.5646553 -1.000000119209
		 -0.30901706 0.5646553 -0.95105666 -0.58778536 0.5646553 -0.80901712 -0.80901718 0.5646553 -0.58778536
		 -0.95105678 0.5646553 -0.30901706 -1.000000238419 0.5646553 1.2537866e-016 -0.95105678 0.5646553 0.30901706
		 -0.80901724 0.5646553 0.58778542 -0.58778548 0.5646553 0.8090173 -0.30901715 0.5646553 0.95105696
		 0 0.5646553 1.000000476837 0.30901715 0.5646553 0.95105702 0.5877856 0.5646553 0.80901748
		 0.80901754 0.5646553 0.5877856 0.95105714 0.5646553 0.30901718 1 0.3387931 7.522718e-017
		 0.95105654 0.3387931 -0.309017 0.809017 0.3387931 -0.5877853 0.58778524 0.3387931 -0.80901706
		 0.30901697 0.3387931 -0.9510566 -2.9802322e-008 0.3387931 -1.000000119209 -0.30901706 0.3387931 -0.95105666
		 -0.58778536 0.3387931 -0.80901712 -0.80901718 0.3387931 -0.58778536 -0.95105678 0.3387931 -0.30901706
		 -1.000000238419 0.3387931 7.522718e-017 -0.95105678 0.3387931 0.30901706 -0.80901724 0.3387931 0.58778542
		 -0.58778548 0.3387931 0.8090173 -0.30901715 0.3387931 0.95105696 0 0.3387931 1.000000476837
		 0.30901715 0.3387931 0.95105702 0.5877856 0.3387931 0.80901748 0.80901754 0.3387931 0.5877856
		 0.95105714 0.3387931 0.30901718 1 0.1129311 2.507574e-017 0.95105654 0.1129311 -0.309017
		 0.809017 0.1129311 -0.5877853 0.58778524 0.1129311 -0.80901706 0.30901697 0.1129311 -0.9510566
		 -2.9802322e-008 0.1129311 -1.000000119209 -0.30901706 0.1129311 -0.95105666 -0.58778536 0.1129311 -0.80901712
		 -0.80901718 0.1129311 -0.58778536 -0.95105678 0.1129311 -0.30901706 -1.000000238419 0.1129311 2.507574e-017
		 -0.95105678 0.1129311 0.30901706 -0.80901724 0.1129311 0.58778542 -0.58778548 0.1129311 0.8090173
		 -0.30901715 0.1129311 0.95105696 0 0.1129311 1.000000476837 0.30901715 0.1129311 0.95105702
		 0.5877856 0.1129311 0.80901748 0.80901754 0.1129311 0.5877856 0.95105714 0.1129311 0.30901718
		 1 -0.1129309 -2.5075697e-017 0.95105654 -0.1129309 -0.309017 0.809017 -0.1129309 -0.5877853
		 0.58778524 -0.1129309 -0.80901706 0.30901697 -0.1129309 -0.9510566 -2.9802322e-008 -0.1129309 -1.000000119209
		 -0.30901706 -0.1129309 -0.95105666 -0.58778536 -0.1129309 -0.80901712 -0.80901718 -0.1129309 -0.58778536
		 -0.95105678 -0.1129309 -0.30901706 -1.000000238419 -0.1129309 -2.5075697e-017 -0.95105678 -0.1129309 0.30901706
		 -0.80901724 -0.1129309 0.58778542 -0.58778548 -0.1129309 0.8090173 -0.30901715 -0.1129309 0.95105696
		 0 -0.1129309 1.000000476837 0.30901715 -0.1129309 0.95105702 0.5877856 -0.1129309 0.80901748
		 0.80901754 -0.1129309 0.5877856 0.95105714 -0.1129309 0.30901718 1 -0.3387931 -7.522718e-017
		 0.95105654 -0.3387931 -0.309017 0.809017 -0.3387931 -0.5877853 0.58778524 -0.3387931 -0.80901706
		 0.30901697 -0.3387931 -0.9510566 -2.9802322e-008 -0.3387931 -1.000000119209 -0.30901706 -0.3387931 -0.95105666
		 -0.58778536 -0.3387931 -0.80901712 -0.80901718 -0.3387931 -0.58778536 -0.95105678 -0.3387931 -0.30901706
		 -1.000000238419 -0.3387931 -7.522718e-017 -0.95105678 -0.3387931 0.30901706;
	setAttr ".vt[332:497]" -0.80901724 -0.3387931 0.58778542 -0.58778548 -0.3387931 0.8090173
		 -0.30901715 -0.3387931 0.95105696 0 -0.3387931 1.000000476837 0.30901715 -0.3387931 0.95105702
		 0.5877856 -0.3387931 0.80901748 0.80901754 -0.3387931 0.5877856 0.95105714 -0.3387931 0.30901718
		 1 -0.5646553 -1.2537866e-016 0.95105654 -0.5646553 -0.309017 0.809017 -0.5646553 -0.5877853
		 0.58778524 -0.5646553 -0.80901706 0.30901697 -0.5646553 -0.9510566 -2.9802322e-008 -0.5646553 -1.000000119209
		 -0.30901706 -0.5646553 -0.95105666 -0.58778536 -0.5646553 -0.80901712 -0.80901718 -0.5646553 -0.58778536
		 -0.95105678 -0.5646553 -0.30901706 -1.000000238419 -0.5646553 -1.2537866e-016 -0.95105678 -0.5646553 0.30901706
		 -0.80901724 -0.5646553 0.58778542 -0.58778548 -0.5646553 0.8090173 -0.30901715 -0.5646553 0.95105696
		 0 -0.5646553 1.000000476837 0.30901715 -0.5646553 0.95105702 0.5877856 -0.5646553 0.80901748
		 0.80901754 -0.5646553 0.5877856 0.95105714 -0.5646553 0.30901718 1 -0.79051709 -1.7553006e-016
		 0.95105654 -0.79051709 -0.309017 0.809017 -0.79051709 -0.5877853 0.58778524 -0.79051709 -0.80901706
		 0.30901697 -0.79051709 -0.9510566 -2.9802322e-008 -0.79051709 -1.000000119209 -0.30901706 -0.79051709 -0.95105666
		 -0.58778536 -0.79051709 -0.80901712 -0.80901718 -0.79051709 -0.58778536 -0.95105678 -0.79051709 -0.30901706
		 -1.000000238419 -0.79051709 -1.7553006e-016 -0.95105678 -0.79051709 0.30901706 -0.80901724 -0.79051709 0.58778542
		 -0.58778548 -0.79051709 0.8090173 -0.30901715 -0.79051709 0.95105696 0 -0.79051709 1.000000476837
		 0.30901715 -0.79051709 0.95105702 0.5877856 -0.79051709 0.80901748 0.80901754 -0.79051709 0.5877856
		 0.95105714 -0.79051709 0.30901718 1 -1.016379356 -2.2568155e-016 0.95105654 -1.016379356 -0.309017
		 0.809017 -1.016379356 -0.5877853 0.58778524 -1.016379356 -0.80901706 0.30901697 -1.016379356 -0.9510566
		 -2.9802322e-008 -1.016379356 -1.000000119209 -0.30901706 -1.016379356 -0.95105666
		 -0.58778536 -1.016379356 -0.80901712 -0.80901718 -1.016379356 -0.58778536 -0.95105678 -1.016379356 -0.30901706
		 -1.000000238419 -1.016379356 -2.2568155e-016 -0.95105678 -1.016379356 0.30901706
		 -0.80901724 -1.016379356 0.58778542 -0.58778548 -1.016379356 0.8090173 -0.30901715 -1.016379356 0.95105696
		 0 -1.016379356 1.000000476837 0.30901715 -1.016379356 0.95105702 0.5877856 -1.016379356 0.80901748
		 0.80901754 -1.016379356 0.5877856 0.95105714 -1.016379356 0.30901718 1 -1.2422415 -2.7583302e-016
		 0.95105654 -1.2422415 -0.309017 0.809017 -1.2422415 -0.5877853 0.58778524 -1.2422415 -0.80901706
		 0.30901697 -1.2422415 -0.9510566 -2.9802322e-008 -1.2422415 -1.000000119209 -0.30901706 -1.2422415 -0.95105666
		 -0.58778536 -1.2422415 -0.80901712 -0.80901718 -1.2422415 -0.58778536 -0.95105678 -1.2422415 -0.30901706
		 -1.000000238419 -1.2422415 -2.7583302e-016 -0.95105678 -1.2422415 0.30901706 -0.80901724 -1.2422415 0.58778542
		 -0.58778548 -1.2422415 0.8090173 -0.30901715 -1.2422415 0.95105696 0 -1.2422415 1.000000476837
		 0.30901715 -1.2422415 0.95105702 0.5877856 -1.2422415 0.80901748 0.80901754 -1.2422415 0.5877856
		 0.95105714 -1.2422415 0.30901718 1 -1.46810329 -3.2598441e-016 0.95105654 -1.46810329 -0.309017
		 0.809017 -1.46810329 -0.5877853 0.58778524 -1.46810329 -0.80901706 0.30901697 -1.46810329 -0.9510566
		 -2.9802322e-008 -1.46810329 -1.000000119209 -0.30901706 -1.46810329 -0.95105666 -0.58778536 -1.46810329 -0.80901712
		 -0.80901718 -1.46810329 -0.58778536 -0.95105678 -1.46810329 -0.30901706 -1.000000238419 -1.46810329 -3.2598441e-016
		 -0.95105678 -1.46810329 0.30901706 -0.80901724 -1.46810329 0.58778542 -0.58778548 -1.46810329 0.8090173
		 -0.30901715 -1.46810329 0.95105696 0 -1.46810329 1.000000476837 0.30901715 -1.46810329 0.95105702
		 0.5877856 -1.46810329 0.80901748 0.80901754 -1.46810329 0.5877856 0.95105714 -1.46810329 0.30901718
		 1 -1.69396555 -3.7613591e-016 0.95105654 -1.69396555 -0.309017 0.809017 -1.69396555 -0.5877853
		 0.58778524 -1.69396555 -0.80901706 0.30901697 -1.69396555 -0.9510566 -2.9802322e-008 -1.69396555 -1.000000119209
		 -0.30901706 -1.69396555 -0.95105666 -0.58778536 -1.69396555 -0.80901712 -0.80901718 -1.69396555 -0.58778536
		 -0.95105678 -1.69396555 -0.30901706 -1.000000238419 -1.69396555 -3.7613591e-016 -0.95105678 -1.69396555 0.30901706
		 -0.80901724 -1.69396555 0.58778542 -0.58778548 -1.69396555 0.8090173 -0.30901715 -1.69396555 0.95105696
		 0 -1.69396555 1.000000476837 0.30901715 -1.69396555 0.95105702 0.5877856 -1.69396555 0.80901748
		 0.80901754 -1.69396555 0.5877856 0.95105714 -1.69396555 0.30901718 1 -1.9198277 -4.2628738e-016
		 0.95105654 -1.9198277 -0.309017 0.809017 -1.9198277 -0.5877853 0.58778524 -1.9198277 -0.80901706
		 0.30901697 -1.9198277 -0.9510566 -2.9802322e-008 -1.9198277 -1.000000119209 -0.30901706 -1.9198277 -0.95105666
		 -0.58778536 -1.9198277 -0.80901712 -0.80901718 -1.9198277 -0.58778536 -0.95105678 -1.9198277 -0.30901706
		 -1.000000238419 -1.9198277 -4.2628738e-016 -0.95105678 -1.9198277 0.30901706 -0.80901724 -1.9198277 0.58778542
		 -0.58778548 -1.9198277 0.8090173 -0.30901715 -1.9198277 0.95105696 0 -1.9198277 1.000000476837
		 0.30901715 -1.9198277 0.95105702 0.5877856 -1.9198277 0.80901748 0.80901754 -1.9198277 0.5877856
		 0.95105714 -1.9198277 0.30901718 1 -2.14568949 -4.7643877e-016 0.95105654 -2.14568949 -0.309017
		 0.809017 -2.14568949 -0.5877853 0.58778524 -2.14568949 -0.80901706 0.30901697 -2.14568949 -0.9510566
		 -2.9802322e-008 -2.14568949 -1.000000119209 -0.30901706 -2.14568949 -0.95105666 -0.58778536 -2.14568949 -0.80901712
		 -0.80901718 -2.14568949 -0.58778536 -0.95105678 -2.14568949 -0.30901706 -1.000000238419 -2.14568949 -4.7643877e-016
		 -0.95105678 -2.14568949 0.30901706 -0.80901724 -2.14568949 0.58778542 -0.58778548 -2.14568949 0.8090173
		 -0.30901715 -2.14568949 0.95105696 0 -2.14568949 1.000000476837 0.30901715 -2.14568949 0.95105702
		 0.5877856 -2.14568949 0.80901748;
	setAttr ".vt[498:599]" 0.80901754 -2.14568949 0.5877856 0.95105714 -2.14568949 0.30901718
		 1 -2.37155175 -5.2659027e-016 0.95105654 -2.37155175 -0.309017 0.809017 -2.37155175 -0.5877853
		 0.58778524 -2.37155175 -0.80901706 0.30901697 -2.37155175 -0.9510566 -2.9802322e-008 -2.37155175 -1.000000119209
		 -0.30901706 -2.37155175 -0.95105666 -0.58778536 -2.37155175 -0.80901712 -0.80901718 -2.37155175 -0.58778536
		 -0.95105678 -2.37155175 -0.30901706 -1.000000238419 -2.37155175 -5.2659027e-016 -0.95105678 -2.37155175 0.30901706
		 -0.80901724 -2.37155175 0.58778542 -0.58778548 -2.37155175 0.8090173 -0.30901715 -2.37155175 0.95105696
		 0 -2.37155175 1.000000476837 0.30901715 -2.37155175 0.95105702 0.5877856 -2.37155175 0.80901748
		 0.80901754 -2.37155175 0.5877856 0.95105714 -2.37155175 0.30901718 1 -2.59741378 -5.7674172e-016
		 0.95105654 -2.59741378 -0.309017 0.809017 -2.59741378 -0.5877853 0.58778524 -2.59741378 -0.80901706
		 0.30901697 -2.59741378 -0.9510566 -2.9802322e-008 -2.59741378 -1.000000119209 -0.30901706 -2.59741378 -0.95105666
		 -0.58778536 -2.59741378 -0.80901712 -0.80901718 -2.59741378 -0.58778536 -0.95105678 -2.59741378 -0.30901706
		 -1.000000238419 -2.59741378 -5.7674172e-016 -0.95105678 -2.59741378 0.30901706 -0.80901724 -2.59741378 0.58778542
		 -0.58778548 -2.59741378 0.8090173 -0.30901715 -2.59741378 0.95105696 0 -2.59741378 1.000000476837
		 0.30901715 -2.59741378 0.95105702 0.5877856 -2.59741378 0.80901748 0.80901754 -2.59741378 0.5877856
		 0.95105714 -2.59741378 0.30901718 1 -2.82327604 -6.2689321e-016 0.95105654 -2.82327604 -0.309017
		 0.809017 -2.82327604 -0.5877853 0.58778524 -2.82327604 -0.80901706 0.30901697 -2.82327604 -0.9510566
		 -2.9802322e-008 -2.82327604 -1.000000119209 -0.30901706 -2.82327604 -0.95105666 -0.58778536 -2.82327604 -0.80901712
		 -0.80901718 -2.82327604 -0.58778536 -0.95105678 -2.82327604 -0.30901706 -1.000000238419 -2.82327604 -6.2689321e-016
		 -0.95105678 -2.82327604 0.30901706 -0.80901724 -2.82327604 0.58778542 -0.58778548 -2.82327604 0.8090173
		 -0.30901715 -2.82327604 0.95105696 0 -2.82327604 1.000000476837 0.30901715 -2.82327604 0.95105702
		 0.5877856 -2.82327604 0.80901748 0.80901754 -2.82327604 0.5877856 0.95105714 -2.82327604 0.30901718
		 1 -3.049137831 -6.770446e-016 0.95105654 -3.049137831 -0.309017 0.809017 -3.049137831 -0.5877853
		 0.58778524 -3.049137831 -0.80901706 0.30901697 -3.049137831 -0.9510566 -2.9802322e-008 -3.049137831 -1.000000119209
		 -0.30901706 -3.049137831 -0.95105666 -0.58778536 -3.049137831 -0.80901712 -0.80901718 -3.049137831 -0.58778536
		 -0.95105678 -3.049137831 -0.30901706 -1.000000238419 -3.049137831 -6.770446e-016
		 -0.95105678 -3.049137831 0.30901706 -0.80901724 -3.049137831 0.58778542 -0.58778548 -3.049137831 0.8090173
		 -0.30901715 -3.049137831 0.95105696 0 -3.049137831 1.000000476837 0.30901715 -3.049137831 0.95105702
		 0.5877856 -3.049137831 0.80901748 0.80901754 -3.049137831 0.5877856 0.95105714 -3.049137831 0.30901718
		 1 -3.2750001 -7.271961e-016 0.95105654 -3.2750001 -0.309017 0.809017 -3.2750001 -0.5877853
		 0.58778524 -3.2750001 -0.80901706 0.30901697 -3.2750001 -0.9510566 -2.9802322e-008 -3.2750001 -1.000000119209
		 -0.30901706 -3.2750001 -0.95105666 -0.58778536 -3.2750001 -0.80901712 -0.80901718 -3.2750001 -0.58778536
		 -0.95105678 -3.2750001 -0.30901706 -1.000000238419 -3.2750001 -7.271961e-016 -0.95105678 -3.2750001 0.30901706
		 -0.80901724 -3.2750001 0.58778542 -0.58778548 -3.2750001 0.8090173 -0.30901715 -3.2750001 0.95105696
		 0 -3.2750001 1.000000476837 0.30901715 -3.2750001 0.95105702 0.5877856 -3.2750001 0.80901748
		 0.80901754 -3.2750001 0.5877856 0.95105714 -3.2750001 0.30901718;
	setAttr -s 1180 ".ed";
	setAttr ".ed[0:165]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0 7 8 0 8 9 0
		 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0 18 19 0 19 0 0
		 20 21 1 21 22 1 22 23 1 23 24 1 24 25 1 25 26 1 26 27 1 27 28 1 28 29 1 29 30 1 30 31 1
		 31 32 1 32 33 1 33 34 1 34 35 1 35 36 1 36 37 1 37 38 1 38 39 1 39 20 1 40 41 1 41 42 1
		 42 43 1 43 44 1 44 45 1 45 46 1 46 47 1 47 48 1 48 49 1 49 50 1 50 51 1 51 52 1 52 53 1
		 53 54 1 54 55 1 55 56 1 56 57 1 57 58 1 58 59 1 59 40 1 60 61 1 61 62 1 62 63 1 63 64 1
		 64 65 1 65 66 1 66 67 1 67 68 1 68 69 1 69 70 1 70 71 1 71 72 1 72 73 1 73 74 1 74 75 1
		 75 76 1 76 77 1 77 78 1 78 79 1 79 60 1 80 81 1 81 82 1 82 83 1 83 84 1 84 85 1 85 86 1
		 86 87 1 87 88 1 88 89 1 89 90 1 90 91 1 91 92 1 92 93 1 93 94 1 94 95 1 95 96 1 96 97 1
		 97 98 1 98 99 1 99 80 1 100 101 1 101 102 1 102 103 1 103 104 1 104 105 1 105 106 1
		 106 107 1 107 108 1 108 109 1 109 110 1 110 111 1 111 112 1 112 113 1 113 114 1 114 115 1
		 115 116 1 116 117 1 117 118 1 118 119 1 119 100 1 120 121 1 121 122 1 122 123 1 123 124 1
		 124 125 1 125 126 1 126 127 1 127 128 1 128 129 1 129 130 1 130 131 1 131 132 1 132 133 1
		 133 134 1 134 135 1 135 136 1 136 137 1 137 138 1 138 139 1 139 120 1 140 141 1 141 142 1
		 142 143 1 143 144 1 144 145 1 145 146 1 146 147 1 147 148 1 148 149 1 149 150 1 150 151 1
		 151 152 1 152 153 1 153 154 1 154 155 1 155 156 1 156 157 1 157 158 1 158 159 1 159 140 1
		 160 161 1 161 162 1 162 163 1 163 164 1 164 165 1 165 166 1;
	setAttr ".ed[166:331]" 166 167 1 167 168 1 168 169 1 169 170 1 170 171 1 171 172 1
		 172 173 1 173 174 1 174 175 1 175 176 1 176 177 1 177 178 1 178 179 1 179 160 1 180 181 1
		 181 182 1 182 183 1 183 184 1 184 185 1 185 186 1 186 187 1 187 188 1 188 189 1 189 190 1
		 190 191 1 191 192 1 192 193 1 193 194 1 194 195 1 195 196 1 196 197 1 197 198 1 198 199 1
		 199 180 1 200 201 1 201 202 1 202 203 1 203 204 1 204 205 1 205 206 1 206 207 1 207 208 1
		 208 209 1 209 210 1 210 211 1 211 212 1 212 213 1 213 214 1 214 215 1 215 216 1 216 217 1
		 217 218 1 218 219 1 219 200 1 220 221 1 221 222 1 222 223 1 223 224 1 224 225 1 225 226 1
		 226 227 1 227 228 1 228 229 1 229 230 1 230 231 1 231 232 1 232 233 1 233 234 1 234 235 1
		 235 236 1 236 237 1 237 238 1 238 239 1 239 220 1 240 241 1 241 242 1 242 243 1 243 244 1
		 244 245 1 245 246 1 246 247 1 247 248 1 248 249 1 249 250 1 250 251 1 251 252 1 252 253 1
		 253 254 1 254 255 1 255 256 1 256 257 1 257 258 1 258 259 1 259 240 1 260 261 1 261 262 1
		 262 263 1 263 264 1 264 265 1 265 266 1 266 267 1 267 268 1 268 269 1 269 270 1 270 271 1
		 271 272 1 272 273 1 273 274 1 274 275 1 275 276 1 276 277 1 277 278 1 278 279 1 279 260 1
		 280 281 1 281 282 1 282 283 1 283 284 1 284 285 1 285 286 1 286 287 1 287 288 1 288 289 1
		 289 290 1 290 291 1 291 292 1 292 293 1 293 294 1 294 295 1 295 296 1 296 297 1 297 298 1
		 298 299 1 299 280 1 300 301 1 301 302 1 302 303 1 303 304 1 304 305 1 305 306 1 306 307 1
		 307 308 1 308 309 1 309 310 1 310 311 1 311 312 1 312 313 1 313 314 1 314 315 1 315 316 1
		 316 317 1 317 318 1 318 319 1 319 300 1 320 321 1 321 322 1 322 323 1 323 324 1 324 325 1
		 325 326 1 326 327 1 327 328 1 328 329 1 329 330 1 330 331 1 331 332 1;
	setAttr ".ed[332:497]" 332 333 1 333 334 1 334 335 1 335 336 1 336 337 1 337 338 1
		 338 339 1 339 320 1 340 341 1 341 342 1 342 343 1 343 344 1 344 345 1 345 346 1 346 347 1
		 347 348 1 348 349 1 349 350 1 350 351 1 351 352 1 352 353 1 353 354 1 354 355 1 355 356 1
		 356 357 1 357 358 1 358 359 1 359 340 1 360 361 1 361 362 1 362 363 1 363 364 1 364 365 1
		 365 366 1 366 367 1 367 368 1 368 369 1 369 370 1 370 371 1 371 372 1 372 373 1 373 374 1
		 374 375 1 375 376 1 376 377 1 377 378 1 378 379 1 379 360 1 380 381 1 381 382 1 382 383 1
		 383 384 1 384 385 1 385 386 1 386 387 1 387 388 1 388 389 1 389 390 1 390 391 1 391 392 1
		 392 393 1 393 394 1 394 395 1 395 396 1 396 397 1 397 398 1 398 399 1 399 380 1 400 401 1
		 401 402 1 402 403 1 403 404 1 404 405 1 405 406 1 406 407 1 407 408 1 408 409 1 409 410 1
		 410 411 1 411 412 1 412 413 1 413 414 1 414 415 1 415 416 1 416 417 1 417 418 1 418 419 1
		 419 400 1 420 421 1 421 422 1 422 423 1 423 424 1 424 425 1 425 426 1 426 427 1 427 428 1
		 428 429 1 429 430 1 430 431 1 431 432 1 432 433 1 433 434 1 434 435 1 435 436 1 436 437 1
		 437 438 1 438 439 1 439 420 1 440 441 1 441 442 1 442 443 1 443 444 1 444 445 1 445 446 1
		 446 447 1 447 448 1 448 449 1 449 450 1 450 451 1 451 452 1 452 453 1 453 454 1 454 455 1
		 455 456 1 456 457 1 457 458 1 458 459 1 459 440 1 460 461 1 461 462 1 462 463 1 463 464 1
		 464 465 1 465 466 1 466 467 1 467 468 1 468 469 1 469 470 1 470 471 1 471 472 1 472 473 1
		 473 474 1 474 475 1 475 476 1 476 477 1 477 478 1 478 479 1 479 460 1 480 481 1 481 482 1
		 482 483 1 483 484 1 484 485 1 485 486 1 486 487 1 487 488 1 488 489 1 489 490 1 490 491 1
		 491 492 1 492 493 1 493 494 1 494 495 1 495 496 1 496 497 1 497 498 1;
	setAttr ".ed[498:663]" 498 499 1 499 480 1 500 501 1 501 502 1 502 503 1 503 504 1
		 504 505 1 505 506 1 506 507 1 507 508 1 508 509 1 509 510 1 510 511 1 511 512 1 512 513 1
		 513 514 1 514 515 1 515 516 1 516 517 1 517 518 1 518 519 1 519 500 1 520 521 1 521 522 1
		 522 523 1 523 524 1 524 525 1 525 526 1 526 527 1 527 528 1 528 529 1 529 530 1 530 531 1
		 531 532 1 532 533 1 533 534 1 534 535 1 535 536 1 536 537 1 537 538 1 538 539 1 539 520 1
		 540 541 1 541 542 1 542 543 1 543 544 1 544 545 1 545 546 1 546 547 1 547 548 1 548 549 1
		 549 550 1 550 551 1 551 552 1 552 553 1 553 554 1 554 555 1 555 556 1 556 557 1 557 558 1
		 558 559 1 559 540 1 560 561 1 561 562 1 562 563 1 563 564 1 564 565 1 565 566 1 566 567 1
		 567 568 1 568 569 1 569 570 1 570 571 1 571 572 1 572 573 1 573 574 1 574 575 1 575 576 1
		 576 577 1 577 578 1 578 579 1 579 560 1 580 581 0 581 582 0 582 583 0 583 584 0 584 585 0
		 585 586 0 586 587 0 587 588 0 588 589 0 589 590 0 590 591 0 591 592 0 592 593 0 593 594 0
		 594 595 0 595 596 0 596 597 0 597 598 0 598 599 0 599 580 0 0 20 1 1 21 1 2 22 1
		 3 23 1 4 24 1 5 25 1 6 26 1 7 27 1 8 28 1 9 29 1 10 30 1 11 31 1 12 32 1 13 33 1
		 14 34 1 15 35 1 16 36 1 17 37 1 18 38 1 19 39 1 20 40 1 21 41 1 22 42 1 23 43 1 24 44 1
		 25 45 1 26 46 1 27 47 1 28 48 1 29 49 1 30 50 1 31 51 1 32 52 1 33 53 1 34 54 1 35 55 1
		 36 56 1 37 57 1 38 58 1 39 59 1 40 60 1 41 61 1 42 62 1 43 63 1 44 64 1 45 65 1 46 66 1
		 47 67 1 48 68 1 49 69 1 50 70 1 51 71 1 52 72 1 53 73 1 54 74 1 55 75 1 56 76 1 57 77 1
		 58 78 1 59 79 1 60 80 1 61 81 1 62 82 1 63 83 1;
	setAttr ".ed[664:829]" 64 84 1 65 85 1 66 86 1 67 87 1 68 88 1 69 89 1 70 90 1
		 71 91 1 72 92 1 73 93 1 74 94 1 75 95 1 76 96 1 77 97 1 78 98 1 79 99 1 80 100 1
		 81 101 1 82 102 1 83 103 1 84 104 1 85 105 1 86 106 1 87 107 1 88 108 1 89 109 1
		 90 110 1 91 111 1 92 112 1 93 113 1 94 114 1 95 115 1 96 116 1 97 117 1 98 118 1
		 99 119 1 100 120 1 101 121 1 102 122 1 103 123 1 104 124 1 105 125 1 106 126 1 107 127 1
		 108 128 1 109 129 1 110 130 1 111 131 1 112 132 1 113 133 1 114 134 1 115 135 1 116 136 1
		 117 137 1 118 138 1 119 139 1 120 140 1 121 141 1 122 142 1 123 143 1 124 144 1 125 145 1
		 126 146 1 127 147 1 128 148 1 129 149 1 130 150 1 131 151 1 132 152 1 133 153 1 134 154 1
		 135 155 1 136 156 1 137 157 1 138 158 1 139 159 1 140 160 1 141 161 1 142 162 1 143 163 1
		 144 164 1 145 165 1 146 166 1 147 167 1 148 168 1 149 169 1 150 170 1 151 171 1 152 172 1
		 153 173 1 154 174 1 155 175 1 156 176 1 157 177 1 158 178 1 159 179 1 160 180 1 161 181 1
		 162 182 1 163 183 1 164 184 1 165 185 1 166 186 1 167 187 1 168 188 1 169 189 1 170 190 1
		 171 191 1 172 192 1 173 193 1 174 194 1 175 195 1 176 196 1 177 197 1 178 198 1 179 199 1
		 180 200 1 181 201 1 182 202 1 183 203 1 184 204 1 185 205 1 186 206 1 187 207 1 188 208 1
		 189 209 1 190 210 1 191 211 1 192 212 1 193 213 1 194 214 1 195 215 1 196 216 1 197 217 1
		 198 218 1 199 219 1 200 220 1 201 221 1 202 222 1 203 223 1 204 224 1 205 225 1 206 226 1
		 207 227 1 208 228 1 209 229 1 210 230 1 211 231 1 212 232 1 213 233 1 214 234 1 215 235 1
		 216 236 1 217 237 1 218 238 1 219 239 1 220 240 1 221 241 1 222 242 1 223 243 1 224 244 1
		 225 245 1 226 246 1 227 247 1 228 248 1 229 249 1;
	setAttr ".ed[830:995]" 230 250 1 231 251 1 232 252 1 233 253 1 234 254 1 235 255 1
		 236 256 1 237 257 1 238 258 1 239 259 1 240 260 1 241 261 1 242 262 1 243 263 1 244 264 1
		 245 265 1 246 266 1 247 267 1 248 268 1 249 269 1 250 270 1 251 271 1 252 272 1 253 273 1
		 254 274 1 255 275 1 256 276 1 257 277 1 258 278 1 259 279 1 260 280 1 261 281 1 262 282 1
		 263 283 1 264 284 1 265 285 1 266 286 1 267 287 1 268 288 1 269 289 1 270 290 1 271 291 1
		 272 292 1 273 293 1 274 294 1 275 295 1 276 296 1 277 297 1 278 298 1 279 299 1 280 300 1
		 281 301 1 282 302 1 283 303 1 284 304 1 285 305 1 286 306 1 287 307 1 288 308 1 289 309 1
		 290 310 1 291 311 1 292 312 1 293 313 1 294 314 1 295 315 1 296 316 1 297 317 1 298 318 1
		 299 319 1 300 320 1 301 321 1 302 322 1 303 323 1 304 324 1 305 325 1 306 326 1 307 327 1
		 308 328 1 309 329 1 310 330 1 311 331 1 312 332 1 313 333 1 314 334 1 315 335 1 316 336 1
		 317 337 1 318 338 1 319 339 1 320 340 1 321 341 1 322 342 1 323 343 1 324 344 1 325 345 1
		 326 346 1 327 347 1 328 348 1 329 349 1 330 350 1 331 351 1 332 352 1 333 353 1 334 354 1
		 335 355 1 336 356 1 337 357 1 338 358 1 339 359 1 340 360 1 341 361 1 342 362 1 343 363 1
		 344 364 1 345 365 1 346 366 1 347 367 1 348 368 1 349 369 1 350 370 1 351 371 1 352 372 1
		 353 373 1 354 374 1 355 375 1 356 376 1 357 377 1 358 378 1 359 379 1 360 380 1 361 381 1
		 362 382 1 363 383 1 364 384 1 365 385 1 366 386 1 367 387 1 368 388 1 369 389 1 370 390 1
		 371 391 1 372 392 1 373 393 1 374 394 1 375 395 1 376 396 1 377 397 1 378 398 1 379 399 1
		 380 400 1 381 401 1 382 402 1 383 403 1 384 404 1 385 405 1 386 406 1 387 407 1 388 408 1
		 389 409 1 390 410 1 391 411 1 392 412 1 393 413 1 394 414 1 395 415 1;
	setAttr ".ed[996:1161]" 396 416 1 397 417 1 398 418 1 399 419 1 400 420 1 401 421 1
		 402 422 1 403 423 1 404 424 1 405 425 1 406 426 1 407 427 1 408 428 1 409 429 1 410 430 1
		 411 431 1 412 432 1 413 433 1 414 434 1 415 435 1 416 436 1 417 437 1 418 438 1 419 439 1
		 420 440 1 421 441 1 422 442 1 423 443 1 424 444 1 425 445 1 426 446 1 427 447 1 428 448 1
		 429 449 1 430 450 1 431 451 1 432 452 1 433 453 1 434 454 1 435 455 1 436 456 1 437 457 1
		 438 458 1 439 459 1 440 460 1 441 461 1 442 462 1 443 463 1 444 464 1 445 465 1 446 466 1
		 447 467 1 448 468 1 449 469 1 450 470 1 451 471 1 452 472 1 453 473 1 454 474 1 455 475 1
		 456 476 1 457 477 1 458 478 1 459 479 1 460 480 1 461 481 1 462 482 1 463 483 1 464 484 1
		 465 485 1 466 486 1 467 487 1 468 488 1 469 489 1 470 490 1 471 491 1 472 492 1 473 493 1
		 474 494 1 475 495 1 476 496 1 477 497 1 478 498 1 479 499 1 480 500 1 481 501 1 482 502 1
		 483 503 1 484 504 1 485 505 1 486 506 1 487 507 1 488 508 1 489 509 1 490 510 1 491 511 1
		 492 512 1 493 513 1 494 514 1 495 515 1 496 516 1 497 517 1 498 518 1 499 519 1 500 520 1
		 501 521 1 502 522 1 503 523 1 504 524 1 505 525 1 506 526 1 507 527 1 508 528 1 509 529 1
		 510 530 1 511 531 1 512 532 1 513 533 1 514 534 1 515 535 1 516 536 1 517 537 1 518 538 1
		 519 539 1 520 540 1 521 541 1 522 542 1 523 543 1 524 544 1 525 545 1 526 546 1 527 547 1
		 528 548 1 529 549 1 530 550 1 531 551 1 532 552 1 533 553 1 534 554 1 535 555 1 536 556 1
		 537 557 1 538 558 1 539 559 1 540 560 1 541 561 1 542 562 1 543 563 1 544 564 1 545 565 1
		 546 566 1 547 567 1 548 568 1 549 569 1 550 570 1 551 571 1 552 572 1 553 573 1 554 574 1
		 555 575 1 556 576 1 557 577 1 558 578 1 559 579 1 560 580 1 561 581 1;
	setAttr ".ed[1162:1179]" 562 582 1 563 583 1 564 584 1 565 585 1 566 586 1 567 587 1
		 568 588 1 569 589 1 570 590 1 571 591 1 572 592 1 573 593 1 574 594 1 575 595 1 576 596 1
		 577 597 1 578 598 1 579 599 1;
	setAttr -s 580 -ch 2320 ".fc";
	setAttr ".fc[0:499]" -type "polyFaces" 
		f 4 -1 600 20 -602
		mu 0 4 1 0 21 22
		f 4 -2 601 21 -603
		mu 0 4 2 1 22 23
		f 4 -3 602 22 -604
		mu 0 4 3 2 23 24
		f 4 -4 603 23 -605
		mu 0 4 4 3 24 25
		f 4 -5 604 24 -606
		mu 0 4 5 4 25 26
		f 4 -6 605 25 -607
		mu 0 4 6 5 26 27
		f 4 -7 606 26 -608
		mu 0 4 7 6 27 28
		f 4 -8 607 27 -609
		mu 0 4 8 7 28 29
		f 4 -9 608 28 -610
		mu 0 4 9 8 29 30
		f 4 -10 609 29 -611
		mu 0 4 10 9 30 31
		f 4 -11 610 30 -612
		mu 0 4 11 10 31 32
		f 4 -12 611 31 -613
		mu 0 4 12 11 32 33
		f 4 -13 612 32 -614
		mu 0 4 13 12 33 34
		f 4 -14 613 33 -615
		mu 0 4 14 13 34 35
		f 4 -15 614 34 -616
		mu 0 4 15 14 35 36
		f 4 -16 615 35 -617
		mu 0 4 16 15 36 37
		f 4 -17 616 36 -618
		mu 0 4 17 16 37 38
		f 4 -18 617 37 -619
		mu 0 4 18 17 38 39
		f 4 -19 618 38 -620
		mu 0 4 19 18 39 40
		f 4 -20 619 39 -601
		mu 0 4 20 19 40 41
		f 4 -21 620 40 -622
		mu 0 4 22 21 42 43
		f 4 -22 621 41 -623
		mu 0 4 23 22 43 44
		f 4 -23 622 42 -624
		mu 0 4 24 23 44 45
		f 4 -24 623 43 -625
		mu 0 4 25 24 45 46
		f 4 -25 624 44 -626
		mu 0 4 26 25 46 47
		f 4 -26 625 45 -627
		mu 0 4 27 26 47 48
		f 4 -27 626 46 -628
		mu 0 4 28 27 48 49
		f 4 -28 627 47 -629
		mu 0 4 29 28 49 50
		f 4 -29 628 48 -630
		mu 0 4 30 29 50 51
		f 4 -30 629 49 -631
		mu 0 4 31 30 51 52
		f 4 -31 630 50 -632
		mu 0 4 32 31 52 53
		f 4 -32 631 51 -633
		mu 0 4 33 32 53 54
		f 4 -33 632 52 -634
		mu 0 4 34 33 54 55
		f 4 -34 633 53 -635
		mu 0 4 35 34 55 56
		f 4 -35 634 54 -636
		mu 0 4 36 35 56 57
		f 4 -36 635 55 -637
		mu 0 4 37 36 57 58
		f 4 -37 636 56 -638
		mu 0 4 38 37 58 59
		f 4 -38 637 57 -639
		mu 0 4 39 38 59 60
		f 4 -39 638 58 -640
		mu 0 4 40 39 60 61
		f 4 -40 639 59 -621
		mu 0 4 41 40 61 62
		f 4 -41 640 60 -642
		mu 0 4 43 42 63 64
		f 4 -42 641 61 -643
		mu 0 4 44 43 64 65
		f 4 -43 642 62 -644
		mu 0 4 45 44 65 66
		f 4 -44 643 63 -645
		mu 0 4 46 45 66 67
		f 4 -45 644 64 -646
		mu 0 4 47 46 67 68
		f 4 -46 645 65 -647
		mu 0 4 48 47 68 69
		f 4 -47 646 66 -648
		mu 0 4 49 48 69 70
		f 4 -48 647 67 -649
		mu 0 4 50 49 70 71
		f 4 -49 648 68 -650
		mu 0 4 51 50 71 72
		f 4 -50 649 69 -651
		mu 0 4 52 51 72 73
		f 4 -51 650 70 -652
		mu 0 4 53 52 73 74
		f 4 -52 651 71 -653
		mu 0 4 54 53 74 75
		f 4 -53 652 72 -654
		mu 0 4 55 54 75 76
		f 4 -54 653 73 -655
		mu 0 4 56 55 76 77
		f 4 -55 654 74 -656
		mu 0 4 57 56 77 78
		f 4 -56 655 75 -657
		mu 0 4 58 57 78 79
		f 4 -57 656 76 -658
		mu 0 4 59 58 79 80
		f 4 -58 657 77 -659
		mu 0 4 60 59 80 81
		f 4 -59 658 78 -660
		mu 0 4 61 60 81 82
		f 4 -60 659 79 -641
		mu 0 4 62 61 82 83
		f 4 -61 660 80 -662
		mu 0 4 64 63 84 85
		f 4 -62 661 81 -663
		mu 0 4 65 64 85 86
		f 4 -63 662 82 -664
		mu 0 4 66 65 86 87
		f 4 -64 663 83 -665
		mu 0 4 67 66 87 88
		f 4 -65 664 84 -666
		mu 0 4 68 67 88 89
		f 4 -66 665 85 -667
		mu 0 4 69 68 89 90
		f 4 -67 666 86 -668
		mu 0 4 70 69 90 91
		f 4 -68 667 87 -669
		mu 0 4 71 70 91 92
		f 4 -69 668 88 -670
		mu 0 4 72 71 92 93
		f 4 -70 669 89 -671
		mu 0 4 73 72 93 94
		f 4 -71 670 90 -672
		mu 0 4 74 73 94 95
		f 4 -72 671 91 -673
		mu 0 4 75 74 95 96
		f 4 -73 672 92 -674
		mu 0 4 76 75 96 97
		f 4 -74 673 93 -675
		mu 0 4 77 76 97 98
		f 4 -75 674 94 -676
		mu 0 4 78 77 98 99
		f 4 -76 675 95 -677
		mu 0 4 79 78 99 100
		f 4 -77 676 96 -678
		mu 0 4 80 79 100 101
		f 4 -78 677 97 -679
		mu 0 4 81 80 101 102
		f 4 -79 678 98 -680
		mu 0 4 82 81 102 103
		f 4 -80 679 99 -661
		mu 0 4 83 82 103 104
		f 4 -81 680 100 -682
		mu 0 4 85 84 105 106
		f 4 -82 681 101 -683
		mu 0 4 86 85 106 107
		f 4 -83 682 102 -684
		mu 0 4 87 86 107 108
		f 4 -84 683 103 -685
		mu 0 4 88 87 108 109
		f 4 -85 684 104 -686
		mu 0 4 89 88 109 110
		f 4 -86 685 105 -687
		mu 0 4 90 89 110 111
		f 4 -87 686 106 -688
		mu 0 4 91 90 111 112
		f 4 -88 687 107 -689
		mu 0 4 92 91 112 113
		f 4 -89 688 108 -690
		mu 0 4 93 92 113 114
		f 4 -90 689 109 -691
		mu 0 4 94 93 114 115
		f 4 -91 690 110 -692
		mu 0 4 95 94 115 116
		f 4 -92 691 111 -693
		mu 0 4 96 95 116 117
		f 4 -93 692 112 -694
		mu 0 4 97 96 117 118
		f 4 -94 693 113 -695
		mu 0 4 98 97 118 119
		f 4 -95 694 114 -696
		mu 0 4 99 98 119 120
		f 4 -96 695 115 -697
		mu 0 4 100 99 120 121
		f 4 -97 696 116 -698
		mu 0 4 101 100 121 122
		f 4 -98 697 117 -699
		mu 0 4 102 101 122 123
		f 4 -99 698 118 -700
		mu 0 4 103 102 123 124
		f 4 -100 699 119 -681
		mu 0 4 104 103 124 125
		f 4 -101 700 120 -702
		mu 0 4 106 105 126 127
		f 4 -102 701 121 -703
		mu 0 4 107 106 127 128
		f 4 -103 702 122 -704
		mu 0 4 108 107 128 129
		f 4 -104 703 123 -705
		mu 0 4 109 108 129 130
		f 4 -105 704 124 -706
		mu 0 4 110 109 130 131
		f 4 -106 705 125 -707
		mu 0 4 111 110 131 132
		f 4 -107 706 126 -708
		mu 0 4 112 111 132 133
		f 4 -108 707 127 -709
		mu 0 4 113 112 133 134
		f 4 -109 708 128 -710
		mu 0 4 114 113 134 135
		f 4 -110 709 129 -711
		mu 0 4 115 114 135 136
		f 4 -111 710 130 -712
		mu 0 4 116 115 136 137
		f 4 -112 711 131 -713
		mu 0 4 117 116 137 138
		f 4 -113 712 132 -714
		mu 0 4 118 117 138 139
		f 4 -114 713 133 -715
		mu 0 4 119 118 139 140
		f 4 -115 714 134 -716
		mu 0 4 120 119 140 141
		f 4 -116 715 135 -717
		mu 0 4 121 120 141 142
		f 4 -117 716 136 -718
		mu 0 4 122 121 142 143
		f 4 -118 717 137 -719
		mu 0 4 123 122 143 144
		f 4 -119 718 138 -720
		mu 0 4 124 123 144 145
		f 4 -120 719 139 -701
		mu 0 4 125 124 145 146
		f 4 -121 720 140 -722
		mu 0 4 127 126 147 148
		f 4 -122 721 141 -723
		mu 0 4 128 127 148 149
		f 4 -123 722 142 -724
		mu 0 4 129 128 149 150
		f 4 -124 723 143 -725
		mu 0 4 130 129 150 151
		f 4 -125 724 144 -726
		mu 0 4 131 130 151 152
		f 4 -126 725 145 -727
		mu 0 4 132 131 152 153
		f 4 -127 726 146 -728
		mu 0 4 133 132 153 154
		f 4 -128 727 147 -729
		mu 0 4 134 133 154 155
		f 4 -129 728 148 -730
		mu 0 4 135 134 155 156
		f 4 -130 729 149 -731
		mu 0 4 136 135 156 157
		f 4 -131 730 150 -732
		mu 0 4 137 136 157 158
		f 4 -132 731 151 -733
		mu 0 4 138 137 158 159
		f 4 -133 732 152 -734
		mu 0 4 139 138 159 160
		f 4 -134 733 153 -735
		mu 0 4 140 139 160 161
		f 4 -135 734 154 -736
		mu 0 4 141 140 161 162
		f 4 -136 735 155 -737
		mu 0 4 142 141 162 163
		f 4 -137 736 156 -738
		mu 0 4 143 142 163 164
		f 4 -138 737 157 -739
		mu 0 4 144 143 164 165
		f 4 -139 738 158 -740
		mu 0 4 145 144 165 166
		f 4 -140 739 159 -721
		mu 0 4 146 145 166 167
		f 4 -141 740 160 -742
		mu 0 4 148 147 168 169
		f 4 -142 741 161 -743
		mu 0 4 149 148 169 170
		f 4 -143 742 162 -744
		mu 0 4 150 149 170 171
		f 4 -144 743 163 -745
		mu 0 4 151 150 171 172
		f 4 -145 744 164 -746
		mu 0 4 152 151 172 173
		f 4 -146 745 165 -747
		mu 0 4 153 152 173 174
		f 4 -147 746 166 -748
		mu 0 4 154 153 174 175
		f 4 -148 747 167 -749
		mu 0 4 155 154 175 176
		f 4 -149 748 168 -750
		mu 0 4 156 155 176 177
		f 4 -150 749 169 -751
		mu 0 4 157 156 177 178
		f 4 -151 750 170 -752
		mu 0 4 158 157 178 179
		f 4 -152 751 171 -753
		mu 0 4 159 158 179 180
		f 4 -153 752 172 -754
		mu 0 4 160 159 180 181
		f 4 -154 753 173 -755
		mu 0 4 161 160 181 182
		f 4 -155 754 174 -756
		mu 0 4 162 161 182 183
		f 4 -156 755 175 -757
		mu 0 4 163 162 183 184
		f 4 -157 756 176 -758
		mu 0 4 164 163 184 185
		f 4 -158 757 177 -759
		mu 0 4 165 164 185 186
		f 4 -159 758 178 -760
		mu 0 4 166 165 186 187
		f 4 -160 759 179 -741
		mu 0 4 167 166 187 188
		f 4 -161 760 180 -762
		mu 0 4 169 168 189 190
		f 4 -162 761 181 -763
		mu 0 4 170 169 190 191
		f 4 -163 762 182 -764
		mu 0 4 171 170 191 192
		f 4 -164 763 183 -765
		mu 0 4 172 171 192 193
		f 4 -165 764 184 -766
		mu 0 4 173 172 193 194
		f 4 -166 765 185 -767
		mu 0 4 174 173 194 195
		f 4 -167 766 186 -768
		mu 0 4 175 174 195 196
		f 4 -168 767 187 -769
		mu 0 4 176 175 196 197
		f 4 -169 768 188 -770
		mu 0 4 177 176 197 198
		f 4 -170 769 189 -771
		mu 0 4 178 177 198 199
		f 4 -171 770 190 -772
		mu 0 4 179 178 199 200
		f 4 -172 771 191 -773
		mu 0 4 180 179 200 201
		f 4 -173 772 192 -774
		mu 0 4 181 180 201 202
		f 4 -174 773 193 -775
		mu 0 4 182 181 202 203
		f 4 -175 774 194 -776
		mu 0 4 183 182 203 204
		f 4 -176 775 195 -777
		mu 0 4 184 183 204 205
		f 4 -177 776 196 -778
		mu 0 4 185 184 205 206
		f 4 -178 777 197 -779
		mu 0 4 186 185 206 207
		f 4 -179 778 198 -780
		mu 0 4 187 186 207 208
		f 4 -180 779 199 -761
		mu 0 4 188 187 208 209
		f 4 -181 780 200 -782
		mu 0 4 190 189 210 211
		f 4 -182 781 201 -783
		mu 0 4 191 190 211 212
		f 4 -183 782 202 -784
		mu 0 4 192 191 212 213
		f 4 -184 783 203 -785
		mu 0 4 193 192 213 214
		f 4 -185 784 204 -786
		mu 0 4 194 193 214 215
		f 4 -186 785 205 -787
		mu 0 4 195 194 215 216
		f 4 -187 786 206 -788
		mu 0 4 196 195 216 217
		f 4 -188 787 207 -789
		mu 0 4 197 196 217 218
		f 4 -189 788 208 -790
		mu 0 4 198 197 218 219
		f 4 -190 789 209 -791
		mu 0 4 199 198 219 220
		f 4 -191 790 210 -792
		mu 0 4 200 199 220 221
		f 4 -192 791 211 -793
		mu 0 4 201 200 221 222
		f 4 -193 792 212 -794
		mu 0 4 202 201 222 223
		f 4 -194 793 213 -795
		mu 0 4 203 202 223 224
		f 4 -195 794 214 -796
		mu 0 4 204 203 224 225
		f 4 -196 795 215 -797
		mu 0 4 205 204 225 226
		f 4 -197 796 216 -798
		mu 0 4 206 205 226 227
		f 4 -198 797 217 -799
		mu 0 4 207 206 227 228
		f 4 -199 798 218 -800
		mu 0 4 208 207 228 229
		f 4 -200 799 219 -781
		mu 0 4 209 208 229 230
		f 4 -201 800 220 -802
		mu 0 4 211 210 231 232
		f 4 -202 801 221 -803
		mu 0 4 212 211 232 233
		f 4 -203 802 222 -804
		mu 0 4 213 212 233 234
		f 4 -204 803 223 -805
		mu 0 4 214 213 234 235
		f 4 -205 804 224 -806
		mu 0 4 215 214 235 236
		f 4 -206 805 225 -807
		mu 0 4 216 215 236 237
		f 4 -207 806 226 -808
		mu 0 4 217 216 237 238
		f 4 -208 807 227 -809
		mu 0 4 218 217 238 239
		f 4 -209 808 228 -810
		mu 0 4 219 218 239 240
		f 4 -210 809 229 -811
		mu 0 4 220 219 240 241
		f 4 -211 810 230 -812
		mu 0 4 221 220 241 242
		f 4 -212 811 231 -813
		mu 0 4 222 221 242 243
		f 4 -213 812 232 -814
		mu 0 4 223 222 243 244
		f 4 -214 813 233 -815
		mu 0 4 224 223 244 245
		f 4 -215 814 234 -816
		mu 0 4 225 224 245 246
		f 4 -216 815 235 -817
		mu 0 4 226 225 246 247
		f 4 -217 816 236 -818
		mu 0 4 227 226 247 248
		f 4 -218 817 237 -819
		mu 0 4 228 227 248 249
		f 4 -219 818 238 -820
		mu 0 4 229 228 249 250
		f 4 -220 819 239 -801
		mu 0 4 230 229 250 251
		f 4 -221 820 240 -822
		mu 0 4 232 231 252 253
		f 4 -222 821 241 -823
		mu 0 4 233 232 253 254
		f 4 -223 822 242 -824
		mu 0 4 234 233 254 255
		f 4 -224 823 243 -825
		mu 0 4 235 234 255 256
		f 4 -225 824 244 -826
		mu 0 4 236 235 256 257
		f 4 -226 825 245 -827
		mu 0 4 237 236 257 258
		f 4 -227 826 246 -828
		mu 0 4 238 237 258 259
		f 4 -228 827 247 -829
		mu 0 4 239 238 259 260
		f 4 -229 828 248 -830
		mu 0 4 240 239 260 261
		f 4 -230 829 249 -831
		mu 0 4 241 240 261 262
		f 4 -231 830 250 -832
		mu 0 4 242 241 262 263
		f 4 -232 831 251 -833
		mu 0 4 243 242 263 264
		f 4 -233 832 252 -834
		mu 0 4 244 243 264 265
		f 4 -234 833 253 -835
		mu 0 4 245 244 265 266
		f 4 -235 834 254 -836
		mu 0 4 246 245 266 267
		f 4 -236 835 255 -837
		mu 0 4 247 246 267 268
		f 4 -237 836 256 -838
		mu 0 4 248 247 268 269
		f 4 -238 837 257 -839
		mu 0 4 249 248 269 270
		f 4 -239 838 258 -840
		mu 0 4 250 249 270 271
		f 4 -240 839 259 -821
		mu 0 4 251 250 271 272
		f 4 -241 840 260 -842
		mu 0 4 253 252 273 274
		f 4 -242 841 261 -843
		mu 0 4 254 253 274 275
		f 4 -243 842 262 -844
		mu 0 4 255 254 275 276
		f 4 -244 843 263 -845
		mu 0 4 256 255 276 277
		f 4 -245 844 264 -846
		mu 0 4 257 256 277 278
		f 4 -246 845 265 -847
		mu 0 4 258 257 278 279
		f 4 -247 846 266 -848
		mu 0 4 259 258 279 280
		f 4 -248 847 267 -849
		mu 0 4 260 259 280 281
		f 4 -249 848 268 -850
		mu 0 4 261 260 281 282
		f 4 -250 849 269 -851
		mu 0 4 262 261 282 283
		f 4 -251 850 270 -852
		mu 0 4 263 262 283 284
		f 4 -252 851 271 -853
		mu 0 4 264 263 284 285
		f 4 -253 852 272 -854
		mu 0 4 265 264 285 286
		f 4 -254 853 273 -855
		mu 0 4 266 265 286 287
		f 4 -255 854 274 -856
		mu 0 4 267 266 287 288
		f 4 -256 855 275 -857
		mu 0 4 268 267 288 289
		f 4 -257 856 276 -858
		mu 0 4 269 268 289 290
		f 4 -258 857 277 -859
		mu 0 4 270 269 290 291
		f 4 -259 858 278 -860
		mu 0 4 271 270 291 292
		f 4 -260 859 279 -841
		mu 0 4 272 271 292 293
		f 4 -261 860 280 -862
		mu 0 4 274 273 294 295
		f 4 -262 861 281 -863
		mu 0 4 275 274 295 296
		f 4 -263 862 282 -864
		mu 0 4 276 275 296 297
		f 4 -264 863 283 -865
		mu 0 4 277 276 297 298
		f 4 -265 864 284 -866
		mu 0 4 278 277 298 299
		f 4 -266 865 285 -867
		mu 0 4 279 278 299 300
		f 4 -267 866 286 -868
		mu 0 4 280 279 300 301
		f 4 -268 867 287 -869
		mu 0 4 281 280 301 302
		f 4 -269 868 288 -870
		mu 0 4 282 281 302 303
		f 4 -270 869 289 -871
		mu 0 4 283 282 303 304
		f 4 -271 870 290 -872
		mu 0 4 284 283 304 305
		f 4 -272 871 291 -873
		mu 0 4 285 284 305 306
		f 4 -273 872 292 -874
		mu 0 4 286 285 306 307
		f 4 -274 873 293 -875
		mu 0 4 287 286 307 308
		f 4 -275 874 294 -876
		mu 0 4 288 287 308 309
		f 4 -276 875 295 -877
		mu 0 4 289 288 309 310
		f 4 -277 876 296 -878
		mu 0 4 290 289 310 311
		f 4 -278 877 297 -879
		mu 0 4 291 290 311 312
		f 4 -279 878 298 -880
		mu 0 4 292 291 312 313
		f 4 -280 879 299 -861
		mu 0 4 293 292 313 314
		f 4 -281 880 300 -882
		mu 0 4 295 294 315 316
		f 4 -282 881 301 -883
		mu 0 4 296 295 316 317
		f 4 -283 882 302 -884
		mu 0 4 297 296 317 318
		f 4 -284 883 303 -885
		mu 0 4 298 297 318 319
		f 4 -285 884 304 -886
		mu 0 4 299 298 319 320
		f 4 -286 885 305 -887
		mu 0 4 300 299 320 321
		f 4 -287 886 306 -888
		mu 0 4 301 300 321 322
		f 4 -288 887 307 -889
		mu 0 4 302 301 322 323
		f 4 -289 888 308 -890
		mu 0 4 303 302 323 324
		f 4 -290 889 309 -891
		mu 0 4 304 303 324 325
		f 4 -291 890 310 -892
		mu 0 4 305 304 325 326
		f 4 -292 891 311 -893
		mu 0 4 306 305 326 327
		f 4 -293 892 312 -894
		mu 0 4 307 306 327 328
		f 4 -294 893 313 -895
		mu 0 4 308 307 328 329
		f 4 -295 894 314 -896
		mu 0 4 309 308 329 330
		f 4 -296 895 315 -897
		mu 0 4 310 309 330 331
		f 4 -297 896 316 -898
		mu 0 4 311 310 331 332
		f 4 -298 897 317 -899
		mu 0 4 312 311 332 333
		f 4 -299 898 318 -900
		mu 0 4 313 312 333 334
		f 4 -300 899 319 -881
		mu 0 4 314 313 334 335
		f 4 -301 900 320 -902
		mu 0 4 316 315 336 337
		f 4 -302 901 321 -903
		mu 0 4 317 316 337 338
		f 4 -303 902 322 -904
		mu 0 4 318 317 338 339
		f 4 -304 903 323 -905
		mu 0 4 319 318 339 340
		f 4 -305 904 324 -906
		mu 0 4 320 319 340 341
		f 4 -306 905 325 -907
		mu 0 4 321 320 341 342
		f 4 -307 906 326 -908
		mu 0 4 322 321 342 343
		f 4 -308 907 327 -909
		mu 0 4 323 322 343 344
		f 4 -309 908 328 -910
		mu 0 4 324 323 344 345
		f 4 -310 909 329 -911
		mu 0 4 325 324 345 346
		f 4 -311 910 330 -912
		mu 0 4 326 325 346 347
		f 4 -312 911 331 -913
		mu 0 4 327 326 347 348
		f 4 -313 912 332 -914
		mu 0 4 328 327 348 349
		f 4 -314 913 333 -915
		mu 0 4 329 328 349 350
		f 4 -315 914 334 -916
		mu 0 4 330 329 350 351
		f 4 -316 915 335 -917
		mu 0 4 331 330 351 352
		f 4 -317 916 336 -918
		mu 0 4 332 331 352 353
		f 4 -318 917 337 -919
		mu 0 4 333 332 353 354
		f 4 -319 918 338 -920
		mu 0 4 334 333 354 355
		f 4 -320 919 339 -901
		mu 0 4 335 334 355 356
		f 4 -321 920 340 -922
		mu 0 4 337 336 357 358
		f 4 -322 921 341 -923
		mu 0 4 338 337 358 359
		f 4 -323 922 342 -924
		mu 0 4 339 338 359 360
		f 4 -324 923 343 -925
		mu 0 4 340 339 360 361
		f 4 -325 924 344 -926
		mu 0 4 341 340 361 362
		f 4 -326 925 345 -927
		mu 0 4 342 341 362 363
		f 4 -327 926 346 -928
		mu 0 4 343 342 363 364
		f 4 -328 927 347 -929
		mu 0 4 344 343 364 365
		f 4 -329 928 348 -930
		mu 0 4 345 344 365 366
		f 4 -330 929 349 -931
		mu 0 4 346 345 366 367
		f 4 -331 930 350 -932
		mu 0 4 347 346 367 368
		f 4 -332 931 351 -933
		mu 0 4 348 347 368 369
		f 4 -333 932 352 -934
		mu 0 4 349 348 369 370
		f 4 -334 933 353 -935
		mu 0 4 350 349 370 371
		f 4 -335 934 354 -936
		mu 0 4 351 350 371 372
		f 4 -336 935 355 -937
		mu 0 4 352 351 372 373
		f 4 -337 936 356 -938
		mu 0 4 353 352 373 374
		f 4 -338 937 357 -939
		mu 0 4 354 353 374 375
		f 4 -339 938 358 -940
		mu 0 4 355 354 375 376
		f 4 -340 939 359 -921
		mu 0 4 356 355 376 377
		f 4 -341 940 360 -942
		mu 0 4 358 357 378 379
		f 4 -342 941 361 -943
		mu 0 4 359 358 379 380
		f 4 -343 942 362 -944
		mu 0 4 360 359 380 381
		f 4 -344 943 363 -945
		mu 0 4 361 360 381 382
		f 4 -345 944 364 -946
		mu 0 4 362 361 382 383
		f 4 -346 945 365 -947
		mu 0 4 363 362 383 384
		f 4 -347 946 366 -948
		mu 0 4 364 363 384 385
		f 4 -348 947 367 -949
		mu 0 4 365 364 385 386
		f 4 -349 948 368 -950
		mu 0 4 366 365 386 387
		f 4 -350 949 369 -951
		mu 0 4 367 366 387 388
		f 4 -351 950 370 -952
		mu 0 4 368 367 388 389
		f 4 -352 951 371 -953
		mu 0 4 369 368 389 390
		f 4 -353 952 372 -954
		mu 0 4 370 369 390 391
		f 4 -354 953 373 -955
		mu 0 4 371 370 391 392
		f 4 -355 954 374 -956
		mu 0 4 372 371 392 393
		f 4 -356 955 375 -957
		mu 0 4 373 372 393 394
		f 4 -357 956 376 -958
		mu 0 4 374 373 394 395
		f 4 -358 957 377 -959
		mu 0 4 375 374 395 396
		f 4 -359 958 378 -960
		mu 0 4 376 375 396 397
		f 4 -360 959 379 -941
		mu 0 4 377 376 397 398
		f 4 -361 960 380 -962
		mu 0 4 379 378 399 400
		f 4 -362 961 381 -963
		mu 0 4 380 379 400 401
		f 4 -363 962 382 -964
		mu 0 4 381 380 401 402
		f 4 -364 963 383 -965
		mu 0 4 382 381 402 403
		f 4 -365 964 384 -966
		mu 0 4 383 382 403 404
		f 4 -366 965 385 -967
		mu 0 4 384 383 404 405
		f 4 -367 966 386 -968
		mu 0 4 385 384 405 406
		f 4 -368 967 387 -969
		mu 0 4 386 385 406 407
		f 4 -369 968 388 -970
		mu 0 4 387 386 407 408
		f 4 -370 969 389 -971
		mu 0 4 388 387 408 409
		f 4 -371 970 390 -972
		mu 0 4 389 388 409 410
		f 4 -372 971 391 -973
		mu 0 4 390 389 410 411
		f 4 -373 972 392 -974
		mu 0 4 391 390 411 412
		f 4 -374 973 393 -975
		mu 0 4 392 391 412 413
		f 4 -375 974 394 -976
		mu 0 4 393 392 413 414
		f 4 -376 975 395 -977
		mu 0 4 394 393 414 415
		f 4 -377 976 396 -978
		mu 0 4 395 394 415 416
		f 4 -378 977 397 -979
		mu 0 4 396 395 416 417
		f 4 -379 978 398 -980
		mu 0 4 397 396 417 418
		f 4 -380 979 399 -961
		mu 0 4 398 397 418 419
		f 4 -381 980 400 -982
		mu 0 4 400 399 420 421
		f 4 -382 981 401 -983
		mu 0 4 401 400 421 422
		f 4 -383 982 402 -984
		mu 0 4 402 401 422 423
		f 4 -384 983 403 -985
		mu 0 4 403 402 423 424
		f 4 -385 984 404 -986
		mu 0 4 404 403 424 425
		f 4 -386 985 405 -987
		mu 0 4 405 404 425 426
		f 4 -387 986 406 -988
		mu 0 4 406 405 426 427
		f 4 -388 987 407 -989
		mu 0 4 407 406 427 428
		f 4 -389 988 408 -990
		mu 0 4 408 407 428 429
		f 4 -390 989 409 -991
		mu 0 4 409 408 429 430
		f 4 -391 990 410 -992
		mu 0 4 410 409 430 431
		f 4 -392 991 411 -993
		mu 0 4 411 410 431 432
		f 4 -393 992 412 -994
		mu 0 4 412 411 432 433
		f 4 -394 993 413 -995
		mu 0 4 413 412 433 434
		f 4 -395 994 414 -996
		mu 0 4 414 413 434 435
		f 4 -396 995 415 -997
		mu 0 4 415 414 435 436
		f 4 -397 996 416 -998
		mu 0 4 416 415 436 437
		f 4 -398 997 417 -999
		mu 0 4 417 416 437 438
		f 4 -399 998 418 -1000
		mu 0 4 418 417 438 439
		f 4 -400 999 419 -981
		mu 0 4 419 418 439 440
		f 4 -401 1000 420 -1002
		mu 0 4 421 420 441 442
		f 4 -402 1001 421 -1003
		mu 0 4 422 421 442 443
		f 4 -403 1002 422 -1004
		mu 0 4 423 422 443 444
		f 4 -404 1003 423 -1005
		mu 0 4 424 423 444 445
		f 4 -405 1004 424 -1006
		mu 0 4 425 424 445 446
		f 4 -406 1005 425 -1007
		mu 0 4 426 425 446 447
		f 4 -407 1006 426 -1008
		mu 0 4 427 426 447 448
		f 4 -408 1007 427 -1009
		mu 0 4 428 427 448 449
		f 4 -409 1008 428 -1010
		mu 0 4 429 428 449 450
		f 4 -410 1009 429 -1011
		mu 0 4 430 429 450 451
		f 4 -411 1010 430 -1012
		mu 0 4 431 430 451 452
		f 4 -412 1011 431 -1013
		mu 0 4 432 431 452 453
		f 4 -413 1012 432 -1014
		mu 0 4 433 432 453 454
		f 4 -414 1013 433 -1015
		mu 0 4 434 433 454 455
		f 4 -415 1014 434 -1016
		mu 0 4 435 434 455 456
		f 4 -416 1015 435 -1017
		mu 0 4 436 435 456 457
		f 4 -417 1016 436 -1018
		mu 0 4 437 436 457 458
		f 4 -418 1017 437 -1019
		mu 0 4 438 437 458 459
		f 4 -419 1018 438 -1020
		mu 0 4 439 438 459 460
		f 4 -420 1019 439 -1001
		mu 0 4 440 439 460 461
		f 4 -421 1020 440 -1022
		mu 0 4 442 441 462 463
		f 4 -422 1021 441 -1023
		mu 0 4 443 442 463 464
		f 4 -423 1022 442 -1024
		mu 0 4 444 443 464 465
		f 4 -424 1023 443 -1025
		mu 0 4 445 444 465 466
		f 4 -425 1024 444 -1026
		mu 0 4 446 445 466 467
		f 4 -426 1025 445 -1027
		mu 0 4 447 446 467 468
		f 4 -427 1026 446 -1028
		mu 0 4 448 447 468 469
		f 4 -428 1027 447 -1029
		mu 0 4 449 448 469 470
		f 4 -429 1028 448 -1030
		mu 0 4 450 449 470 471
		f 4 -430 1029 449 -1031
		mu 0 4 451 450 471 472
		f 4 -431 1030 450 -1032
		mu 0 4 452 451 472 473
		f 4 -432 1031 451 -1033
		mu 0 4 453 452 473 474
		f 4 -433 1032 452 -1034
		mu 0 4 454 453 474 475
		f 4 -434 1033 453 -1035
		mu 0 4 455 454 475 476
		f 4 -435 1034 454 -1036
		mu 0 4 456 455 476 477
		f 4 -436 1035 455 -1037
		mu 0 4 457 456 477 478
		f 4 -437 1036 456 -1038
		mu 0 4 458 457 478 479
		f 4 -438 1037 457 -1039
		mu 0 4 459 458 479 480
		f 4 -439 1038 458 -1040
		mu 0 4 460 459 480 481
		f 4 -440 1039 459 -1021
		mu 0 4 461 460 481 482
		f 4 -441 1040 460 -1042
		mu 0 4 463 462 483 484
		f 4 -442 1041 461 -1043
		mu 0 4 464 463 484 485
		f 4 -443 1042 462 -1044
		mu 0 4 465 464 485 486
		f 4 -444 1043 463 -1045
		mu 0 4 466 465 486 487
		f 4 -445 1044 464 -1046
		mu 0 4 467 466 487 488
		f 4 -446 1045 465 -1047
		mu 0 4 468 467 488 489
		f 4 -447 1046 466 -1048
		mu 0 4 469 468 489 490
		f 4 -448 1047 467 -1049
		mu 0 4 470 469 490 491
		f 4 -449 1048 468 -1050
		mu 0 4 471 470 491 492
		f 4 -450 1049 469 -1051
		mu 0 4 472 471 492 493
		f 4 -451 1050 470 -1052
		mu 0 4 473 472 493 494
		f 4 -452 1051 471 -1053
		mu 0 4 474 473 494 495
		f 4 -453 1052 472 -1054
		mu 0 4 475 474 495 496
		f 4 -454 1053 473 -1055
		mu 0 4 476 475 496 497
		f 4 -455 1054 474 -1056
		mu 0 4 477 476 497 498
		f 4 -456 1055 475 -1057
		mu 0 4 478 477 498 499
		f 4 -457 1056 476 -1058
		mu 0 4 479 478 499 500
		f 4 -458 1057 477 -1059
		mu 0 4 480 479 500 501
		f 4 -459 1058 478 -1060
		mu 0 4 481 480 501 502
		f 4 -460 1059 479 -1041
		mu 0 4 482 481 502 503
		f 4 -461 1060 480 -1062
		mu 0 4 484 483 504 505
		f 4 -462 1061 481 -1063
		mu 0 4 485 484 505 506
		f 4 -463 1062 482 -1064
		mu 0 4 486 485 506 507
		f 4 -464 1063 483 -1065
		mu 0 4 487 486 507 508
		f 4 -465 1064 484 -1066
		mu 0 4 488 487 508 509
		f 4 -466 1065 485 -1067
		mu 0 4 489 488 509 510
		f 4 -467 1066 486 -1068
		mu 0 4 490 489 510 511
		f 4 -468 1067 487 -1069
		mu 0 4 491 490 511 512
		f 4 -469 1068 488 -1070
		mu 0 4 492 491 512 513
		f 4 -470 1069 489 -1071
		mu 0 4 493 492 513 514
		f 4 -471 1070 490 -1072
		mu 0 4 494 493 514 515
		f 4 -472 1071 491 -1073
		mu 0 4 495 494 515 516
		f 4 -473 1072 492 -1074
		mu 0 4 496 495 516 517
		f 4 -474 1073 493 -1075
		mu 0 4 497 496 517 518
		f 4 -475 1074 494 -1076
		mu 0 4 498 497 518 519
		f 4 -476 1075 495 -1077
		mu 0 4 499 498 519 520
		f 4 -477 1076 496 -1078
		mu 0 4 500 499 520 521
		f 4 -478 1077 497 -1079
		mu 0 4 501 500 521 522
		f 4 -479 1078 498 -1080
		mu 0 4 502 501 522 523
		f 4 -480 1079 499 -1061
		mu 0 4 503 502 523 524
		f 4 -481 1080 500 -1082
		mu 0 4 505 504 525 526
		f 4 -482 1081 501 -1083
		mu 0 4 506 505 526 527
		f 4 -483 1082 502 -1084
		mu 0 4 507 506 527 528
		f 4 -484 1083 503 -1085
		mu 0 4 508 507 528 529
		f 4 -485 1084 504 -1086
		mu 0 4 509 508 529 530
		f 4 -486 1085 505 -1087
		mu 0 4 510 509 530 531
		f 4 -487 1086 506 -1088
		mu 0 4 511 510 531 532
		f 4 -488 1087 507 -1089
		mu 0 4 512 511 532 533
		f 4 -489 1088 508 -1090
		mu 0 4 513 512 533 534
		f 4 -490 1089 509 -1091
		mu 0 4 514 513 534 535
		f 4 -491 1090 510 -1092
		mu 0 4 515 514 535 536
		f 4 -492 1091 511 -1093
		mu 0 4 516 515 536 537
		f 4 -493 1092 512 -1094
		mu 0 4 517 516 537 538
		f 4 -494 1093 513 -1095
		mu 0 4 518 517 538 539
		f 4 -495 1094 514 -1096
		mu 0 4 519 518 539 540
		f 4 -496 1095 515 -1097
		mu 0 4 520 519 540 541
		f 4 -497 1096 516 -1098
		mu 0 4 521 520 541 542
		f 4 -498 1097 517 -1099
		mu 0 4 522 521 542 543
		f 4 -499 1098 518 -1100
		mu 0 4 523 522 543 544
		f 4 -500 1099 519 -1081
		mu 0 4 524 523 544 545;
	setAttr ".fc[500:579]"
		f 4 -501 1100 520 -1102
		mu 0 4 526 525 546 547
		f 4 -502 1101 521 -1103
		mu 0 4 527 526 547 548
		f 4 -503 1102 522 -1104
		mu 0 4 528 527 548 549
		f 4 -504 1103 523 -1105
		mu 0 4 529 528 549 550
		f 4 -505 1104 524 -1106
		mu 0 4 530 529 550 551
		f 4 -506 1105 525 -1107
		mu 0 4 531 530 551 552
		f 4 -507 1106 526 -1108
		mu 0 4 532 531 552 553
		f 4 -508 1107 527 -1109
		mu 0 4 533 532 553 554
		f 4 -509 1108 528 -1110
		mu 0 4 534 533 554 555
		f 4 -510 1109 529 -1111
		mu 0 4 535 534 555 556
		f 4 -511 1110 530 -1112
		mu 0 4 536 535 556 557
		f 4 -512 1111 531 -1113
		mu 0 4 537 536 557 558
		f 4 -513 1112 532 -1114
		mu 0 4 538 537 558 559
		f 4 -514 1113 533 -1115
		mu 0 4 539 538 559 560
		f 4 -515 1114 534 -1116
		mu 0 4 540 539 560 561
		f 4 -516 1115 535 -1117
		mu 0 4 541 540 561 562
		f 4 -517 1116 536 -1118
		mu 0 4 542 541 562 563
		f 4 -518 1117 537 -1119
		mu 0 4 543 542 563 564
		f 4 -519 1118 538 -1120
		mu 0 4 544 543 564 565
		f 4 -520 1119 539 -1101
		mu 0 4 545 544 565 566
		f 4 -521 1120 540 -1122
		mu 0 4 547 546 567 568
		f 4 -522 1121 541 -1123
		mu 0 4 548 547 568 569
		f 4 -523 1122 542 -1124
		mu 0 4 549 548 569 570
		f 4 -524 1123 543 -1125
		mu 0 4 550 549 570 571
		f 4 -525 1124 544 -1126
		mu 0 4 551 550 571 572
		f 4 -526 1125 545 -1127
		mu 0 4 552 551 572 573
		f 4 -527 1126 546 -1128
		mu 0 4 553 552 573 574
		f 4 -528 1127 547 -1129
		mu 0 4 554 553 574 575
		f 4 -529 1128 548 -1130
		mu 0 4 555 554 575 576
		f 4 -530 1129 549 -1131
		mu 0 4 556 555 576 577
		f 4 -531 1130 550 -1132
		mu 0 4 557 556 577 578
		f 4 -532 1131 551 -1133
		mu 0 4 558 557 578 579
		f 4 -533 1132 552 -1134
		mu 0 4 559 558 579 580
		f 4 -534 1133 553 -1135
		mu 0 4 560 559 580 581
		f 4 -535 1134 554 -1136
		mu 0 4 561 560 581 582
		f 4 -536 1135 555 -1137
		mu 0 4 562 561 582 583
		f 4 -537 1136 556 -1138
		mu 0 4 563 562 583 584
		f 4 -538 1137 557 -1139
		mu 0 4 564 563 584 585
		f 4 -539 1138 558 -1140
		mu 0 4 565 564 585 586
		f 4 -540 1139 559 -1121
		mu 0 4 566 565 586 587
		f 4 -541 1140 560 -1142
		mu 0 4 568 567 588 589
		f 4 -542 1141 561 -1143
		mu 0 4 569 568 589 590
		f 4 -543 1142 562 -1144
		mu 0 4 570 569 590 591
		f 4 -544 1143 563 -1145
		mu 0 4 571 570 591 592
		f 4 -545 1144 564 -1146
		mu 0 4 572 571 592 593
		f 4 -546 1145 565 -1147
		mu 0 4 573 572 593 594
		f 4 -547 1146 566 -1148
		mu 0 4 574 573 594 595
		f 4 -548 1147 567 -1149
		mu 0 4 575 574 595 596
		f 4 -549 1148 568 -1150
		mu 0 4 576 575 596 597
		f 4 -550 1149 569 -1151
		mu 0 4 577 576 597 598
		f 4 -551 1150 570 -1152
		mu 0 4 578 577 598 599
		f 4 -552 1151 571 -1153
		mu 0 4 579 578 599 600
		f 4 -553 1152 572 -1154
		mu 0 4 580 579 600 601
		f 4 -554 1153 573 -1155
		mu 0 4 581 580 601 602
		f 4 -555 1154 574 -1156
		mu 0 4 582 581 602 603
		f 4 -556 1155 575 -1157
		mu 0 4 583 582 603 604
		f 4 -557 1156 576 -1158
		mu 0 4 584 583 604 605
		f 4 -558 1157 577 -1159
		mu 0 4 585 584 605 606
		f 4 -559 1158 578 -1160
		mu 0 4 586 585 606 607
		f 4 -560 1159 579 -1141
		mu 0 4 587 586 607 608
		f 4 -561 1160 580 -1162
		mu 0 4 589 588 609 610
		f 4 -562 1161 581 -1163
		mu 0 4 590 589 610 611
		f 4 -563 1162 582 -1164
		mu 0 4 591 590 611 612
		f 4 -564 1163 583 -1165
		mu 0 4 592 591 612 613
		f 4 -565 1164 584 -1166
		mu 0 4 593 592 613 614
		f 4 -566 1165 585 -1167
		mu 0 4 594 593 614 615
		f 4 -567 1166 586 -1168
		mu 0 4 595 594 615 616
		f 4 -568 1167 587 -1169
		mu 0 4 596 595 616 617
		f 4 -569 1168 588 -1170
		mu 0 4 597 596 617 618
		f 4 -570 1169 589 -1171
		mu 0 4 598 597 618 619
		f 4 -571 1170 590 -1172
		mu 0 4 599 598 619 620
		f 4 -572 1171 591 -1173
		mu 0 4 600 599 620 621
		f 4 -573 1172 592 -1174
		mu 0 4 601 600 621 622
		f 4 -574 1173 593 -1175
		mu 0 4 602 601 622 623
		f 4 -575 1174 594 -1176
		mu 0 4 603 602 623 624
		f 4 -576 1175 595 -1177
		mu 0 4 604 603 624 625
		f 4 -577 1176 596 -1178
		mu 0 4 605 604 625 626
		f 4 -578 1177 597 -1179
		mu 0 4 606 605 626 627
		f 4 -579 1178 598 -1180
		mu 0 4 607 606 627 628
		f 4 -580 1179 599 -1161
		mu 0 4 608 607 628 629;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".vcs" 2;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "7F2FAFD1-4128-3B49-D037-D89EFB35F0BA";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode displayLayerManager -n "layerManager";
	rename -uid "B9F5448D-4B5F-A754-889E-85B33A098130";
createNode displayLayer -n "defaultLayer";
	rename -uid "5B9B1C58-4371-D446-6B4D-C18BAFD5AD91";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "B0546791-4714-4425-8243-C1ADB03D9828";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "DDD00425-41F3-A4E6-E0B3-4F8FA81EA7A4";
	setAttr ".g" yes;
createNode dfgMayaNode -n "ZSplineSpineCanvasOp";
	rename -uid "C8B1A9E1-4273-A3FB-810E-97BE891C761D";
	addAttr -r false -ci true -k true -sn "pelvis" -ln "pelvis" -at "matrix";
	addAttr -r false -ci true -k true -sn "torso" -ln "torso" -at "matrix";
	addAttr -r false -ci true -k true -sn "chest" -ln "chest" -at "matrix";
	addAttr -r false -ci true -k true -sn "upChest" -ln "upChest" -at "matrix";
	addAttr -r false -ci true -k true -sn "neck" -ln "neck" -at "matrix";
	addAttr -r false -ci true -k true -sn "rigScale" -ln "rigScale" -at "double";
	addAttr -r false -ci true -k true -sn "drawDebug" -ln "drawDebug" -min 0 -max 1 
		-at "bool";
	addAttr -w false -s false -ci true -m -sn "outputs" -ln "outputs" -at "matrix";
	addAttr -r false -ci true -k true -sn "numDeformers" -ln "numDeformers" -at "long";
	addAttr -r false -ci true -k true -sn "pelvisRest" -ln "pelvisRest" -at "matrix";
	addAttr -r false -ci true -k true -sn "torsoRest" -ln "torsoRest" -at "matrix";
	addAttr -r false -ci true -k true -sn "chestRest" -ln "chestRest" -at "matrix";
	addAttr -r false -ci true -k true -sn "upChestRest" -ln "upChestRest" -at "matrix";
	addAttr -r false -ci true -k true -sn "neckRest" -ln "neckRest" -at "matrix";
	addAttr -w false -s false -ci true -sn "dummyResult" -ln "dummyResult" -at "double3" 
		-nc 3;
	addAttr -w false -s false -ci true -sn "dummyResultX" -ln "dummyResultX" -at "double" 
		-p "dummyResult";
	addAttr -w false -s false -ci true -sn "dummyResultY" -ln "dummyResultY" -at "double" 
		-p "dummyResult";
	addAttr -w false -s false -ci true -sn "dummyResultZ" -ln "dummyResultZ" -at "double" 
		-p "dummyResult";
	addAttr -r false -ci true -k true -sn "defSegs" -ln "defSegs" -at "long";
	setAttr ".cch" no;
	setAttr ".ihi" 2;
	setAttr ".nds" 0;
	setAttr ".fzn" no;
	setAttr ".svd" -type "string" (
		"{\n  \"objectType\" : \"Graph\",\n  \"metadata\" : {\n    \"maya_id\" : \"1\"\n    },\n  \"title\" : \"\",\n  \"ports\" : [\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"pelvis\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Mat44\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"torso\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Mat44\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"chest\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Mat44\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"upChest\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Mat44\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n"
		+ "        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"neck\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Mat44\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"rigScale\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Scalar\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"drawDebug\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Boolean\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"nodePortType\" : \"In\",\n      \"name\" : \"outputs\",\n      \"execPortType\" : \"Out\",\n      \"typeSpec\" : \"Mat44[]\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"numDeformers\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Integer\"\n      },\n    {\n      \"objectType\" : \"Port\",\n"
		+ "      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"pelvisRest\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Mat44\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"torsoRest\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Mat44\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"chestRest\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Mat44\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"upChestRest\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Mat44\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"neckRest\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Mat44\"\n      },\n    {\n"
		+ "      \"objectType\" : \"Port\",\n      \"nodePortType\" : \"In\",\n      \"name\" : \"dummyResult\",\n      \"execPortType\" : \"Out\",\n      \"typeSpec\" : \"Vec3\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"nodePortType\" : \"In\",\n      \"name\" : \"result\",\n      \"execPortType\" : \"Out\",\n      \"typeSpec\" : \"InlineDebugShape\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"defSegs\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Integer\"\n      }\n    ],\n  \"extDeps\" : {\n    \"Kraken\" : \"*\"\n    },\n  \"nodes\" : [\n    {\n      \"objectType\" : \"Inst\",\n      \"metadata\" : {\n        \"uiGraphPos\" : \"{\\\"x\\\":461.224,\\\"y\\\":224.908}\"\n        },\n      \"name\" : \"ZSplineSpineSolver_1\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"pelvis\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"torso\"\n          },\n"
		+ "        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"chest\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"upChest\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"neck\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"rigScale\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"drawDebug\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"outputs\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"numDeformers\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"result\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n"
		+ "          \"nodePortType\" : \"In\",\n          \"name\" : \"referenceCurve\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"defaultValues\" : {\n            \"SInt32\" : 600\n            },\n          \"name\" : \"defaultVal\"\n          }\n        ],\n      \"definition\" : {\n        \"objectType\" : \"Graph\",\n        \"metadata\" : {\n          \"maya_id\" : \"2\",\n          \"uiGraphZoom\" : \"{\\n  \\\"value\\\" : 0.9513480067253113\\n  }\",\n          \"uiGraphPan\" : \"{\\n  \\\"x\\\" : 62.88127136230469,\\n  \\\"y\\\" : -207.124755859375\\n  }\"\n          },\n        \"title\" : \"ZSplineSpineSolver\",\n        \"ports\" : [\n          {\n            \"objectType\" : \"Port\",\n            \"metadata\" : {\n              \"uiPersistValue\" : \"true\"\n              },\n            \"nodePortType\" : \"Out\",\n            \"name\" : \"pelvis\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"Mat44\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"metadata\" : {\n              \"uiPersistValue\" : \"true\"\n"
		+ "              },\n            \"nodePortType\" : \"Out\",\n            \"name\" : \"torso\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"Mat44\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"metadata\" : {\n              \"uiPersistValue\" : \"true\"\n              },\n            \"nodePortType\" : \"Out\",\n            \"name\" : \"chest\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"Mat44\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"metadata\" : {\n              \"uiPersistValue\" : \"true\"\n              },\n            \"nodePortType\" : \"Out\",\n            \"name\" : \"upChest\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"Mat44\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"metadata\" : {\n              \"uiPersistValue\" : \"true\"\n              },\n            \"nodePortType\" : \"Out\",\n            \"name\" : \"neck\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"Mat44\"\n            },\n          {\n            \"objectType\" : \"Port\",\n"
		+ "            \"metadata\" : {\n              \"uiPersistValue\" : \"true\"\n              },\n            \"nodePortType\" : \"Out\",\n            \"name\" : \"rigScale\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"Scalar\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"metadata\" : {\n              \"uiPersistValue\" : \"true\"\n              },\n            \"nodePortType\" : \"Out\",\n            \"name\" : \"drawDebug\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"Boolean\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"In\",\n            \"name\" : \"outputs\",\n            \"execPortType\" : \"Out\",\n            \"typeSpec\" : \"Mat44[]\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"metadata\" : {\n              \"uiPersistValue\" : \"true\"\n              },\n            \"nodePortType\" : \"Out\",\n            \"name\" : \"numDeformers\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"Integer\"\n            },\n          {\n            \"objectType\" : \"Port\",\n"
		+ "            \"nodePortType\" : \"In\",\n            \"name\" : \"result\",\n            \"execPortType\" : \"Out\",\n            \"typeSpec\" : \"Vec3\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"Out\",\n            \"name\" : \"referenceCurve\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"ZSpline\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"Out\",\n            \"name\" : \"defaultVal\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"Integer\"\n            }\n          ],\n        \"extDeps\" : {\n          \"Math\" : \"*\"\n          },\n        \"nodes\" : [\n          {\n            \"objectType\" : \"Inst\",\n            \"metadata\" : {\n              \"uiGraphPos\" : \"{\\\"x\\\":34.7672,\\\"y\\\":325.421}\"\n              },\n            \"name\" : \"assemble\",\n            \"ports\" : [\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"In\",\n                \"name\" : \"pelvis\"\n                },\n              {\n"
		+ "                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"In\",\n                \"name\" : \"torso\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"In\",\n                \"name\" : \"chest\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"In\",\n                \"name\" : \"upchest\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"In\",\n                \"name\" : \"neck\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"Out\",\n                \"name\" : \"result\"\n                }\n              ],\n            \"definition\" : {\n              \"objectType\" : \"Func\",\n              \"metadata\" : {\n                \"uiTextColor\" : \"{\\n  \\\"r\\\" : 20,\\n  \\\"g\\\" : 20,\\n  \\\"b\\\" : 20\\n  }\",\n                \"uiNodeColor\" : \"{\\n  \\\"r\\\" : 121,\\n  \\\"g\\\" : 134,\\n  \\\"b\\\" : 143\\n  }\"\n                },\n"
		+ "              \"title\" : \"asseble\",\n              \"ports\" : [\n                {\n                  \"objectType\" : \"Port\",\n                  \"nodePortType\" : \"Out\",\n                  \"name\" : \"pelvis\",\n                  \"execPortType\" : \"In\",\n                  \"typeSpec\" : \"Mat44\"\n                  },\n                {\n                  \"objectType\" : \"Port\",\n                  \"nodePortType\" : \"Out\",\n                  \"name\" : \"torso\",\n                  \"execPortType\" : \"In\",\n                  \"typeSpec\" : \"Mat44\"\n                  },\n                {\n                  \"objectType\" : \"Port\",\n                  \"nodePortType\" : \"Out\",\n                  \"name\" : \"chest\",\n                  \"execPortType\" : \"In\",\n                  \"typeSpec\" : \"Mat44\"\n                  },\n                {\n                  \"objectType\" : \"Port\",\n                  \"nodePortType\" : \"Out\",\n                  \"name\" : \"upchest\",\n                  \"execPortType\" : \"In\",\n                  \"typeSpec\" : \"Mat44\"\n                  },\n                {\n"
		+ "                  \"objectType\" : \"Port\",\n                  \"nodePortType\" : \"Out\",\n                  \"name\" : \"neck\",\n                  \"execPortType\" : \"In\",\n                  \"typeSpec\" : \"Mat44\"\n                  },\n                {\n                  \"objectType\" : \"Port\",\n                  \"nodePortType\" : \"In\",\n                  \"name\" : \"result\",\n                  \"execPortType\" : \"Out\",\n                  \"typeSpec\" : \"Mat44[]\"\n                  }\n                ],\n              \"extDeps\" : {},\n              \"code\" : \"dfgEntry {\n  result.push(pelvis);\n  result.push(torso);\n  result.push(chest);\n  result.push(upchest);\n  result.push(neck);\n}\n\"\n              }\n            },\n          {\n            \"objectType\" : \"Inst\",\n            \"metadata\" : {\n              \"uiGraphPos\" : \"{\\\"x\\\":776.528,\\\"y\\\":244.274}\"\n              },\n            \"name\" : \"GetEmptyDebugShape2\",\n            \"ports\" : [\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"IO\",\n                \"name\" : \"exec\"\n"
		+ "                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"IO\",\n                \"name\" : \"this\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"In\",\n                \"name\" : \"name\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"Out\",\n                \"name\" : \"result\"\n                }\n              ],\n            \"executable\" : \"Fabric.Exts.InlineDrawing.DrawingHandle.GetEmptyDebugShape\",\n            \"presetGUID\" : \"DB3916AA2CE58EEAFAEDB9E2653EF4D6\"\n            },\n          {\n            \"objectType\" : \"User\",\n            \"metadata\" : {\n              \"uiTitle\" : \"Drawing\",\n              \"uiGraphPos\" : \"{\\\"x\\\":753.448,\\\"y\\\":80.90900000000001}\",\n              \"uiNodeColor\" : \"{\\n  \\\"r\\\" : 121,\\n  \\\"g\\\" : 134,\\n  \\\"b\\\" : 143\\n  }\",\n              \"uiTextColor\" : \"{\\n  \\\"r\\\" : 20,\\n  \\\"g\\\" : 20,\\n  \\\"b\\\" : 20\\n  }\",\n              \"uiGraphSize\" : \"{\\\"w\\\":611.199,\\\"h\\\":420.479}\"\n"
		+ "              },\n            \"name\" : \"uiBackDropTheDrivenRig22\",\n            \"ports\" : []\n            },\n          {\n            \"objectType\" : \"Inst\",\n            \"metadata\" : {\n              \"uiGraphPos\" : \"{\\\"x\\\":555.883,\\\"y\\\":369.326}\"\n              },\n            \"name\" : \"EmptyDrawingHandle\",\n            \"ports\" : [\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"Out\",\n                \"name\" : \"handle\"\n                }\n              ],\n            \"executable\" : \"Fabric.Exts.InlineDrawing.DrawingHandle.EmptyDrawingHandle\",\n            \"presetGUID\" : \"2440020BA6A1CAB1CEB690A198F99C70\"\n            },\n          {\n            \"objectType\" : \"Inst\",\n            \"metadata\" : {\n              \"uiGraphPos\" : \"{\\\"x\\\":776.9160000000001,\\\"y\\\":136.871}\",\n              \"uiCollapsedState\" : \"0\"\n              },\n            \"name\" : \"CreateSegs\",\n            \"ports\" : [\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"Out\",\n                \"name\" : \"result\"\n"
		+ "                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"In\",\n                \"name\" : \"this\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"Out\",\n                \"name\" : \"color\"\n                }\n              ],\n            \"executable\" : \"OSS.Exts.Curves.ZSpline.createSegsOnZSpline\",\n            \"presetGUID\" : \"D8E844DE0169A7D9BB304C9F8DDF30A2\"\n            },\n          {\n            \"objectType\" : \"Inst\",\n            \"metadata\" : {\n              \"uiGraphPos\" : \"{\\\"x\\\":1052.66,\\\"y\\\":161.581}\",\n              \"uiNodeColor\" : \"{\\n  \\\"r\\\" : 121,\\n  \\\"g\\\" : 134,\\n  \\\"b\\\" : 143\\n  }\",\n              \"uiTextColor\" : \"{\\n  \\\"r\\\" : 20,\\n  \\\"g\\\" : 20,\\n  \\\"b\\\" : 20\\n  }\",\n              \"uiCollapsedState\" : \"0\"\n              },\n            \"name\" : \"DrawCurve\",\n            \"ports\" : [\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"In\",\n                \"name\" : \"points\"\n"
		+ "                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"In\",\n                \"name\" : \"color\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"Out\",\n                \"name\" : \"result\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"IO\",\n                \"name\" : \"this\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"Out\",\n                \"name\" : \"dummyResult\"\n                }\n              ],\n            \"executable\" : \"OSS.Exts.Curves.ZSpline.drawCurve\",\n            \"presetGUID\" : \"B3D1DFFCE15CC7040DCD73D99F2C3098\"\n            },\n          {\n            \"objectType\" : \"Inst\",\n            \"metadata\" : {\n              \"uiGraphPos\" : \"{\\\"x\\\":310.545,\\\"y\\\":415.196}\"\n              },\n            \"name\" : \"buildZSpline\",\n            \"ports\" : [\n              {\n                \"objectType\" : \"InstPort\",\n"
		+ "                \"nodePortType\" : \"In\",\n                \"name\" : \"mat44s\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"Out\",\n                \"name\" : \"result\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"IO\",\n                \"name\" : \"isSegmentStart\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"IO\",\n                \"name\" : \"clamped\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"IO\",\n                \"name\" : \"weights\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"IO\",\n                \"name\" : \"resolution\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"IO\",\n                \"name\" : \"order\"\n                },\n              {\n"
		+ "                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"IO\",\n                \"name\" : \"closed\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"IO\",\n                \"name\" : \"defSegs\"\n                }\n              ],\n            \"executable\" : \"OSS.Exts.Curves.ZSpline.ZSpline\",\n            \"presetGUID\" : \"1A4FC39528C5CC9C3EF2B16480BD4E7B\"\n            },\n          {\n            \"objectType\" : \"Inst\",\n            \"metadata\" : {\n              \"uiGraphPos\" : \"{\\\"x\\\":1037.15,\\\"y\\\":323.474}\"\n              },\n            \"name\" : \"DrawAxesInstances\",\n            \"ports\" : [\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"IO\",\n                \"name\" : \"exec\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"IO\",\n                \"name\" : \"this\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"In\",\n"
		+ "                \"defaultValues\" : {\n                  \"String\" : \"a\"\n                  },\n                \"name\" : \"name\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"In\",\n                \"name\" : \"transforms\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"Out\",\n                \"name\" : \"dummyResult\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"Out\",\n                \"name\" : \"instance\"\n                }\n              ],\n            \"definition\" : {\n              \"objectType\" : \"Func\",\n              \"metadata\" : {\n                \"uiDocUrl\" : \"http://docs.fabric-engine.com/FabricEngine/2.0.1/HTML/KLExtensionsGuide/InlineDrawing/DrawingHandle.html\",\n                \"uiTooltip\" : \"helper function to draw axes at given transforms\\n\\n Supported by DrawingHandle\"\n                },\n              \"title\" : \"DrawAxesInstances\",\n"
		+ "              \"ports\" : [\n                {\n                  \"objectType\" : \"Port\",\n                  \"nodePortType\" : \"IO\",\n                  \"name\" : \"exec\",\n                  \"execPortType\" : \"IO\",\n                  \"typeSpec\" : \"Execute\"\n                  },\n                {\n                  \"objectType\" : \"Port\",\n                  \"nodePortType\" : \"IO\",\n                  \"name\" : \"this\",\n                  \"execPortType\" : \"IO\",\n                  \"typeSpec\" : \"DrawingHandle\"\n                  },\n                {\n                  \"objectType\" : \"Port\",\n                  \"nodePortType\" : \"Out\",\n                  \"name\" : \"name\",\n                  \"execPortType\" : \"In\",\n                  \"typeSpec\" : \"String\"\n                  },\n                {\n                  \"objectType\" : \"Port\",\n                  \"metadata\" : {\n                    \"uiColor\" : \"{\\n  \\\"r\\\" : 249,\\n  \\\"g\\\" : 157,\\n  \\\"b\\\" : 28\\n  }\"\n                    },\n                  \"nodePortType\" : \"Out\",\n                  \"name\" : \"transforms\",\n"
		+ "                  \"execPortType\" : \"In\",\n                  \"typeSpec\" : \"Xfo[]\"\n                  },\n                {\n                  \"objectType\" : \"Port\",\n                  \"metadata\" : {\n                    \"uiColor\" : \"{\\n  \\\"r\\\" : 255,\\n  \\\"g\\\" : 242,\\n  \\\"b\\\" : 0\\n  }\"\n                    },\n                  \"nodePortType\" : \"In\",\n                  \"name\" : \"dummyResult\",\n                  \"execPortType\" : \"Out\",\n                  \"typeSpec\" : \"Vec3\"\n                  },\n                {\n                  \"objectType\" : \"Port\",\n                  \"nodePortType\" : \"In\",\n                  \"name\" : \"instance\",\n                  \"execPortType\" : \"Out\",\n                  \"typeSpec\" : \"InlineInstance\"\n                  }\n                ],\n              \"extDeps\" : {\n                \"InlineDrawing\" : \"*\",\n                \"FabricInterfaces\" : \"*\"\n                },\n              \"origPresetGUID\" : \"A2DAC55CB1CE7426981A13F213257B7A\",\n              \"code\" : \"require InlineDrawing;\n\ndfgEntry {\n  this.drawAxesInstances(name, transforms, dummyResult, instance);\n"
		+ "}\n\"\n              }\n            },\n          {\n            \"objectType\" : \"Inst\",\n            \"metadata\" : {\n              \"uiGraphPos\" : \"{\\\"x\\\":529.696,\\\"y\\\":492.658}\",\n              \"uiNodeColor\" : \"{\\n  \\\"r\\\" : 121,\\n  \\\"g\\\" : 134,\\n  \\\"b\\\" : 143\\n  }\",\n              \"uiTextColor\" : \"{\\n  \\\"r\\\" : 20,\\n  \\\"g\\\" : 20,\\n  \\\"b\\\" : 20\\n  }\",\n              \"uiCollapsedState\" : \"0\"\n              },\n            \"name\" : \"createXfosOnZSpline\",\n            \"ports\" : [\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"In\",\n                \"name\" : \"this\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"Out\",\n                \"name\" : \"result\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"In\",\n                \"defaultValues\" : {\n                  \"Float32\" : 0\n                  },\n                \"name\" : \"keepCurveLen\"\n                },\n              {\n"
		+ "                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"In\",\n                \"defaultValues\" : {\n                  \"Float32\" : 1\n                  },\n                \"name\" : \"keepArcLen\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"Out\",\n                \"name\" : \"medianXfos\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"In\",\n                \"name\" : \"referenceCurve\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"In\",\n                \"defaultValues\" : {\n                  \"Float32\" : 1\n                  },\n                \"name\" : \"compressionAmt\"\n                }\n              ],\n            \"definition\" : {\n              \"objectType\" : \"Func\",\n              \"metadata\" : {\n                \"uiTextColor\" : \"{\\n  \\\"r\\\" : 20,\\n  \\\"g\\\" : 20,\\n  \\\"b\\\" : 20\\n  }\",\n                \"uiNodeColor\" : \"{\\n  \\\"r\\\" : 121,\\n  \\\"g\\\" : 134,\\n  \\\"b\\\" : 143\\n  }\"\n"
		+ "                },\n              \"title\" : \"createXfosOnZSplineSegments\",\n              \"ports\" : [\n                {\n                  \"objectType\" : \"Port\",\n                  \"nodePortType\" : \"Out\",\n                  \"name\" : \"this\",\n                  \"execPortType\" : \"In\",\n                  \"typeSpec\" : \"ZSpline\"\n                  },\n                {\n                  \"objectType\" : \"Port\",\n                  \"nodePortType\" : \"In\",\n                  \"name\" : \"result\",\n                  \"execPortType\" : \"Out\",\n                  \"typeSpec\" : \"Xfo[]\"\n                  },\n                {\n                  \"objectType\" : \"Port\",\n                  \"nodePortType\" : \"Out\",\n                  \"defaultValues\" : {\n                    \"Float32\" : 0\n                    },\n                  \"name\" : \"keepCurveLen\",\n                  \"execPortType\" : \"In\",\n                  \"typeSpec\" : \"Scalar\"\n                  },\n                {\n                  \"objectType\" : \"Port\",\n                  \"nodePortType\" : \"Out\",\n                  \"defaultValues\" : {\n"
		+ "                    \"Float32\" : 1\n                    },\n                  \"name\" : \"keepArcLen\",\n                  \"execPortType\" : \"In\",\n                  \"typeSpec\" : \"Scalar\"\n                  },\n                {\n                  \"objectType\" : \"Port\",\n                  \"nodePortType\" : \"In\",\n                  \"name\" : \"medianXfos\",\n                  \"execPortType\" : \"Out\",\n                  \"typeSpec\" : \"Xfo[]\"\n                  },\n                {\n                  \"objectType\" : \"Port\",\n                  \"nodePortType\" : \"Out\",\n                  \"name\" : \"referenceCurve\",\n                  \"execPortType\" : \"In\",\n                  \"typeSpec\" : \"ZSpline\"\n                  },\n                {\n                  \"objectType\" : \"Port\",\n                  \"nodePortType\" : \"Out\",\n                  \"name\" : \"compressionAmt\",\n                  \"execPortType\" : \"In\",\n                  \"typeSpec\" : \"Scalar\"\n                  }\n                ],\n              \"extDeps\" : {\n                \"Math\" : \"*\"\n                },\n"
		+ "              \"origPresetGUID\" : \"9A8AFEEBF71811F541C71B0877BDF45B\",\n              \"code\" : \"dfgEntry {\n  result.resize(0);\n  for(UInt32 n=0;n<this.BSplines.size();n++){\n    for(UInt32 k=0; k<this.BSplines[n].defSegs; k++) {\n        Scalar t =  Scalar(k)/ Scalar(Math_max(1,(this.BSplines[n].defSegs-1)));\n        Vec3 scale = this.BSplines[n].evalScale(t,0,keepCurveLen);\n        if(compressionAmt>0) {\n          Scalar compression = this.BSplines[n].evalCompression(t, referenceCurve.BSplines[n]);\n          scale = scale*compression.linearInterpolate(1,1-compressionAmt);\n        }\n        \n        Xfo outXfo = Xfo(\n                this.BSplines[n].evalPosition(t,keepArcLen,keepCurveLen),\n                this.BSplines[n].evalOri(t,keepArcLen,keepCurveLen),\n                scale);\n        result.push(outXfo);\n        \n        // export on mid segments\n        if(k==0 && n!=0) {\n            medianXfos.push(outXfo.linearInterpolate(result[result.size()-2], 0.5));\n           // ToDo Export defrobulated Euler Angles on segment Joints\n"
		+ "        }\n    }\n  }\n}  \"\n              }\n            },\n          {\n            \"objectType\" : \"Inst\",\n            \"metadata\" : {\n              \"uiGraphPos\" : \"{\\\"x\\\":1235.3,\\\"y\\\":324.887}\"\n              },\n            \"name\" : \"Add_1\",\n            \"ports\" : [\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"In\",\n                \"name\" : \"lhs\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"In\",\n                \"name\" : \"rhs\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"Out\",\n                \"name\" : \"result\"\n                }\n              ],\n            \"executable\" : \"Fabric.Core.Math.Add\",\n            \"presetGUID\" : \"8146B3E77857E24CAE33F8B5284585E7\"\n            },\n          {\n            \"objectType\" : \"Inst\",\n            \"metadata\" : {\n              \"uiGraphPos\" : \"{\\\"x\\\":852.37,\\\"y\\\":655.962}\"\n              },\n            \"name\" : \"convertXfoToMat44\",\n"
		+ "            \"ports\" : [\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"In\",\n                \"name\" : \"xfoArray\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"Out\",\n                \"name\" : \"mat44Array\"\n                }\n              ],\n            \"definition\" : {\n              \"objectType\" : \"Func\",\n              \"title\" : \"convertXfoToMat44\",\n              \"ports\" : [\n                {\n                  \"objectType\" : \"Port\",\n                  \"nodePortType\" : \"Out\",\n                  \"name\" : \"xfoArray\",\n                  \"execPortType\" : \"In\",\n                  \"typeSpec\" : \"Xfo[]\"\n                  },\n                {\n                  \"objectType\" : \"Port\",\n                  \"nodePortType\" : \"In\",\n                  \"name\" : \"mat44Array\",\n                  \"execPortType\" : \"Out\",\n                  \"typeSpec\" : \"Mat44[]\"\n                  }\n                ],\n              \"extDeps\" : {},\n              \"code\" : \"dfgEntry {\n"
		+ "  for(UInt32 i=0;i<xfoArray.size();i++)\n  {\n    mat44Array.push(xfoArray[i].toMat44());\n  }\n}\n\"\n              }\n            },\n          {\n            \"objectType\" : \"Inst\",\n            \"metadata\" : {\n              \"uiGraphPos\" : \"{\\\"x\\\":847.92,\\\"y\\\":576.005}\"\n              },\n            \"name\" : \"convertXfoToMat44_2\",\n            \"ports\" : [\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"In\",\n                \"name\" : \"xfoArray\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"Out\",\n                \"name\" : \"mat44Array\"\n                }\n              ],\n            \"definition\" : {\n              \"objectType\" : \"Func\",\n              \"title\" : \"convertXfoToMat44\",\n              \"ports\" : [\n                {\n                  \"objectType\" : \"Port\",\n                  \"nodePortType\" : \"Out\",\n                  \"name\" : \"xfoArray\",\n                  \"execPortType\" : \"In\",\n                  \"typeSpec\" : \"Xfo[]\"\n"
		+ "                  },\n                {\n                  \"objectType\" : \"Port\",\n                  \"nodePortType\" : \"In\",\n                  \"name\" : \"mat44Array\",\n                  \"execPortType\" : \"Out\",\n                  \"typeSpec\" : \"Mat44[]\"\n                  }\n                ],\n              \"extDeps\" : {},\n              \"code\" : \"dfgEntry {\n  for(UInt32 i=0;i<xfoArray.size();i++)\n  {\n    mat44Array.push(xfoArray[i].toMat44());\n  }\n}\n\"\n              }\n            },\n          {\n            \"objectType\" : \"Inst\",\n            \"metadata\" : {\n              \"uiGraphPos\" : \"{\\\"x\\\":207.0,\\\"y\\\":711.0}\"\n              },\n            \"name\" : \"Convert_2\",\n            \"ports\" : [\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"Out\",\n                \"name\" : \"result\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"In\",\n                \"name\" : \"size\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n"
		+ "                \"nodePortType\" : \"In\",\n                \"name\" : \"defaultVal\"\n                }\n              ],\n            \"definition\" : {\n              \"objectType\" : \"Func\",\n              \"title\" : \"Convert[]\",\n              \"ports\" : [\n                {\n                  \"objectType\" : \"Port\",\n                  \"nodePortType\" : \"In\",\n                  \"name\" : \"result\",\n                  \"execPortType\" : \"Out\",\n                  \"typeSpec\" : \"$TYPEOUT$[]\"\n                  },\n                {\n                  \"objectType\" : \"Port\",\n                  \"nodePortType\" : \"Out\",\n                  \"name\" : \"size\",\n                  \"execPortType\" : \"In\",\n                  \"typeSpec\" : \"UInt32\"\n                  },\n                {\n                  \"objectType\" : \"Port\",\n                  \"nodePortType\" : \"Out\",\n                  \"name\" : \"defaultVal\",\n                  \"execPortType\" : \"In\",\n                  \"typeSpec\" : \"$TYPE$\"\n                  }\n                ],\n              \"extDeps\" : {},\n              \"code\" : \"dfgEntry {\n"
		+ "  result.resize(size);\n  for(UInt32 i=0;i<size;i++){\n     result[i]=defaultVal;\n  }\n}\n\"\n              }\n            },\n          {\n            \"objectType\" : \"Inst\",\n            \"metadata\" : {\n              \"uiGraphPos\" : \"{\\\"x\\\":140.0,\\\"y\\\":538.0}\"\n              },\n            \"name\" : \"Size_1\",\n            \"ports\" : [\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"In\",\n                \"name\" : \"this\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"Out\",\n                \"name\" : \"result\"\n                }\n              ],\n            \"executable\" : \"Fabric.Exts.Geometry.Func.Size\",\n            \"presetGUID\" : \"3426735D9D96DD0F52A2A961A393053A\"\n            },\n          {\n            \"objectType\" : \"Inst\",\n            \"metadata\" : {\n              \"uiGraphPos\" : \"{\\\"x\\\":56.0,\\\"y\\\":781.0}\",\n              \"uiCollapsedState\" : \"0\"\n              },\n            \"name\" : \"Convert_3\",\n            \"ports\" : [\n              {\n"
		+ "                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"Out\",\n                \"name\" : \"result\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"In\",\n                \"name\" : \"size\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"In\",\n                \"name\" : \"defaultVal\"\n                }\n              ],\n            \"definition\" : {\n              \"objectType\" : \"Func\",\n              \"title\" : \"Convert[]\",\n              \"ports\" : [\n                {\n                  \"objectType\" : \"Port\",\n                  \"nodePortType\" : \"In\",\n                  \"name\" : \"result\",\n                  \"execPortType\" : \"Out\",\n                  \"typeSpec\" : \"$TYPEOUT$[]\"\n                  },\n                {\n                  \"objectType\" : \"Port\",\n                  \"nodePortType\" : \"Out\",\n                  \"name\" : \"size\",\n                  \"execPortType\" : \"In\",\n                  \"typeSpec\" : \"UInt32\"\n"
		+ "                  },\n                {\n                  \"objectType\" : \"Port\",\n                  \"nodePortType\" : \"Out\",\n                  \"name\" : \"defaultVal\",\n                  \"execPortType\" : \"In\",\n                  \"typeSpec\" : \"$TYPE$\"\n                  }\n                ],\n              \"extDeps\" : {},\n              \"code\" : \"dfgEntry {\n  result.resize(size);\n  for(UInt32 i=0;i<size;i++){\n     result[i]=defaultVal;\n  }\n}\n\"\n              }\n            },\n          {\n            \"objectType\" : \"Inst\",\n            \"metadata\" : {\n              \"uiGraphPos\" : \"{\\\"x\\\":69.0,\\\"y\\\":655.0}\",\n              \"uiCollapsedState\" : \"0\"\n              },\n            \"name\" : \"Size_2\",\n            \"ports\" : [\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"In\",\n                \"name\" : \"this\"\n                },\n              {\n                \"objectType\" : \"InstPort\",\n                \"nodePortType\" : \"Out\",\n                \"name\" : \"result\"\n                }\n              ],\n"
		+ "            \"executable\" : \"Fabric.Exts.Geometry.Func.Size\",\n            \"presetGUID\" : \"3426735D9D96DD0F52A2A961A393053A\"\n            }\n          ],\n        \"connections\" : {\n          \"pelvis\" : [\n            \"assemble.pelvis\"\n            ],\n          \"torso\" : [\n            \"assemble.torso\"\n            ],\n          \"chest\" : [\n            \"assemble.chest\"\n            ],\n          \"upChest\" : [\n            \"assemble.upchest\"\n            ],\n          \"neck\" : [\n            \"assemble.neck\"\n            ],\n          \"numDeformers\" : [\n            \"Convert_2.defaultVal\"\n            ],\n          \"referenceCurve\" : [\n            \"createXfosOnZSpline.referenceCurve\"\n            ],\n          \"defaultVal\" : [\n            \"Convert_3.defaultVal\"\n            ],\n          \"assemble.result\" : [\n            \"buildZSpline.mat44s\",\n            \"Size_1.this\",\n            \"Size_2.this\"\n            ],\n          \"GetEmptyDebugShape2.result\" : [\n            \"DrawCurve.this\"\n            ],\n          \"EmptyDrawingHandle.handle\" : [\n"
		+ "            \"GetEmptyDebugShape2.this\",\n            \"DrawAxesInstances.this\"\n            ],\n          \"CreateSegs.result\" : [\n            \"DrawCurve.points\"\n            ],\n          \"CreateSegs.color\" : [\n            \"DrawCurve.color\"\n            ],\n          \"DrawCurve.dummyResult\" : [\n            \"Add_1.lhs\"\n            ],\n          \"buildZSpline.result\" : [\n            \"createXfosOnZSpline.this\",\n            \"CreateSegs.this\"\n            ],\n          \"DrawAxesInstances.dummyResult\" : [\n            \"Add_1.rhs\"\n            ],\n          \"createXfosOnZSpline.result\" : [\n            \"convertXfoToMat44_2.xfoArray\",\n            \"DrawAxesInstances.transforms\"\n            ],\n          \"createXfosOnZSpline.medianXfos\" : [\n            \"convertXfoToMat44.xfoArray\"\n            ],\n          \"Add_1.result\" : [\n            \"result\"\n            ],\n          \"convertXfoToMat44_2.mat44Array\" : [\n            \"outputs\"\n            ],\n          \"Convert_2.result\" : [\n            \"buildZSpline.defSegs\"\n            ],\n          \"Size_1.result\" : [\n"
		+ "            \"Convert_2.size\"\n            ],\n          \"Convert_3.result\" : [\n            \"buildZSpline.resolution\"\n            ],\n          \"Size_2.result\" : [\n            \"Convert_3.size\"\n            ]\n          }\n        }\n      },\n    {\n      \"objectType\" : \"Inst\",\n      \"metadata\" : {\n        \"uiGraphPos\" : \"{\\\"x\\\":-93.9573,\\\"y\\\":569.115}\"\n        },\n      \"name\" : \"assemble\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"pelvis\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"torso\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"chest\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"upchest\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"neck\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n"
		+ "          \"nodePortType\" : \"Out\",\n          \"name\" : \"result\"\n          }\n        ],\n      \"definition\" : {\n        \"objectType\" : \"Func\",\n        \"metadata\" : {\n          \"uiTextColor\" : \"{\\n  \\\"r\\\" : 20,\\n  \\\"g\\\" : 20,\\n  \\\"b\\\" : 20\\n  }\",\n          \"uiNodeColor\" : \"{\\n  \\\"r\\\" : 121,\\n  \\\"g\\\" : 134,\\n  \\\"b\\\" : 143\\n  }\"\n          },\n        \"title\" : \"asseble\",\n        \"ports\" : [\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"Out\",\n            \"name\" : \"pelvis\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"Mat44\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"Out\",\n            \"name\" : \"torso\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"Mat44\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"Out\",\n            \"name\" : \"chest\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"Mat44\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"Out\",\n"
		+ "            \"name\" : \"upchest\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"Mat44\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"Out\",\n            \"name\" : \"neck\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"Mat44\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"In\",\n            \"name\" : \"result\",\n            \"execPortType\" : \"Out\",\n            \"typeSpec\" : \"Mat44[]\"\n            }\n          ],\n        \"extDeps\" : {},\n        \"code\" : \"dfgEntry {\n  result.push(pelvis);\n  result.push(torso);\n  result.push(chest);\n  result.push(upchest);\n  result.push(neck);\n}\n\"\n        }\n      },\n    {\n      \"objectType\" : \"Inst\",\n      \"metadata\" : {\n        \"uiGraphPos\" : \"{\\\"x\\\":302.23,\\\"y\\\":653.829}\"\n        },\n      \"name\" : \"buildZSpline\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"mat44s\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n"
		+ "          \"nodePortType\" : \"Out\",\n          \"name\" : \"result\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"isSegmentStart\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"clamped\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"weights\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"resolution\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"order\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"closed\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"defSegs\"\n          }\n        ],\n      \"executable\" : \"OSS.Exts.Curves.ZSpline.ZSpline\",\n      \"presetGUID\" : \"1A4FC39528C5CC9C3EF2B16480BD4E7B\"\n"
		+ "      },\n    {\n      \"objectType\" : \"Inst\",\n      \"metadata\" : {\n        \"uiGraphPos\" : \"{\\\"x\\\":639.826,\\\"y\\\":529.292}\",\n        \"uiCollapsedState\" : \"0\"\n        },\n      \"name\" : \"CreateSegs\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"result\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"this\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"color\"\n          }\n        ],\n      \"executable\" : \"OSS.Exts.Curves.ZSpline.createSegsOnZSpline\",\n      \"presetGUID\" : \"D8E844DE0169A7D9BB304C9F8DDF30A2\"\n      },\n    {\n      \"objectType\" : \"Inst\",\n      \"metadata\" : {\n        \"uiGraphPos\" : \"{\\\"x\\\":890.153,\\\"y\\\":548.289}\",\n        \"uiNodeColor\" : \"{\\n  \\\"r\\\" : 121,\\n  \\\"g\\\" : 134,\\n  \\\"b\\\" : 143\\n  }\",\n        \"uiTextColor\" : \"{\\n  \\\"r\\\" : 20,\\n  \\\"g\\\" : 20,\\n  \\\"b\\\" : 20\\n  }\",\n        \"uiCollapsedState\" : \"0\"\n        },\n"
		+ "      \"name\" : \"DrawCurve\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"points\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"color\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"result\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"this\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"dummyResult\"\n          }\n        ],\n      \"executable\" : \"OSS.Exts.Curves.ZSpline.drawCurve\",\n      \"presetGUID\" : \"B3D1DFFCE15CC7040DCD73D99F2C3098\"\n      },\n    {\n      \"objectType\" : \"Inst\",\n      \"metadata\" : {\n        \"uiGraphPos\" : \"{\\\"x\\\":630.686,\\\"y\\\":623.018}\"\n        },\n      \"name\" : \"GetEmptyDebugShape2\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"IO\",\n"
		+ "          \"name\" : \"exec\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"this\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"name\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"result\"\n          }\n        ],\n      \"executable\" : \"Fabric.Exts.InlineDrawing.DrawingHandle.GetEmptyDebugShape\",\n      \"presetGUID\" : \"DB3916AA2CE58EEAFAEDB9E2653EF4D6\"\n      },\n    {\n      \"objectType\" : \"Inst\",\n      \"metadata\" : {\n        \"uiGraphPos\" : \"{\\\"x\\\":638.143,\\\"y\\\":760.701}\"\n        },\n      \"name\" : \"EmptyDrawingHandle\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"handle\"\n          }\n        ],\n      \"executable\" : \"Fabric.Exts.InlineDrawing.DrawingHandle.EmptyDrawingHandle\",\n      \"presetGUID\" : \"2440020BA6A1CAB1CEB690A198F99C70\"\n      },\n    {\n      \"objectType\" : \"Inst\",\n"
		+ "      \"metadata\" : {\n        \"uiGraphPos\" : \"{\\\"x\\\":-1.0,\\\"y\\\":841.5}\",\n        \"uiCollapsedState\" : \"0\"\n        },\n      \"name\" : \"Convert_3\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"result\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"size\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"defaultVal\"\n          }\n        ],\n      \"definition\" : {\n        \"objectType\" : \"Func\",\n        \"title\" : \"Convert[]\",\n        \"ports\" : [\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"In\",\n            \"name\" : \"result\",\n            \"execPortType\" : \"Out\",\n            \"typeSpec\" : \"$TYPEOUT$[]\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"Out\",\n            \"name\" : \"size\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"UInt32\"\n"
		+ "            },\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"Out\",\n            \"name\" : \"defaultVal\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"$TYPE$\"\n            }\n          ],\n        \"extDeps\" : {},\n        \"code\" : \"dfgEntry {\n  result.resize(size);\n  for(UInt32 i=0;i<size;i++){\n     result[i]=defaultVal;\n  }\n}\n\"\n        }\n      },\n    {\n      \"objectType\" : \"Inst\",\n      \"metadata\" : {\n        \"uiGraphPos\" : \"{\\\"x\\\":19.0,\\\"y\\\":734.5}\",\n        \"uiCollapsedState\" : \"0\"\n        },\n      \"name\" : \"Size_2\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"this\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"result\"\n          }\n        ],\n      \"executable\" : \"Fabric.Exts.Geometry.Func.Size\",\n      \"presetGUID\" : \"3426735D9D96DD0F52A2A961A393053A\"\n      },\n    {\n      \"objectType\" : \"Inst\",\n      \"metadata\" : {\n        \"uiGraphPos\" : \"{\\\"x\\\":-196.0,\\\"y\\\":770.406}\"\n"
		+ "        },\n      \"name\" : \"Scalar_1\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"defaultValues\" : {\n            \"Float32\" : 50\n            },\n          \"name\" : \"value\"\n          }\n        ],\n      \"executable\" : \"Fabric.Core.Constants.Scalar\",\n      \"presetGUID\" : \"E0E96C6E234F70063BC98887B83327DC\"\n      }\n    ],\n  \"connections\" : {\n    \"pelvis\" : [\n      \"ZSplineSpineSolver_1.pelvis\"\n      ],\n    \"torso\" : [\n      \"ZSplineSpineSolver_1.torso\"\n      ],\n    \"chest\" : [\n      \"ZSplineSpineSolver_1.chest\"\n      ],\n    \"upChest\" : [\n      \"ZSplineSpineSolver_1.upChest\"\n      ],\n    \"neck\" : [\n      \"ZSplineSpineSolver_1.neck\"\n      ],\n    \"rigScale\" : [\n      \"ZSplineSpineSolver_1.rigScale\"\n      ],\n    \"drawDebug\" : [\n      \"ZSplineSpineSolver_1.drawDebug\"\n      ],\n    \"numDeformers\" : [\n      \"ZSplineSpineSolver_1.numDeformers\"\n      ],\n    \"pelvisRest\" : [\n      \"assemble.pelvis\"\n      ],\n    \"torsoRest\" : [\n      \"assemble.torso\"\n      ],\n    \"chestRest\" : [\n"
		+ "      \"assemble.chest\"\n      ],\n    \"upChestRest\" : [\n      \"assemble.upchest\"\n      ],\n    \"neckRest\" : [\n      \"assemble.neck\"\n      ],\n    \"ZSplineSpineSolver_1.outputs\" : [\n      \"outputs\"\n      ],\n    \"ZSplineSpineSolver_1.result\" : [\n      \"dummyResult\"\n      ],\n    \"assemble.result\" : [\n      \"buildZSpline.mat44s\",\n      \"Size_2.this\"\n      ],\n    \"buildZSpline.result\" : [\n      \"CreateSegs.this\",\n      \"ZSplineSpineSolver_1.referenceCurve\"\n      ],\n    \"CreateSegs.result\" : [\n      \"DrawCurve.points\"\n      ],\n    \"CreateSegs.color\" : [\n      \"DrawCurve.color\"\n      ],\n    \"DrawCurve.result\" : [\n      \"result\"\n      ],\n    \"GetEmptyDebugShape2.result\" : [\n      \"DrawCurve.this\"\n      ],\n    \"EmptyDrawingHandle.handle\" : [\n      \"GetEmptyDebugShape2.this\"\n      ],\n    \"Convert_3.result\" : [\n      \"buildZSpline.resolution\"\n      ],\n    \"Size_2.result\" : [\n      \"Convert_3.size\"\n      ],\n    \"Scalar_1.value\" : [\n      \"Convert_3.defaultVal\",\n      \"ZSplineSpineSolver_1.defaultVal\"\n      ]\n    },\n  \"metadata\" : {\n"
		+ "    \"maya_id\" : \"1\"\n    },\n  \"requiredPresets\" : {\n    \"Fabric.Exts.InlineDrawing.DrawingHandle.GetEmptyDebugShape\" : {\n      \"objectType\" : \"Func\",\n      \"metadata\" : {\n        \"uiDocUrl\" : \"http://docs.fabric-engine.com/FabricEngine/2.0.1/HTML/KLExtensionsGuide/InlineDrawing/DrawingHandle.html\",\n        \"uiTooltip\" : \"helper function to clear a debug drawing shape\\n\\n Supported by DrawingHandle\"\n        },\n      \"title\" : \"GetEmptyDebugShape\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"exec\",\n          \"execPortType\" : \"IO\",\n          \"typeSpec\" : \"Execute\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"this\",\n          \"execPortType\" : \"IO\",\n          \"typeSpec\" : \"DrawingHandle\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"Out\",\n          \"defaultValues\" : {\n            \"String\" : \"debug\"\n            },\n          \"name\" : \"name\",\n          \"execPortType\" : \"In\",\n"
		+ "          \"typeSpec\" : \"String\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"result\",\n          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"InlineDebugShape\"\n          }\n        ],\n      \"extDeps\" : {\n        \"InlineDrawing\" : \"*\",\n        \"FabricInterfaces\" : \"*\"\n        },\n      \"presetGUID\" : \"DB3916AA2CE58EEAFAEDB9E2653EF4D6\",\n      \"code\" : \"require InlineDrawing;\n\ndfgEntry {\n  result = this.getEmptyDebugShape(name);\n}\n\"\n      },\n    \"Fabric.Exts.InlineDrawing.DrawingHandle.EmptyDrawingHandle\" : {\n      \"objectType\" : \"Graph\",\n      \"title\" : \"EmptyDrawingHandle\",\n      \"cacheRule\" : \"never\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"handle\",\n          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"DrawingHandle\"\n          }\n        ],\n      \"extDeps\" : {},\n      \"presetGUID\" : \"2440020BA6A1CAB1CEB690A198F99C70\",\n      \"nodes\" : [\n        {\n          \"objectType\" : \"Inst\",\n"
		+ "          \"metadata\" : {\n            \"uiGraphPos\" : \"{\\\"x\\\": 894, \\\"y\\\": 100}\"\n            },\n          \"name\" : \"Clear\",\n          \"ports\" : [\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"IO\",\n              \"name\" : \"this\"\n              }\n            ],\n          \"executable\" : \"Fabric.Exts.InlineDrawing.DrawingHandle.Clear\",\n          \"cacheRule\" : \"never\"\n          },\n        {\n          \"objectType\" : \"Var\",\n          \"metadata\" : {\n            \"uiGraphPos\" : \"{\\\"x\\\":567.0,\\\"y\\\":56.0}\",\n            \"uiCollapsedState\" : \"0\"\n            },\n          \"name\" : \"handleVar\",\n          \"ports\" : [\n            {\n              \"objectType\" : \"VarPort\",\n              \"nodePortType\" : \"IO\",\n              \"name\" : \"value\"\n              }\n            ],\n          \"dataType\" : \"DrawingHandle\",\n          \"extDep\" : \"InlineDrawing:*\"\n          },\n        {\n          \"objectType\" : \"Inst\",\n          \"metadata\" : {\n            \"uiGraphPos\" : \"{\\\"x\\\":287.0,\\\"y\\\":56.0}\"\n            },\n"
		+ "          \"name\" : \"CreateDrawingHandle\",\n          \"ports\" : [\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"Out\",\n              \"name\" : \"handle\"\n              }\n            ],\n          \"definition\" : {\n            \"objectType\" : \"Func\",\n            \"title\" : \"Create DrawingHandle\",\n            \"ports\" : [\n              {\n                \"objectType\" : \"Port\",\n                \"nodePortType\" : \"In\",\n                \"name\" : \"handle\",\n                \"execPortType\" : \"Out\",\n                \"typeSpec\" : \"DrawingHandle\"\n                }\n              ],\n            \"extDeps\" : {\n              \"InlineDrawing\" : \"*\"\n              },\n            \"code\" : \"dfgEntry {\n  handle = DrawingHandle();\n}\n\"\n            }\n          }\n        ],\n      \"connections\" : {\n        \"Clear.this\" : [\n          \"handle\"\n          ],\n        \"handleVar.value\" : [\n          \"Clear.this\"\n          ],\n        \"CreateDrawingHandle.handle\" : [\n          \"handleVar.value\"\n          ]\n        }\n      },\n"
		+ "    \"Fabric.Exts.InlineDrawing.DrawingHandle.Clear\" : {\n      \"objectType\" : \"Func\",\n      \"metadata\" : {\n        \"uiDocUrl\" : \"http://docs.fabric-engine.com/FabricEngine/2.0.0-beta/HTML/KLExtensionsGuide/InlineDrawing/DrawingHandle.html\",\n        \"uiTooltip\" : \"removes all contents from the DrawingHandle\\n\\n Supported by DrawingHandle\"\n        },\n      \"title\" : \"Clear\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"this\",\n          \"execPortType\" : \"IO\",\n          \"typeSpec\" : \"DrawingHandle\"\n          }\n        ],\n      \"extDeps\" : {\n        \"InlineDrawing\" : \"*\"\n        },\n      \"code\" : \"require InlineDrawing;\n\ndfgEntry {\n  this.clear();\n}\n\"\n      },\n    \"OSS.Exts.Curves.ZSpline.createSegsOnZSpline\" : {\n      \"objectType\" : \"Func\",\n      \"title\" : \"createSegsOnZSpline\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"result\",\n          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"Vec3[]\"\n"
		+ "          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"this\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"ZSpline\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"color\",\n          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"Color[]\"\n          }\n        ],\n      \"extDeps\" : {\n        \"Math\" : \"*\"\n        },\n      \"presetGUID\" : \"D8E844DE0169A7D9BB304C9F8DDF30A2\",\n      \"code\" : \"dfgEntry {\n  result.resize(0);\n  color.resize(0);\n  for(UInt32 n=0;n<this.BSplines.size();n++){\n    BSpline b = this.BSplines[n];\n    UInt32 resolution = b.resolution;\n    \n    // Color Settings\n    Scalar hue = mathRandomScalar(n,1);\n    Scalar saturation = 2;\n    \n    for(UInt32 k=0; k<=resolution; k++) {\n      Scalar t =  Scalar(k)/(resolution);\n      t = (t+n)/(this.BSplines.size());\n      Color c = randomColor(hue*180,saturation,this.normalizeT(t));\n      result.push(this.evalPosition(t));\n      color.push(c);\n"
		+ "    }\n  }\n}\n\"\n      },\n    \"OSS.Exts.Curves.ZSpline.drawCurve\" : {\n      \"objectType\" : \"Func\",\n      \"metadata\" : {\n        \"uiTextColor\" : \"{\\n  \\\"r\\\" : 20,\\n  \\\"g\\\" : 20,\\n  \\\"b\\\" : 20\\n  }\",\n        \"uiNodeColor\" : \"{\\n  \\\"r\\\" : 121,\\n  \\\"g\\\" : 134,\\n  \\\"b\\\" : 143\\n  }\"\n        },\n      \"title\" : \"drawCurve\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"points\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Vec3[]\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"color\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Color[]\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"result\",\n          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"InlineDebugShape\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"this\",\n          \"execPortType\" : \"IO\",\n"
		+ "          \"typeSpec\" : \"InlineDebugShape\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"dummyResult\",\n          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"Vec3\"\n          }\n        ],\n      \"extDeps\" : {},\n      \"presetGUID\" : \"B3D1DFFCE15CC7040DCD73D99F2C3098\",\n      \"code\" : \"dfgEntry {\n  Index firstIndex = this.allocateLines(points.size(), points.size()-1);\n  Index colorIndex = firstIndex;\n  Vec3Attribute positionsAttr = this.attributes.getOrCreateAttribute('positions', Vec3Attribute);\n  Vec3Attribute normalsAttr = this.attributes.getOrCreateAttribute('normals', Vec3Attribute);\n  ColorAttribute vertexColorsAttr = this.attributes.getOrCreateColorAttribute('vertexColors');\n  \n\n  for( Integer i=0; i<points.size(); i++){\n    vertexColorsAttr.values[firstIndex] = color[i];\n    positionsAttr.values[firstIndex] = points[i];\n    normalsAttr.values[firstIndex++] = this.defaultNormal;\n    if(i > 0){\n      this.linesIndices[this.linesIndicesOffset++] = firstIndex - 2;\n"
		+ "      this.linesIndices[this.linesIndicesOffset++] = firstIndex - 1;\n    }\n  }\n\n  positionsAttr.incrementVersion();\n  normalsAttr.incrementVersion();\n  vertexColorsAttr.incrementVersion();\n\n  result = this;\n}\n\"\n      },\n    \"OSS.Exts.Curves.ZSpline.ZSpline\" : {\n      \"objectType\" : \"Func\",\n      \"metadata\" : {\n        \"uiTextColor\" : \"{\\n  \\\"r\\\" : 20,\\n  \\\"g\\\" : 20,\\n  \\\"b\\\" : 20\\n  }\",\n        \"uiNodeColor\" : \"{\\n  \\\"r\\\" : 121,\\n  \\\"g\\\" : 134,\\n  \\\"b\\\" : 143\\n  }\"\n        },\n      \"title\" : \"ZSpline\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"mat44s\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Mat44[]\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"result\",\n          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"ZSpline\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"isSegmentStart\",\n          \"execPortType\" : \"IO\",\n"
		+ "          \"typeSpec\" : \"Boolean[]\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"clamped\",\n          \"execPortType\" : \"IO\",\n          \"typeSpec\" : \"Boolean[]\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"weights\",\n          \"execPortType\" : \"IO\",\n          \"typeSpec\" : \"Scalar[]\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"resolution\",\n          \"execPortType\" : \"IO\",\n          \"typeSpec\" : \"UInt32[]\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"order\",\n          \"execPortType\" : \"IO\",\n          \"typeSpec\" : \"UInt32[]\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"closed\",\n          \"execPortType\" : \"IO\",\n          \"typeSpec\" : \"Boolean\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"IO\",\n"
		+ "          \"name\" : \"defSegs\",\n          \"execPortType\" : \"IO\",\n          \"typeSpec\" : \"UInt32[]\"\n          }\n        ],\n      \"extDeps\" : {\n        \"Curves\" : \"*\",\n        \"Math\" : \"*\"\n        },\n      \"presetGUID\" : \"1A4FC39528C5CC9C3EF2B16480BD4E7B\",\n      \"code\" : \"dfgEntry { \n  result.buildZSpline(mat44s, isSegmentStart, weights, order, resolution, defSegs, clamped, closed);\n}\"\n      },\n    \"Fabric.Core.Math.Add\" : {\n      \"objectType\" : \"Func\",\n      \"title\" : \"Add\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"lhs\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"$TYPE$\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"rhs\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"$TYPE$\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"result\",\n          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"$TYPE$\"\n"
		+ "          }\n        ],\n      \"extDeps\" : {},\n      \"presetGUID\" : \"8146B3E77857E24CAE33F8B5284585E7\",\n      \"code\" : \"\ndfgEntry {\n\tresult = lhs + rhs;\n}\n\"\n      },\n    \"Fabric.Exts.Geometry.Func.Size\" : {\n      \"objectType\" : \"Func\",\n      \"metadata\" : {\n        \"uiDocUrl\" : \"http://docs.fabric-engine.com/FabricEngine/2.0.1/HTML/KLExtensionsGuide/Geometry/GeometryAttribute.html\",\n        \"uiTooltip\" : \"Returns the size of the attribute array.\\n\\n Supported by GeometryAttribute,GeometryAttributes,BaseAttribute,SkinningAttributeData,Points\"\n        },\n      \"title\" : \"Size\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"this\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"$TYPE$\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"result\",\n          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"Size\"\n          }\n        ],\n      \"extDeps\" : {\n        \"Geometry\" : \"*\"\n        },\n"
		+ "      \"presetGUID\" : \"3426735D9D96DD0F52A2A961A393053A\",\n      \"code\" : \"require Geometry;\n\ndfgEntry {\n  result = this.size();\n}\n\"\n      },\n    \"Fabric.Core.Constants.Scalar\" : {\n      \"objectType\" : \"Func\",\n      \"metadata\" : {\n        \"uiAlwaysShowDaisyChainPorts\" : \"true\"\n        },\n      \"title\" : \"Scalar\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"value\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Scalar\"\n          }\n        ],\n      \"extDeps\" : {},\n      \"presetGUID\" : \"E0E96C6E234F70063BC98887B83327DC\",\n      \"code\" : \"dfgEntry {\n}\n\"\n      }\n    },\n  \"args\" : [\n    {\n      \"type\" : \"Mat44\",\n      \"value\" : {\n        \"row0\" : {\n          \"x\" : 1,\n          \"y\" : 0,\n          \"z\" : 0,\n          \"t\" : 0\n          },\n        \"row1\" : {\n          \"x\" : 0,\n          \"y\" : 1,\n          \"z\" : 0,\n          \"t\" : 9\n          },\n        \"row2\" : {\n          \"x\" : 0,\n          \"y\" : 0,\n          \"z\" : 1,\n          \"t\" : 0\n          },\n"
		+ "        \"row3\" : {\n          \"x\" : 0,\n          \"y\" : 0,\n          \"z\" : 0,\n          \"t\" : 1\n          }\n        },\n      \"ext\" : \"Math\"\n      },\n    {\n      \"type\" : \"Mat44\",\n      \"value\" : {\n        \"row0\" : {\n          \"x\" : 1,\n          \"y\" : 0,\n          \"z\" : 0,\n          \"t\" : 0\n          },\n        \"row1\" : {\n          \"x\" : 0,\n          \"y\" : 1,\n          \"z\" : 0,\n          \"t\" : 10\n          },\n        \"row2\" : {\n          \"x\" : 0,\n          \"y\" : 0,\n          \"z\" : 1,\n          \"t\" : 0\n          },\n        \"row3\" : {\n          \"x\" : 0,\n          \"y\" : 0,\n          \"z\" : 0,\n          \"t\" : 1\n          }\n        },\n      \"ext\" : \"Math\"\n      },\n    {\n      \"type\" : \"Mat44\",\n      \"value\" : {\n        \"row0\" : {\n          \"x\" : 1,\n          \"y\" : 0,\n          \"z\" : 0,\n          \"t\" : 0\n          },\n        \"row1\" : {\n          \"x\" : 0,\n          \"y\" : 1,\n          \"z\" : 0,\n          \"t\" : 12\n          },\n        \"row2\" : {\n          \"x\" : 0,\n          \"y\" : 0,\n          \"z\" : 1,\n          \"t\" : 0\n          },\n"
		+ "        \"row3\" : {\n          \"x\" : 0,\n          \"y\" : 0,\n          \"z\" : 0,\n          \"t\" : 1\n          }\n        },\n      \"ext\" : \"Math\"\n      },\n    {\n      \"type\" : \"Mat44\",\n      \"value\" : {\n        \"row0\" : {\n          \"x\" : 1,\n          \"y\" : 0,\n          \"z\" : 0,\n          \"t\" : 0\n          },\n        \"row1\" : {\n          \"x\" : 0,\n          \"y\" : 1,\n          \"z\" : 0,\n          \"t\" : 14\n          },\n        \"row2\" : {\n          \"x\" : 0,\n          \"y\" : 0,\n          \"z\" : 1,\n          \"t\" : 0\n          },\n        \"row3\" : {\n          \"x\" : 0,\n          \"y\" : 0,\n          \"z\" : 0,\n          \"t\" : 1\n          }\n        },\n      \"ext\" : \"Math\"\n      },\n    {\n      \"type\" : \"Mat44\",\n      \"value\" : {\n        \"row0\" : {\n          \"x\" : 1,\n          \"y\" : 0,\n          \"z\" : 0,\n          \"t\" : 0\n          },\n        \"row1\" : {\n          \"x\" : 0,\n          \"y\" : 1,\n          \"z\" : 0,\n          \"t\" : 15\n          },\n        \"row2\" : {\n          \"x\" : 0,\n          \"y\" : 0,\n          \"z\" : 1,\n          \"t\" : 0\n          },\n"
		+ "        \"row3\" : {\n          \"x\" : 0,\n          \"y\" : 0,\n          \"z\" : 0,\n          \"t\" : 1\n          }\n        },\n      \"ext\" : \"Math\"\n      },\n    {\n      \"type\" : \"Float32\",\n      \"value\" : 1\n      },\n    {\n      \"type\" : \"Boolean\",\n      \"value\" : false\n      },\n    {\n      \"type\" : \"Mat44[]\",\n      \"value\" : null,\n      \"ext\" : \"Math\"\n      },\n    {\n      \"type\" : \"SInt32\",\n      \"value\" : 6\n      },\n    {\n      \"type\" : \"Mat44\",\n      \"value\" : {\n        \"row0\" : {\n          \"x\" : 1,\n          \"y\" : 0,\n          \"z\" : 0,\n          \"t\" : 0\n          },\n        \"row1\" : {\n          \"x\" : 0,\n          \"y\" : 1,\n          \"z\" : 0,\n          \"t\" : 9\n          },\n        \"row2\" : {\n          \"x\" : 0,\n          \"y\" : 0,\n          \"z\" : 1,\n          \"t\" : 0\n          },\n        \"row3\" : {\n          \"x\" : 0,\n          \"y\" : 0,\n          \"z\" : 0,\n          \"t\" : 1\n          }\n        },\n      \"ext\" : \"Math\"\n      },\n    {\n      \"type\" : \"Mat44\",\n      \"value\" : {\n        \"row0\" : {\n          \"x\" : 1,\n          \"y\" : 0,\n"
		+ "          \"z\" : 0,\n          \"t\" : 0\n          },\n        \"row1\" : {\n          \"x\" : 0,\n          \"y\" : 1,\n          \"z\" : 0,\n          \"t\" : 10\n          },\n        \"row2\" : {\n          \"x\" : 0,\n          \"y\" : 0,\n          \"z\" : 1,\n          \"t\" : 0\n          },\n        \"row3\" : {\n          \"x\" : 0,\n          \"y\" : 0,\n          \"z\" : 0,\n          \"t\" : 1\n          }\n        },\n      \"ext\" : \"Math\"\n      },\n    {\n      \"type\" : \"Mat44\",\n      \"value\" : {\n        \"row0\" : {\n          \"x\" : 1,\n          \"y\" : 0,\n          \"z\" : 0,\n          \"t\" : 0\n          },\n        \"row1\" : {\n          \"x\" : 0,\n          \"y\" : 1,\n          \"z\" : 0,\n          \"t\" : 12\n          },\n        \"row2\" : {\n          \"x\" : 0,\n          \"y\" : 0,\n          \"z\" : 1,\n          \"t\" : 0\n          },\n        \"row3\" : {\n          \"x\" : 0,\n          \"y\" : 0,\n          \"z\" : 0,\n          \"t\" : 1\n          }\n        },\n      \"ext\" : \"Math\"\n      },\n    {\n      \"type\" : \"Mat44\",\n      \"value\" : {\n        \"row0\" : {\n          \"x\" : 1,\n          \"y\" : 0,\n"
		+ "          \"z\" : 0,\n          \"t\" : 0\n          },\n        \"row1\" : {\n          \"x\" : 0,\n          \"y\" : 1,\n          \"z\" : 0,\n          \"t\" : 14\n          },\n        \"row2\" : {\n          \"x\" : 0,\n          \"y\" : 0,\n          \"z\" : 1,\n          \"t\" : 0\n          },\n        \"row3\" : {\n          \"x\" : 0,\n          \"y\" : 0,\n          \"z\" : 0,\n          \"t\" : 1\n          }\n        },\n      \"ext\" : \"Math\"\n      },\n    {\n      \"type\" : \"Mat44\",\n      \"value\" : null,\n      \"ext\" : \"Math\"\n      },\n    {\n      \"type\" : \"Vec3\",\n      \"value\" : null,\n      \"ext\" : \"Math\"\n      },\n    {\n      \"type\" : \"InlineDebugShape\",\n      \"value\" : null,\n      \"ext\" : \"InlineDrawing\"\n      },\n    {\n      \"type\" : \"SInt32\",\n      \"value\" : 0\n      }\n    ]\n  }");
	setAttr ".evalID" 910;
	setAttr -k on ".pelvis" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 9 0 1;
	setAttr -k on ".torso" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 10 0 1;
	setAttr -k on ".chest" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 12 0 1;
	setAttr -k on ".upChest" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 14 0 1;
	setAttr -k on ".neck" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 15 0 1;
	setAttr -k on ".rigScale" 1;
	setAttr -k on ".drawDebug" no;
	setAttr -s 6 ".outputs";
	setAttr -k on ".numDeformers" 6;
	setAttr -k on ".pelvisRest" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 9 0 1;
	setAttr -k on ".torsoRest" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 10 0 1;
	setAttr -k on ".chestRest" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 12 0 1;
	setAttr -k on ".upChestRest" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 14 0 1;
	setAttr -k on ".neckRest" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 15 0 1;
	setAttr -k on ".defSegs" 0;
createNode decomposeMatrix -n "decomposeMatrix1";
	rename -uid "7F5E2CF7-4759-36DE-2554-B59B33FCECB5";
	setAttr ".ot" -type "double3" 0 9 0 ;
	setAttr ".or" -type "double3" 180 0 90.000006830188354 ;
	setAttr ".os" -type "double3" 1.0000001192092967 1.0000001192092682 1.0000002384185791 ;
createNode decomposeMatrix -n "decomposeMatrix2";
	rename -uid "ADD16E9D-45CC-A765-694A-E98DCCCEDBD6";
	setAttr ".ot" -type "double3" 0 10.200000762939453 0 ;
	setAttr ".or" -type "double3" 180 0 90.000006830188354 ;
	setAttr ".os" -type "double3" 1.0000001192092967 1.0000001192092682 1.0000002384185791 ;
	setAttr ".oqx" 0.70710673903970278;
	setAttr ".oqy" 0.70710682333338981;
	setAttr ".oqz" 4.3297805392524438e-017;
	setAttr ".oqw" 4.3297800231024742e-017;
createNode decomposeMatrix -n "decomposeMatrix3";
	rename -uid "B281AEA0-4886-BB80-9D59-EB802361818B";
	setAttr ".ot" -type "double3" 0 11.399999618530273 0 ;
	setAttr ".or" -type "double3" 180 0 90.000006830188354 ;
	setAttr ".os" -type "double3" 1.0000001192092967 1.0000001192092682 1.0000002384185791 ;
createNode decomposeMatrix -n "decomposeMatrix4";
	rename -uid "C084CE2B-4193-D8AF-AF72-E1BA16710151";
	setAttr ".ot" -type "double3" 0 12.600000381469727 0 ;
	setAttr ".or" -type "double3" 180 0 90.000006830188354 ;
	setAttr ".os" -type "double3" 1.0000001192092967 1.0000001192092682 1.0000002384185791 ;
createNode decomposeMatrix -n "decomposeMatrix5";
	rename -uid "2011A7B3-4476-2072-E596-A28672B24333";
	setAttr ".ot" -type "double3" 0 13.799999237060547 0 ;
	setAttr ".or" -type "double3" 180 0 90.000006830188354 ;
	setAttr ".os" -type "double3" 1.0000001192092967 1.0000001192092682 1.0000002384185791 ;
	setAttr ".osh" -type "double3" -2.3841855067985985e-007 0 0 ;
	setAttr ".oqx" 0.70710673903970278;
	setAttr ".oqy" 0.70710682333338981;
	setAttr ".oqz" 4.3297805392524438e-017;
	setAttr ".oqw" 4.3297800231024742e-017;
createNode decomposeMatrix -n "decomposeMatrix6";
	rename -uid "CAB43E0F-4E88-3F45-39D1-D591F6AF041B";
	setAttr ".ot" -type "double3" 0 15 0 ;
	setAttr ".or" -type "double3" 180 0 90.000006830188354 ;
	setAttr ".os" -type "double3" 1.0000001192092967 1.0000001192092682 1.0000002384185791 ;
createNode dfgMayaNode -n "spineDeformerKLOp";
	rename -uid "E46702CC-4621-0DA5-E92C-BFB52ED83771";
	addAttr -r false -ci true -k true -sn "drawDebug" -ln "drawDebug" -min 0 -max 1 
		-at "bool";
	addAttr -r false -ci true -k true -sn "rigScale" -ln "rigScale" -at "double";
	addAttr -r false -ci true -k true -m -sn "constrainers" -ln "constrainers" -at "matrix";
	addAttr -w false -s false -ci true -m -sn "constrainees" -ln "constrainees" -at "matrix";
	setAttr ".cch" no;
	setAttr ".ihi" 2;
	setAttr ".nds" 0;
	setAttr ".fzn" no;
	setAttr ".svd" -type "string" (
		"{\n  \"objectType\" : \"Graph\",\n  \"metadata\" : {\n    \"maya_id\" : \"2\"\n    },\n  \"title\" : \"\",\n  \"ports\" : [\n    {\n      \"objectType\" : \"Port\",\n      \"nodePortType\" : \"IO\",\n      \"name\" : \"solver\",\n      \"execPortType\" : \"IO\",\n      \"typeSpec\" : \"MultiPoseConstraintSolver\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"drawDebug\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Boolean\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"rigScale\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Scalar\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"constrainers\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Mat44[]\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"nodePortType\" : \"In\",\n      \"name\" : \"constrainees\",\n"
		+ "      \"execPortType\" : \"Out\",\n      \"typeSpec\" : \"Mat44[]\"\n      }\n    ],\n  \"extDeps\" : {\n    \"Kraken\" : \"*\"\n    },\n  \"nodes\" : [\n    {\n      \"objectType\" : \"Inst\",\n      \"metadata\" : {\n        \"uiGraphPos\" : \"{\\\"x\\\":100.0,\\\"y\\\":100.0}\"\n        },\n      \"name\" : \"spineDeformerKLOp\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"solver\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"drawDebug\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"rigScale\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"constrainers\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"constrainees\"\n          }\n        ],\n      \"definition\" : {\n        \"objectType\" : \"Func\",\n        \"title\" : \"spineDeformerKLOp\",\n"
		+ "        \"ports\" : [\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"IO\",\n            \"name\" : \"solver\",\n            \"execPortType\" : \"IO\",\n            \"typeSpec\" : \"MultiPoseConstraintSolver\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"Out\",\n            \"name\" : \"drawDebug\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"Boolean\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"Out\",\n            \"name\" : \"rigScale\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"Scalar\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"Out\",\n            \"name\" : \"constrainers\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"Mat44[]\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"In\",\n            \"name\" : \"constrainees\",\n            \"execPortType\" : \"Out\",\n            \"typeSpec\" : \"Mat44[]\"\n"
		+ "            }\n          ],\n        \"extDeps\" : {\n          \"Kraken\" : \"*\"\n          },\n        \"code\" : \"dfgEntry {\n  constrainees.resize(6);\n  if(solver == null)\n    solver = MultiPoseConstraintSolver();\n  solver.solve(\n    drawDebug,\n    rigScale,\n    constrainers,\n    constrainees\n  );\n}\n\"\n        }\n      }\n    ],\n  \"connections\" : {\n    \"solver\" : [\n      \"spineDeformerKLOp.solver\"\n      ],\n    \"drawDebug\" : [\n      \"spineDeformerKLOp.drawDebug\"\n      ],\n    \"rigScale\" : [\n      \"spineDeformerKLOp.rigScale\"\n      ],\n    \"constrainers\" : [\n      \"spineDeformerKLOp.constrainers\"\n      ],\n    \"spineDeformerKLOp.solver\" : [\n      \"solver\"\n      ],\n    \"spineDeformerKLOp.constrainees\" : [\n      \"constrainees\"\n      ]\n    },\n  \"metadata\" : {\n    \"maya_id\" : \"2\"\n    },\n  \"args\" : [\n    {\n      \"type\" : \"MultiPoseConstraintSolver\",\n      \"value\" : null,\n      \"ext\" : \"Kraken\"\n      },\n    {\n      \"type\" : \"Boolean\",\n      \"value\" : false\n      },\n    {\n      \"type\" : \"Float32\",\n      \"value\" : 1\n      },\n    {\n      \"type\" : \"Mat44[]\",\n"
		+ "      \"value\" : null,\n      \"ext\" : \"Math\"\n      },\n    {\n      \"type\" : \"Mat44[]\",\n      \"value\" : null,\n      \"ext\" : \"Math\"\n      }\n    ]\n  }");
	setAttr ".evalID" 1;
	setAttr -k on ".drawDebug" no;
	setAttr -k on ".rigScale" 1;
	setAttr -s 6 ".constrainers";
	setAttr -k on ".constrainers[0]" -type "matrix" -1.1920928977282503e-007 1.0000001192092896 0 0
		 1.0000001192092611 1.1920928955077701e-007 1.2246469451366022e-016 0 1.2246470911258943e-016 1.4598929226474285e-023 -1.0000002384185791 0
		 0 9 0 1;
	setAttr -k on ".constrainers[1]" -type "matrix" -1.1920928977282503e-007 1.0000001192092896 0 0
		 1.0000001192092611 1.1920928955077701e-007 1.2246469451366022e-016 0 1.2246470911258943e-016 1.4598929226474285e-023 -1.0000002384185791 0
		 0 10.200000762939453 0 1;
	setAttr -k on ".constrainers[2]" -type "matrix" -1.1920928977282503e-007 1.0000001192092896 0 0
		 1.0000001192092611 1.1920928955077701e-007 1.2246469451366022e-016 0 1.2246470911258943e-016 1.4598929226474285e-023 -1.0000002384185791 0
		 0 11.399999618530273 0 1;
	setAttr -k on ".constrainers[3]" -type "matrix" -1.1920928977282503e-007 1.0000001192092896 0 0
		 1.0000001192092611 1.1920928955077701e-007 1.2246469451366022e-016 0 1.2246470911258943e-016 1.4598929226474285e-023 -1.0000002384185791 0
		 0 12.600000381469727 0 1;
	setAttr -k on ".constrainers[4]" -type "matrix" -1.1920928977282503e-007 1.0000001192092896 0 0
		 1.0000001192092611 1.1920928955077701e-007 1.2246469451366022e-016 0 1.2246470911258943e-016 1.4598929226474285e-023 -1.0000002384185791 0
		 0 13.799999237060547 0 1;
	setAttr -k on ".constrainers[5]" -type "matrix" -1.1920928977282503e-007 1.0000001192092896 0 0
		 1.0000001192092611 1.1920928955077701e-007 1.2246469451366022e-016 0 1.2246470911258943e-016 1.4598929226474285e-023 -1.0000002384185791 0
		 0 15 0 1;
	setAttr -k on ".constrainers";
	setAttr -s 6 ".constrainees";
createNode decomposeMatrix -n "decomposeMatrix7";
	rename -uid "94A62A72-435C-C265-80B6-33879658B6FA";
	setAttr ".ot" -type "double3" 0 9 0 ;
	setAttr ".or" -type "double3" 180 0 90.000006830188354 ;
	setAttr ".os" -type "double3" 1.0000001192092967 1.0000001192092967 1.0000002384185791 ;
createNode decomposeMatrix -n "decomposeMatrix8";
	rename -uid "19074499-46BE-C9B2-7A2C-709D42233844";
	setAttr ".ot" -type "double3" 0 10.200000762939453 0 ;
	setAttr ".or" -type "double3" 180 0 90.000006830188354 ;
	setAttr ".os" -type "double3" 1.0000001192092967 1.0000001192092967 1.0000002384185791 ;
createNode decomposeMatrix -n "decomposeMatrix9";
	rename -uid "EA594E3E-4BD2-F93A-0DF1-73B12A86169A";
	setAttr ".ot" -type "double3" 0 11.399999618530273 0 ;
	setAttr ".or" -type "double3" 180 0 90.000006830188354 ;
	setAttr ".os" -type "double3" 1.0000001192092967 1.0000001192092967 1.0000002384185791 ;
createNode decomposeMatrix -n "decomposeMatrix10";
	rename -uid "090E7EFD-4673-5E70-B371-A0BEC5EC5C3B";
	setAttr ".ot" -type "double3" 0 12.600000381469727 0 ;
	setAttr ".or" -type "double3" 180 0 90.000006830188354 ;
	setAttr ".os" -type "double3" 1.0000001192092967 1.0000001192092967 1.0000002384185791 ;
	setAttr ".oqx" 0.70710673903970278;
	setAttr ".oqy" 0.70710682333338981;
	setAttr ".oqz" 4.3297805392524438e-017;
	setAttr ".oqw" 4.3297800231024742e-017;
createNode decomposeMatrix -n "decomposeMatrix11";
	rename -uid "73C8C030-4A5F-4B48-1261-90841D3A874A";
	setAttr ".ot" -type "double3" 0 13.799999237060547 0 ;
	setAttr ".or" -type "double3" 180 0 90.000006830188354 ;
	setAttr ".os" -type "double3" 1.0000001192092967 1.0000001192092967 1.0000002384185791 ;
createNode decomposeMatrix -n "decomposeMatrix12";
	rename -uid "462CFB59-4241-31B3-3D52-ADA02F5D0B39";
	setAttr ".ot" -type "double3" 0 15 0 ;
	setAttr ".or" -type "double3" 180 0 90.000006830188354 ;
	setAttr ".os" -type "double3" 1.0000001192092967 1.0000001192092967 1.0000002384185791 ;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "197FDC98-497F-F122-A8FB-7DAF0D867226";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"top\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n"
		+ "                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n"
		+ "                -rendererName \"vp2Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n"
		+ "                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 1\n                -height 1\n                -sceneRenderFilter 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n            modelEditor -e \n"
		+ "                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n"
		+ "            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n"
		+ "            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n"
		+ "        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"side\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n"
		+ "                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -rendererName \"vp2Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n"
		+ "                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n"
		+ "                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 1\n                -height 1\n                -sceneRenderFilter 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n            modelEditor -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n"
		+ "            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n"
		+ "            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n"
		+ "            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"front\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n"
		+ "                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -rendererName \"vp2Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n"
		+ "                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n"
		+ "                -width 1\n                -height 1\n                -sceneRenderFilter 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n            modelEditor -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n"
		+ "            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n"
		+ "            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n"
		+ "            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 1\n                -headsUpDisplay 1\n"
		+ "                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 1\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -rendererName \"vp2Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n"
		+ "                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n"
		+ "                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 1800\n                -height 1245\n                -sceneRenderFilter 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n            modelEditor -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\t}\n\t} else {\n"
		+ "\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 1\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 1\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n"
		+ "            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n"
		+ "            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1800\n            -height 1245\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n"
		+ "            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `outlinerPanel -unParent -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            outlinerEditor -e \n                -docTag \"isolOutln_fromSeln\" \n                -showShapes 0\n                -showReferenceNodes 1\n                -showReferenceMembers 1\n                -showAttributes 0\n                -showConnected 0\n                -showAnimCurvesOnly 0\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 1\n                -showPublishedAsConnected 0\n                -showContainerContents 1\n                -ignoreDagHierarchy 0\n"
		+ "                -expandConnections 0\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 0\n                -highlightActive 1\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"defaultSetFilter\" \n                -showSetMembers 1\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n"
		+ "                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 0\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showReferenceNodes 1\n            -showReferenceMembers 1\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 0\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n"
		+ "            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n"
		+ "            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"graphEditor\" -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n"
		+ "                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n"
		+ "                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -stackedCurves 0\n                -stackedCurvesMin -1\n"
		+ "                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n"
		+ "                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n"
		+ "                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n"
		+ "                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dopeSheetPanel\" -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n"
		+ "                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n"
		+ "                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n"
		+ "                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n"
		+ "                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n"
		+ "                -ignoreOutlinerColor 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"clipEditorPanel\" -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 0 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n"
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"sequenceEditorPanel\" -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 1 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n"
		+ "                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperGraphPanel\" -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n"
		+ "                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n"
		+ "                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"visorPanel\" -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"createNodePanel\" -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"polyTexturePlacementPanel\" -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"renderWindowPanel\" -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"blendShapePanel\" (localizedPanelLabel(\"Blend Shape\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\tblendShapePanel -unParent -l (localizedPanelLabel(\"Blend Shape\")) -mbv $menusOkayInPanels ;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tblendShapePanel -edit -l (localizedPanelLabel(\"Blend Shape\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dynRelEdPanel\" -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"relationshipPanel\" -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"referenceEditorPanel\" -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"componentEditorPanel\" -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dynPaintScriptedPanelType\" -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"scriptEditorPanel\" -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"profilerPanel\" (localizedPanelLabel(\"Profiler Tool\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"profilerPanel\" -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"Stereo\" (localizedPanelLabel(\"Stereo\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"Stereo\" -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels `;\nstring $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -editorChanged \"updateModelPanelBar\" \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n"
		+ "                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -rendererOverrideName \"stereoOverrideVP2\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n"
		+ "                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n"
		+ "                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 0\n                -height 0\n                -sceneRenderFilter 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                -useCustomBackground 1\n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n            stereoCameraView -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels  $panelName;\nstring $editorName = ($panelName+\"Editor\");\n"
		+ "            stereoCameraView -e \n                -editorChanged \"updateModelPanelBar\" \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n"
		+ "                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -rendererOverrideName \"stereoOverrideVP2\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n"
		+ "                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n"
		+ "                -captureSequenceNumber -1\n                -width 0\n                -height 0\n                -sceneRenderFilter 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                -useCustomBackground 1\n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n            stereoCameraView -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperShadePanel\" -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"nodeEditorPanel\" -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -defaultPinnedState 0\n                -additiveGraphingMode 1\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n"
		+ "                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -activeTab 0\n                -editorMode \"default\" \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -defaultPinnedState 0\n                -additiveGraphingMode 1\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n"
		+ "                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -activeTab 0\n                -editorMode \"default\" \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\tif ($useSceneConfig) {\n\t\tscriptedPanel -e -to $panelName;\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"vertical2\\\" -ps 1 20 100 -ps 2 80 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Outliner\")) \n\t\t\t\t\t\"outlinerPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `outlinerPanel -unParent -l (localizedPanelLabel(\\\"Outliner\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\noutlinerEditor -e \\n    -docTag \\\"isolOutln_fromSeln\\\" \\n    -showShapes 0\\n    -showReferenceNodes 1\\n    -showReferenceMembers 1\\n    -showAttributes 0\\n    -showConnected 0\\n    -showAnimCurvesOnly 0\\n    -showMuteInfo 0\\n    -organizeByLayer 1\\n    -showAnimLayerWeight 1\\n    -autoExpandLayers 1\\n    -autoExpand 0\\n    -showDagOnly 0\\n    -showAssets 1\\n    -showContainedOnly 1\\n    -showPublishedAsConnected 0\\n    -showContainerContents 1\\n    -ignoreDagHierarchy 0\\n    -expandConnections 0\\n    -showUpstreamCurves 1\\n    -showUnitlessCurves 1\\n    -showCompounds 1\\n    -showLeafs 1\\n    -showNumericAttrsOnly 0\\n    -highlightActive 1\\n    -autoSelectNewObjects 0\\n    -doNotSelectNewObjects 0\\n    -dropIsParent 1\\n    -transmitFilters 0\\n    -setFilter \\\"defaultSetFilter\\\" \\n    -showSetMembers 1\\n    -allowMultiSelection 1\\n    -alwaysToggleSelect 0\\n    -directSelect 0\\n    -displayMode \\\"DAG\\\" \\n    -expandObjects 0\\n    -setsIgnoreFilters 1\\n    -containersIgnoreFilters 0\\n    -editAttrName 0\\n    -showAttrValues 0\\n    -highlightSecondary 0\\n    -showUVAttrsOnly 0\\n    -showTextureNodesOnly 0\\n    -attrAlphaOrder \\\"default\\\" \\n    -animLayerFilterOptions \\\"allAffecting\\\" \\n    -sortOrder \\\"none\\\" \\n    -longNames 0\\n    -niceNames 1\\n    -showNamespace 1\\n    -showPinIcons 0\\n    -mapMotionTrails 0\\n    -ignoreHiddenAttribute 0\\n    -ignoreOutlinerColor 0\\n    $editorName\"\n"
		+ "\t\t\t\t\t\"outlinerPanel -edit -l (localizedPanelLabel(\\\"Outliner\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\noutlinerEditor -e \\n    -docTag \\\"isolOutln_fromSeln\\\" \\n    -showShapes 0\\n    -showReferenceNodes 1\\n    -showReferenceMembers 1\\n    -showAttributes 0\\n    -showConnected 0\\n    -showAnimCurvesOnly 0\\n    -showMuteInfo 0\\n    -organizeByLayer 1\\n    -showAnimLayerWeight 1\\n    -autoExpandLayers 1\\n    -autoExpand 0\\n    -showDagOnly 0\\n    -showAssets 1\\n    -showContainedOnly 1\\n    -showPublishedAsConnected 0\\n    -showContainerContents 1\\n    -ignoreDagHierarchy 0\\n    -expandConnections 0\\n    -showUpstreamCurves 1\\n    -showUnitlessCurves 1\\n    -showCompounds 1\\n    -showLeafs 1\\n    -showNumericAttrsOnly 0\\n    -highlightActive 1\\n    -autoSelectNewObjects 0\\n    -doNotSelectNewObjects 0\\n    -dropIsParent 1\\n    -transmitFilters 0\\n    -setFilter \\\"defaultSetFilter\\\" \\n    -showSetMembers 1\\n    -allowMultiSelection 1\\n    -alwaysToggleSelect 0\\n    -directSelect 0\\n    -displayMode \\\"DAG\\\" \\n    -expandObjects 0\\n    -setsIgnoreFilters 1\\n    -containersIgnoreFilters 0\\n    -editAttrName 0\\n    -showAttrValues 0\\n    -highlightSecondary 0\\n    -showUVAttrsOnly 0\\n    -showTextureNodesOnly 0\\n    -attrAlphaOrder \\\"default\\\" \\n    -animLayerFilterOptions \\\"allAffecting\\\" \\n    -sortOrder \\\"none\\\" \\n    -longNames 0\\n    -niceNames 1\\n    -showNamespace 1\\n    -showPinIcons 0\\n    -mapMotionTrails 0\\n    -ignoreHiddenAttribute 0\\n    -ignoreOutlinerColor 0\\n    $editorName\"\n"
		+ "\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 1\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 1\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1800\\n    -height 1245\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 1\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 1\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1800\\n    -height 1245\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        setFocus `paneLayout -q -p1 $gMainPane`;\n        sceneUIReplacement -deleteRemaining;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "CFC7ACBE-4AD4-E98E-49E7-A4B823B9640F";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode ilrOptionsNode -s -n "TurtleRenderOptions";
	rename -uid "092524B7-4A50-FF05-037B-9B9ED6ECEDB7";
lockNode -l 1 ;
createNode ilrUIOptionsNode -s -n "TurtleUIOptions";
	rename -uid "3C4DB60E-4F13-6855-3042-37957F21623E";
lockNode -l 1 ;
createNode ilrBakeLayerManager -s -n "TurtleBakeLayerManager";
	rename -uid "5059F171-4107-BFBC-AE63-3AA18B09866A";
lockNode -l 1 ;
createNode ilrBakeLayer -s -n "TurtleDefaultBakeLayer";
	rename -uid "E1EB6B46-4F6D-71DD-BE63-EF92956168F5";
lockNode -l 1 ;
createNode skinCluster -n "skinCluster1";
	rename -uid "69CD8307-403D-E37B-47D1-B39BDC8DD2F7";
	setAttr -s 1200 ".wl";
	setAttr -s 5 ".wl[0].w[1:5]"  0.0015113970462828036 0.0041146607782583935 
		0.01523395532336997 0.88503607827335962 0.094103908578729231;
	setAttr -s 5 ".wl[1].w[1:5]"  0.0015113971611581244 0.0041146610814735444 
		0.01523395636312657 0.88503607197883227 0.094103913415409246;
	setAttr -s 5 ".wl[2].w[1:5]"  0.0015113972129271647 0.0041146612207010108 
		0.015233956857669902 0.88503606878617147 0.094103915922530382;
	setAttr -s 5 ".wl[3].w[1:5]"  0.0015113972755841363 0.0041146613828106811 
		0.015233957391855646 0.88503606580433536 0.094103918145414245;
	setAttr -s 5 ".wl[4].w[1:5]"  0.001511397377255615 0.0041146616536687818 
		0.015233958337193515 0.88503605988937672 0.094103922742505272;
	setAttr -s 5 ".wl[5].w[1:5]"  0.0015113975937514296 0.0041146622208229856 
		0.015233960253588339 0.88503604861802054 0.094103931313816627;
	setAttr -s 5 ".wl[6].w[1:5]"  0.0015113977634043077 0.0041146626727268289 
		0.015233961830408945 0.88503603875640302 0.094103938977056961;
	setAttr -s 5 ".wl[7].w[1:5]"  0.001511397817354226 0.0041146628125713243 
		0.015233962292999451 0.88503603615278525 0.094103940924289683;
	setAttr -s 5 ".wl[8].w[1:5]"  0.0015113980359175603 0.0041146633926043511 
		0.015233964302753816 0.88503602374497259 0.094103950523751589;
	setAttr -s 5 ".wl[9].w[1:5]"  0.0015113982840370963 0.0041146640447729046 
		0.015233966520900503 0.88503601052808123 0.094103960622208313;
	setAttr -s 5 ".wl[10].w[1:5]"  0.0015113981382235948 0.0041146636599635614 
		0.015233965201797064 0.88503601850852687 0.094103954491488909;
	setAttr -s 5 ".wl[11].w[1:5]"  0.0015113982840017665 0.004114664044668228 
		0.015233966520450875 0.88503601048141778 0.094103960618529742;
	setAttr -s 5 ".wl[12].w[1:5]"  0.001511398396139988 0.0041146643386868959 
		0.015233967511136048 0.88503598963530128 0.094103964868328754;
	setAttr -s 5 ".wl[13].w[1:5]"  0.0015113988058611172 0.004114665422314305 
		0.015233971246855198 0.88503598537955142 0.094103982666981445;
	setAttr -s 5 ".wl[14].w[1:5]"  0.0015113991725394123 0.0041146663881245016 
		0.015233974540844627 0.88503595103306154 0.094103997631351383;
	setAttr -s 5 ".wl[15].w[1:5]"  0.0015113992499364317 0.0041146665954326436 
		0.015233975278849619 0.88503597025905201 0.09410400162614159;
	setAttr -s 5 ".wl[16].w[1:5]"  0.0015113994323075447 0.0041146670736606841 
		0.015233976890795089 0.88503593684522486 0.094104008553037077;
	setAttr -s 5 ".wl[17].w[1:5]"  0.0015113997893146111 0.0041146680176648003 
		0.015233980143336462 0.88503593155933624 0.094104024011911522;
	setAttr -s 5 ".wl[18].w[1:5]"  0.0015113999816995702 0.0041146685230019344 
		0.015233981854322204 0.88503590283622036 0.094104031525244922;
	setAttr -s 5 ".wl[19].w[1:5]"  0.0015114000097408231 0.0041146685988835236 
		0.015233982131280488 0.88503591573629969 0.094104033159997602;
	setAttr -s 5 ".wl[20].w[1:5]"  0.0013907927338458941 0.0039688822037939773 
		0.015877934760398636 0.86785491031248641 0.1109074799894751;
	setAttr -s 5 ".wl[21].w[1:5]"  0.001390792851868535 0.0039688825299881185 
		0.015877935961178615 0.86785490267750043 0.11090748597946425;
	setAttr -s 5 ".wl[22].w[1:5]"  0.0013907929084323123 0.0039688826898326476 
		0.015877936576136623 0.86785489839756091 0.11090748942803763;
	setAttr -s 5 ".wl[23].w[1:5]"  0.0013907929685291242 0.0039688828514867994 
		0.015877937137638101 0.86785489529518556 0.1109074917471604;
	setAttr -s 5 ".wl[24].w[1:5]"  0.0013907930762393249 0.0039688831525520052 
		0.0158779382714033 0.86785488773114128 0.11090749776866415;
	setAttr -s 5 ".wl[25].w[1:5]"  0.0013907932930672929 0.003968883746014791 
		0.015877940412124009 0.86785487473169987 0.1109075078170941;
	setAttr -s 5 ".wl[26].w[1:5]"  0.0013907934727229062 0.0039688842481096142 
		0.015877942302427922 0.86785486212723817 0.11090751784950149;
	setAttr -s 5 ".wl[27].w[1:5]"  0.0013907935248073245 0.003968884388583809 
		0.015877942793254159 0.86785485937263607 0.11090751992071865;
	setAttr -s 5 ".wl[28].w[1:5]"  0.0013907937534464066 0.0039688850247452667 
		0.015877945167142579 0.86785484383186218 0.1109075322228036;
	setAttr -s 5 ".wl[29].w[1:5]"  0.0013907940047822656 0.0039688857156808923 
		0.015877947682541117 0.86785482822906146 0.11090754436793414;
	setAttr -s 5 ".wl[30].w[1:5]"  0.0013907938550643401 0.0039688853019833967 
		0.015877946160377888 0.86785483789730922 0.11090753678526506;
	setAttr -s 5 ".wl[31].w[1:5]"  0.0013907940047498514 0.0039688857155832126 
		0.015877947682103925 0.86785482818267989 0.11090754436395132;
	setAttr -s 5 ".wl[32].w[1:5]"  0.0013907941223147695 0.0039688860385195743 
		0.015877948850913062 0.86785480602106069 0.11090754970223295;
	setAttr -s 5 ".wl[33].w[1:5]"  0.0013907945399516508 0.0039688871948817903 
		0.015877953129523125 0.86785479701572299 0.11090757161238003;
	setAttr -s 5 ".wl[34].w[1:5]"  0.001390794918854093 0.0039688882399989949 
		0.015877956956131367 0.86785475844524507 0.11090759020569199;
	setAttr -s 5 ".wl[35].w[1:5]"  0.0013907949944173335 0.0039688884518448916 
		0.015877957766501135 0.86785477678292544 0.1109075950137234;
	setAttr -s 5 ".wl[36].w[1:5]"  0.0013907951855251009 0.0039688889768557806 
		0.015877959667307335 0.86785474122512851 0.11090760371110461;
	setAttr -s 5 ".wl[37].w[1:5]"  0.0013907955497096567 0.0039688899850127655 
		0.015877963395474676 0.8678547318112203 0.11090762275104234;
	setAttr -s 5 ".wl[38].w[1:5]"  0.0013907957503286052 0.00396889053699526 
		0.015877965402513787 0.86785470089306416 0.11090763215213907;
	setAttr -s 5 ".wl[39].w[1:5]"  0.0013907957767483655 0.0039688906118779581 
		0.015877965697079673 0.86785471349217724 0.11090763409469871;
	setAttr -s 5 ".wl[40].w[1:5]"  0.0014921145465355257 0.0044827017653436586 
		0.019536148417118874 0.81997727094177586 0.15451176432922611;
	setAttr -s 5 ".wl[41].w[1:5]"  0.0014921146732268006 0.0044827021320406387 
		0.019536149858930457 0.81997726191853737 0.15451177141726477;
	setAttr -s 5 ".wl[42].w[1:5]"  0.0014921147372911991 0.0044827023227868674 
		0.01953615065495868 0.81997725618794071 0.15451177609702252;
	setAttr -s 5 ".wl[43].w[1:5]"  0.0014921147975787772 0.0044827024905676202 
		0.019536151256505735 0.8199772533691756 0.15451177808617225;
	setAttr -s 5 ".wl[44].w[1:5]"  0.0014921149163934103 0.0044827028395513528 
		0.019536152672694714 0.81997724379016856 0.1545117857811921;
	setAttr -s 5 ".wl[45].w[1:5]"  0.0014921151435907446 0.0044827034883344503 
		0.01953615514727752 0.81997722954569441 0.15451179667510284;
	setAttr -s 5 ".wl[46].w[1:5]"  0.0014921153417097957 0.0044827040701585956 
		0.019536157507544238 0.81997721359357578 0.1545118094870116;
	setAttr -s 5 ".wl[47].w[1:5]"  0.0014921153943057769 0.0044827042171268977 
		0.0195361580398144 0.81997721100413046 0.15451181134462258;
	setAttr -s 5 ".wl[48].w[1:5]"  0.0014921156437557707 0.0044827049455357076 
		0.019536160959221529 0.81997719183277928 0.15451182661870758;
	setAttr -s 5 ".wl[49].w[1:5]"  0.0014921159100151284 0.0044827057105794989 
		0.019536163918624269 0.81997717410365512 0.15451184035712601;
	setAttr -s 5 ".wl[50].w[1:5]"  0.0014921157494030668 0.0044827052458593104 
		0.019536162092760691 0.81997718550819942 0.1545118314037775;
	setAttr -s 5 ".wl[51].w[1:5]"  0.0014921159099570162 0.0044827057103979497 
		0.019536163917762677 0.8199771740477142 0.15451184034868451;
	setAttr -s 5 ".wl[52].w[1:5]"  0.0014921160360296996 0.0044827060726576433 
		0.019536165311717996 0.81997715098219015 0.15451184628878964;
	setAttr -s 5 ".wl[53].w[1:5]"  0.0014921164840754396 0.0044827073721453777 
		0.019536170453399084 0.81997713655087689 0.15451187260285901;
	setAttr -s 5 ".wl[54].w[1:5]"  0.0014921168905858077 0.0044827085459183524 
		0.019536175036762176 0.81997709407864894 0.1545118942140061;
	setAttr -s 5 ".wl[55].w[1:5]"  0.0014921169716498566 0.0044827087844801121 
		0.019536176020693966 0.81997711077042712 0.15451190046216118;
	setAttr -s 5 ".wl[56].w[1:5]"  0.0014921171766580882 0.004482709373644608 
		0.019536178288819216 0.8199770737665979 0.15451191016020166;
	setAttr -s 5 ".wl[57].w[1:5]"  0.0014921175673838127 0.0044827105066173323 
		0.019536182768550712 0.81997705968639645 0.15451193299261529;
	setAttr -s 5 ".wl[58].w[1:5]"  0.0014921177826610831 0.0044827111264089973 
		0.019536185167646426 0.81997702707353481 0.15451194365754925;
	setAttr -s 5 ".wl[59].w[1:5]"  0.0014921178108530228 0.0044827112104337393 
		0.019536185526316047 0.8199770388084997 0.15451194628737561;
	setAttr -s 5 ".wl[60].w[1:5]"  0.0018233833021910613 0.0057952405570086633 
		0.027759173365905217 0.71870251727861012 0.24591968549628498;
	setAttr -s 5 ".wl[61].w[1:5]"  0.0018233834411150831 0.0057952409774375303 
		0.027759175105406667 0.71870250844525474 0.2459196920307859;
	setAttr -s 5 ".wl[62].w[1:5]"  0.0018233835131649184 0.0057952412036175651 
		0.027759176122358998 0.71870250180633977 0.24591969735451874;
	setAttr -s 5 ".wl[63].w[1:5]"  0.0018233835770303454 0.0057952413866542455 
		0.027759176777502306 0.71870250033614214 0.24591969792267104;
	setAttr -s 5 ".wl[64].w[1:5]"  0.0018233837090742529 0.005795241794080648 
		0.027759178541208743 0.71870248996225505 0.24591970599338117;
	setAttr -s 5 ".wl[65].w[1:5]"  0.0018233839552750843 0.0057952425257293029 
		0.027759181434343555 0.71870247770635776 0.24591971437829444;
	setAttr -s 5 ".wl[66].w[1:5]"  0.0018233841753984498 0.0057952432047622647 
		0.027759184372183283 0.71870246045457153 0.24591972779308452;
	setAttr -s 5 ".wl[67].w[1:5]"  0.001823384231318115 0.0057952433659683045 
		0.027759184959108316 0.71870245892905738 0.24591972851454788;
	setAttr -s 5 ".wl[68].w[1:5]"  0.00182338450706739 0.0057952442103146517 
		0.027759188550710398 0.71870243890649166 0.24591974382541579;
	setAttr -s 5 ".wl[69].w[1:5]"  0.0018233847971805268 0.0057952450797451203 
		0.027759192062682712 0.7187024226216745 0.24591975543871705;
	setAttr -s 5 ".wl[70].w[1:5]"  0.0018233846210770055 0.0057952445469989242 
		0.027759189860467923 0.71870243376850496 0.24591974720295126;
	setAttr -s 5 ".wl[71].w[1:5]"  0.0018233847971399571 0.0057952450796023196 
		0.02775919206184772 0.71870242258982231 0.24591975542793179;
	setAttr -s 5 ".wl[72].w[1:5]"  0.0018233849325526178 0.0057952454849944865 
		0.027759193679653633 0.71870240132409879 0.24591975931374133;
	setAttr -s 5 ".wl[73].w[1:5]"  0.001823385427292491 0.0057952469868911942 
		0.027759199959184622 0.71870238565964051 0.24591978545945076;
	setAttr -s 5 ".wl[74].w[1:5]"  0.0018233858701935234 0.005795248322617721 
		0.027759205424461156 0.71870234534699196 0.24591980380165696;
	setAttr -s 5 ".wl[75].w[1:5]"  0.0018233859636172152 0.0057952486120076115 
		0.02775920671289801 0.71870235965602303 0.24591981206486632;
	setAttr -s 5 ".wl[76].w[1:5]"  0.0018233861838504149 0.0057952492714745786 
		0.027759209346613377 0.71870232549700597 0.24591981846697708;
	setAttr -s 5 ".wl[77].w[1:5]"  0.0018233866150170674 0.0057952505799356716 
		0.027759214811343143 0.71870231051797107 0.24591984099729658;
	setAttr -s 5 ".wl[78].w[1:5]"  0.0018233868475191878 0.0057952512780579364 
		0.027759217625823063 0.71870228018270232 0.24591984885914617;
	setAttr -s 5 ".wl[79].w[1:5]"  0.0018233868812494211 0.0057952513842455975 
		0.027759218121276921 0.71870229044065614 0.24591985282332593;
	setAttr -s 5 ".wl[80].w[1:5]"  0.0023062397726970256 0.0077974690687373513 
		0.041439785898937626 0.55115449795723825 0.39730200730238963;
	setAttr -s 5 ".wl[81].w[1:5]"  0.002306239926817649 0.0077974695562411734 
		0.041439787977969905 0.55115449353863366 0.39730200900033752;
	setAttr -s 5 ".wl[82].w[1:5]"  0.0023062400053354705 0.0077974698158727197 
		0.041439789214197754 0.55115448858273541 0.39730201238185864;
	setAttr -s 5 ".wl[83].w[1:5]"  0.0023062400779339186 0.0077974700312679023 
		0.041439789969751867 0.55115448991994731 0.39730201000109888;
	setAttr -s 5 ".wl[84].w[1:5]"  0.0023062402230917991 0.007797470501302829 
		0.041439792098836123 0.55115448314659421 0.39730201403017507;
	setAttr -s 5 ".wl[85].w[1:5]"  0.0023062404985461785 0.0077974713539677052 
		0.041439795521868945 0.5511544797217105 0.39730201290390688;
	setAttr -s 5 ".wl[86].w[1:5]"  0.00230624074053817 0.0077974721372932711 
		0.041439799067054368 0.55115446849405703 0.39730201956105726;
	setAttr -s 5 ".wl[87].w[1:5]"  0.0023062408039538191 0.0077974723267410723 
		0.041439799747423907 0.55115446935072476 0.39730201777115642;
	setAttr -s 5 ".wl[88].w[1:5]"  0.002306241108177105 0.007797473302706877 
		0.041439804066015044 0.5511544573483006 0.39730202417480054;
	setAttr -s 5 ".wl[89].w[1:5]"  0.0023062414314945186 0.0077974743135369416 
		0.041439808241035596 0.55115445092673898 0.39730202508719398;
	setAttr -s 5 ".wl[90].w[1:5]"  0.0023062412360923702 0.0077974736957305149 
		0.041439805609470998 0.55115445646256889 0.39730202299613721;
	setAttr -s 5 ".wl[91].w[1:5]"  0.0023062414314385009 0.0077974743133268042 
		0.04143980823965606 0.55115445090403947 0.39730202506788348;
	setAttr -s 5 ".wl[92].w[1:5]"  0.0023062415774172213 0.0077974747671687395 
		0.041439810047598565 0.55115443739600101 0.39730202096140721;
	setAttr -s 5 ".wl[93].w[1:5]"  0.0023062421316531068 0.0077974765289574519 
		0.041439817705844414 0.55115443325593771 0.39730203387006702;
	setAttr -s 5 ".wl[94].w[1:5]"  0.0023062426189257076 0.0077974780620980481 
		0.041439824114822568 0.5511544103795184 0.39730203359055671;
	setAttr -s 5 ".wl[95].w[1:5]"  0.0023062427294496049 0.0077974784238024576 
		0.041439825854910677 0.55115442219496302 0.39730204380628648;
	setAttr -s 5 ".wl[96].w[1:5]"  0.0023062429669576758 0.0077974791624573171 
		0.041439828801611088 0.55115440052430198 0.39730203731059321;
	setAttr -s 5 ".wl[97].w[1:5]"  0.0023062434494197821 0.0077974806952748792 
		0.041439835451307958 0.55115439592281645 0.39730204794453683;
	setAttr -s 5 ".wl[98].w[1:5]"  0.0023062437021358633 0.0077974814848098869 
		0.041439838660220725 0.55115437723037086 0.39730204367205563;
	setAttr -s 5 ".wl[99].w[1:5]"  0.0023062437439020094 0.0077974816244064582 
		0.041439839377531852 0.55115438524262383 0.39730204967684174;
	setAttr -s 5 ".wl[100].w[1:5]"  0.0027489714921977173 0.0099491387035957318 
		0.059214834628398001 0.35815010004088071 0.56993695513492781;
	setAttr -s 5 ".wl[101].w[1:5]"  0.0027489716746129313 0.0099491393127308404 
		0.059214837329181889 0.35815010240190542 0.56993694928156891;
	setAttr -s 5 ".wl[102].w[1:5]"  0.0027489717653050292 0.0099491396303978321 
		0.059214838928944823 0.35815010128512903 0.56993694839022324;
	setAttr -s 5 ".wl[103].w[1:5]"  0.0027489718540630002 0.0099491399080520234 
		0.059214839918219749 0.3581501053292383 0.56993694299042696;
	setAttr -s 5 ".wl[104].w[1:5]"  0.0027489720236735585 0.0099491404886525633 
		0.059214842676070571 0.35815010532620212 0.56993693948540125;
	setAttr -s 5 ".wl[105].w[1:5]"  0.0027489723533817034 0.0099491415650786123 
		0.059214847131722967 0.35815011338965569 0.56993692556016096;
	setAttr -s 5 ".wl[106].w[1:5]"  0.0027489726362210465 0.0099491425329956296 
		0.059214851725782759 0.35815011342808084 0.56993691967691962;
	setAttr -s 5 ".wl[107].w[1:5]"  0.0027489727134870938 0.009949142776331979 
		0.059214852615260993 0.35815011669643831 0.56993691519848177;
	setAttr -s 5 ".wl[108].w[1:5]"  0.0027489730707947082 0.0099491439873249602 
		0.059214858214866453 0.35815011856332718 0.56993690616368664;
	setAttr -s 5 ".wl[109].w[1:5]"  0.0027489734558191663 0.0099491452574000053 
		0.059214863644409678 0.35815012596219115 0.56993689168018014;
	setAttr -s 5 ".wl[110].w[1:5]"  0.0027489732245063797 0.0099491444853921571 
		0.059214860226770492 0.35815012290494752 0.5699368991583833;
	setAttr -s 5 ".wl[111].w[1:5]"  0.0027489734557142112 0.0099491452569902723 
		0.059214863641527248 0.35815012594429202 0.56993689164326866;
	setAttr -s 5 ".wl[112].w[1:5]"  0.0027489736281953127 0.0099491458208458578 
		0.059214865906600231 0.35815012332754143 0.56993687603730625;
	setAttr -s 5 ".wl[113].w[1:5]"  0.0027489742847274941 0.0099491480265259963 
		0.059214875955327699 0.35815013805182128 0.56993686717405712;
	setAttr -s 5 ".wl[114].w[1:5]"  0.002748974861277691 0.009949149939322716 
		0.059214884199275397 0.35815014093870279 0.56993683882734292;
	setAttr -s 5 ".wl[115].w[1:5]"  0.0027489749925721624 0.0099491503962896612 
		0.059214886589978644 0.35815015047660265 0.56993685055396914;
	setAttr -s 5 ".wl[116].w[1:5]"  0.0027489752732742043 0.0099491513143379062 
		0.059214890286065386 0.35815014638797604 0.56993682550426794;
	setAttr -s 5 ".wl[117].w[1:5]"  0.0027489758447650091 0.0099491532330634996 
		0.059214899003146096 0.35815015868566341 0.56993681672582153;
	setAttr -s 5 ".wl[118].w[1:5]"  0.0027489761434544642 0.0099491542153931911 
		0.059214903067027015 0.35815015660031219 0.56993679470885417;
	setAttr -s 5 ".wl[119].w[1:5]"  0.0027489761931782327 0.0099491543928972009 
		0.059214904079100031 0.35815016205772304 0.56993680292785565;
	setAttr -s 5 ".wl[120].w[1:5]"  0.0031229671134208126 0.012184305244260379 
		0.081855030974713042 0.21055607730983078 0.69228161935777499;
	setAttr -s 5 ".wl[121].w[1:5]"  0.0031229673420284142 0.01218430606092398 
		0.081855034826544271 0.2105560830093457 0.69228160876115774;
	setAttr -s 5 ".wl[122].w[1:5]"  0.0031229674574289488 0.01218430649487324 
		0.081855037190363536 0.21055608441371498 0.69228160444361941;
	setAttr -s 5 ".wl[123].w[1:5]"  0.0031229675664690903 0.012184306856996145 
		0.0818550384978812 0.21055608899221867 0.69228159808643486;
	setAttr -s 5 ".wl[124].w[1:5]"  0.0031229677806791081 0.012184307642995124 
		0.081855042508553161 0.2105560929232437 0.69228158914452897;
	setAttr -s 5 ".wl[125].w[1:5]"  0.0031229681909858658 0.01218430907277882 
		0.081855048726583085 0.21055610559407403 0.6922815684155782;
	setAttr -s 5 ".wl[126].w[1:5]"  0.0031229685481937303 0.012184310383137192 
		0.081855055408016714 0.21055611217245634 0.69228155348819609;
	setAttr -s 5 ".wl[127].w[1:5]"  0.0031229686433001174 0.012184310701402003 
		0.081855056595150508 0.21055611600191987 0.6922815480582275;
	setAttr -s 5 ".wl[128].w[1:5]"  0.0031229690931748448 0.012184312334604682 
		0.081855064679575942 0.21055612544666744 0.69228152844597712;
	setAttr -s 5 ".wl[129].w[1:5]"  0.0031229695738447527 0.012184314028800125 
		0.081855072335416487 0.2105561389859899 0.69228150507594877;
	setAttr -s 5 ".wl[130].w[1:5]"  0.0031229692840194401 0.012184312994080447 
		0.081855067464382147 0.21055613171719509 0.69228151854032283;
	setAttr -s 5 ".wl[131].w[1:5]"  0.0031229695737160527 0.012184314028272882 
		0.081855072331330339 0.21055613897410308 0.69228150502709407;
	setAttr -s 5 ".wl[132].w[1:5]"  0.0031229697947485618 0.012184314801647781 
		0.081855075599372953 0.21055614250579327 0.69228148201892636;
	setAttr -s 5 ".wl[133].w[1:5]"  0.0031229706113409992 0.012184317736430807 
		0.081855089874966494 0.21055616546811939 0.69228145980160194;
	setAttr -s 5 ".wl[134].w[1:5]"  0.0031229713384854233 0.012184320317205177 
		0.081855101663440635 0.21055618175750535 0.69228141368928486;
	setAttr -s 5 ".wl[135].w[1:5]"  0.0031229714952024702 0.0121843209017967 
		0.081855105009333198 0.21055618889372732 0.69228142670935267;
	setAttr -s 5 ".wl[136].w[1:5]"  0.0031229718547120611 0.012184322160211227 
		0.081855110339551604 0.21055619470441561 0.69228138970703113;
	setAttr -s 5 ".wl[137].w[1:5]"  0.0031229725660491068 0.012184324715030179 
		0.081855122727329047 0.21055621449199599 0.69228136899205539;
	setAttr -s 5 ".wl[138].w[1:5]"  0.0031229729463331428 0.012184326053289733 
		0.081855128567812366 0.21055622154913697 0.69228133561846883;
	setAttr -s 5 ".wl[139].w[1:5]"  0.0031229730039097738 0.012184326274304956 
		0.081855129974175989 0.21055622496837936 0.69228134545181175;
	setAttr -s 5 ".wl[140].w[1:5]"  0.0037074950968213451 0.01571611400308973 
		0.11960823810826215 0.12714799564102655 0.73382015715080018;
	setAttr -s 5 ".wl[141].w[1:5]"  0.0037074953823613413 0.015716115095494865 
		0.11960824334071529 0.12714800100167611 0.73382014517975247;
	setAttr -s 5 ".wl[142].w[1:5]"  0.0037074955327726102 0.01571611570774124 
		0.11960824688837945 0.12714800286470601 0.73382013900640075;
	setAttr -s 5 ".wl[143].w[1:5]"  0.0037074956610142571 0.015716116151801438 
		0.11960824823733401 0.12714800648751301 0.73382013346233721;
	setAttr -s 5 ".wl[144].w[1:5]"  0.0037074959346067929 0.015716117233800484 
		0.11960825400983859 0.12714801070247891 0.73382012211927516;
	setAttr -s 5 ".wl[145].w[1:5]"  0.0037074964367003515 0.015716119093666641 
		0.11960826189868276 0.12714802172124709 0.73382010084970306;
	setAttr -s 5 ".wl[146].w[1:5]"  0.0037074968927777352 0.015716120896675557 
		0.11960827150684003 0.12714802876526879 0.73382008193843795;
	setAttr -s 5 ".wl[147].w[1:5]"  0.003707497005359326 0.015716121290934578 
		0.11960827278619796 0.1271480318301966 0.73382007708731167;
	setAttr -s 5 ".wl[148].w[1:5]"  0.003707497574863528 0.015716123514094949 
		0.11960828417636184 0.12714804136361443 0.73382005337106515;
	setAttr -s 5 ".wl[149].w[1:5]"  0.0037074981685986212 0.015716125746662056 
		0.11960829421973052 0.1271480535259307 0.73382002833907811;
	setAttr -s 5 ".wl[150].w[1:5]"  0.0037074978067451669 0.015716124363305259 
		0.11960828761045204 0.12714804670637969 0.73382004351311791;
	setAttr -s 5 ".wl[151].w[1:5]"  0.0037074981683631308 0.015716125745566946 
		0.11960829420974138 0.1271480535187717 0.73382002827752135;
	setAttr -s 5 ".wl[152].w[1:5]"  0.003707498447265231 0.015716126788292172 
		0.11960829851377583 0.12714805790616912 0.73382000306498674;
	setAttr -s 5 ".wl[153].w[1:5]"  0.0037074994631153108 0.015716130700629952 
		0.11960831803842026 0.12714807813109996 0.73381997715919423;
	setAttr -s 5 ".wl[154].w[1:5]"  0.0037075003737040814 0.015716134158882594 
		0.11960833390211834 0.12714809445369402 0.73381992587752243;
	setAttr -s 5 ".wl[155].w[1:5]"  0.0037075005647144717 0.015716134926485024 
		0.11960833864851543 0.12714809944259578 0.73381993942710155;
	setAttr -s 5 ".wl[156].w[1:5]"  0.0037075010181652239 0.015716136622514178 
		0.119608345670506 0.1271481066026274 0.73381989885210863;
	setAttr -s 5 ".wl[157].w[1:5]"  0.0037075019032794263 0.01571614002878962 
		0.11960836259630313 0.12714812412971149 0.73381987480527222;
	setAttr -s 5 ".wl[158].w[1:5]"  0.0037075023817238861 0.015716141828874965 
		0.11960837036096887 0.12714813207668571 0.73381983808678752;
	setAttr -s 5 ".wl[159].w[1:5]"  0.0037075024507193465 0.015716142115669424 
		0.11960837239585777 0.12714813423220039 0.73381984847085902;
	setAttr -s 5 ".wl[160].w[1:5]"  0.0048548324838580438 0.022554534293829129 
		0.19328587028406813 0.084768847086054727 0.69453591585218999;
	setAttr -s 5 ".wl[161].w[1:5]"  0.0048548328330148566 0.022554535707646244 
		0.19328587595752628 0.084768850998428832 0.69453590450338387;
	setAttr -s 5 ".wl[162].w[1:5]"  0.0048548330237450695 0.022554536546362251 
		0.19328588057471455 0.084768852453210142 0.69453589740196808;
	setAttr -s 5 ".wl[163].w[1:5]"  0.0048548331719814996 0.022554537062694061 
		0.19328588106519828 0.084768854976524061 0.69453589372360214;
	setAttr -s 5 ".wl[164].w[1:5]"  0.0048548335130811542 0.022554538507624747 
		0.19328588806479571 0.084768858143623158 0.69453588177087533;
	setAttr -s 5 ".wl[165].w[1:5]"  0.0048548341157888938 0.022554540838136454 
		0.19328589534380952 0.084768866027383385 0.69453586367488185;
	setAttr -s 5 ".wl[166].w[1:5]"  0.004854834684274863 0.022554543245097421 
		0.1932859069821003 0.084768871318085082 0.69453584377044242;
	setAttr -s 5 ".wl[167].w[1:5]"  0.0048548348152044557 0.022554543709522677 
		0.19328590760679396 0.084768873460723995 0.69453584040775496;
	setAttr -s 5 ".wl[168].w[1:5]"  0.0048548355198185312 0.022554546642773555 
		0.19328592088726554 0.084768880532894469 0.69453581641724782;
	setAttr -s 5 ".wl[169].w[1:5]"  0.004854836238667809 0.022554549483430619 
		0.19328593096468893 0.084768889308417597 0.69453579400479504;
	setAttr -s 5 ".wl[170].w[1:5]"  0.0048548357963935735 0.022554547694401527 
		0.19328592382027321 0.084768884333718819 0.694535808355213;
	setAttr -s 5 ".wl[171].w[1:5]"  0.0048548362384873874 0.022554549482498836 
		0.19328593095435223 0.08476888930496361 0.69453579396149034;
	setAttr -s 5 ".wl[172].w[1:5]"  0.0048548365743790499 0.022554550796781824 
		0.19328593463125443 0.084768892624277573 0.69453577009379608;
	setAttr -s 5 ".wl[173].w[1:5]"  0.0048548378221400469 0.022554555898721462 
		0.19328595694160541 0.084768907226146578 0.69453574560384612;
	setAttr -s 5 ".wl[174].w[1:5]"  0.0048548389304151479 0.022554560338733948 
		0.19328597315098373 0.084768919248721708 0.69453569709706708;
	setAttr -s 5 ".wl[175].w[1:5]"  0.0048548391717239577 0.022554561385539237 
		0.19328597983348544 0.084768922694279367 0.69453570992438418;
	setAttr -s 5 ".wl[176].w[1:5]"  0.0048548397181543482 0.022554563525134276 
		0.19328598587465487 0.084768928109794681 0.6945356715381833;
	setAttr -s 5 ".wl[177].w[1:5]"  0.0048548408049388586 0.022554567964124795 
		0.19328600512017968 0.084768940778873536 0.69453564882434271;
	setAttr -s 5 ".wl[178].w[1:5]"  0.0048548413837720935 0.022554570250917862 
		0.19328601231991957 0.084768946725644487 0.69453561409844278;
	setAttr -s 5 ".wl[179].w[1:5]"  0.0048548414726478388 0.022554570653798029 
		0.19328601546380506 0.084768948173897532 0.6945356238866055;
	setAttr -s 5 ".wl[180].w[1:5]"  0.0067109460518877308 0.034488816719890361 
		0.324450893808721 0.060162230259027803 0.57418711316047311;
	setAttr -s 5 ".wl[181].w[1:5]"  0.0067109464706006121 0.034488818475247637 
		0.32445089646786546 0.060162232905879881 0.57418710568040654;
	setAttr -s 5 ".wl[182].w[1:5]"  0.006710946699159343 0.034488819545396392 
		0.32445090031670565 0.060162233859793017 0.57418709957894576;
	setAttr -s 5 ".wl[183].w[1:5]"  0.0067109468771162752 0.034488820149880514 
		0.32445089841600211 0.060162235605359403 0.57418709895164177;
	setAttr -s 5 ".wl[184].w[1:5]"  0.0067109472859979147 0.034488821971467187 
		0.3244509033131609 0.060162237719001525 0.57418708971037258;
	setAttr -s 5 ".wl[185].w[1:5]"  0.0067109480089990172 0.034488824816851844 
		0.32445090393030712 0.06016224310322961 0.57418708014061248;
	setAttr -s 5 ".wl[186].w[1:5]"  0.0067109486904551232 0.034488827850745911 
		0.32445091204873394 0.06016224663477257 0.57418706477529247;
	setAttr -s 5 ".wl[187].w[1:5]"  0.0067109488476155233 0.03448882839870019 
		0.32445091067229681 0.06016224811447704 0.57418706396691044;
	setAttr -s 5 ".wl[188].w[1:5]"  0.0067109496923372603 0.034488832074875082 
		0.32445091892464528 0.060162252862981019 0.5741870464451615;
	setAttr -s 5 ".wl[189].w[1:5]"  0.0067109505545484404 0.03448883557118626 
		0.32445092186725277 0.060162258832060701 0.5741870331749519;
	setAttr -s 5 ".wl[190].w[1:5]"  0.0067109500241877154 0.0344888333509588 
		0.32445091856730546 0.060162255465465032 0.57418704259208297;
	setAttr -s 5 ".wl[191].w[1:5]"  0.0067109505542804039 0.034488835569637617 
		0.3244509218479667 0.06016225882957519 0.57418703314033237;
	setAttr -s 5 ".wl[192].w[1:5]"  0.0067109509435360707 0.034488837101771266 
		0.32445091996588493 0.060162261033362821 0.57418701567593389;
	setAttr -s 5 ".wl[193].w[1:5]"  0.0067109524565021027 0.034488843555344588 
		0.32445093468337594 0.060162270967599345 0.57418700182963778;
	setAttr -s 5 ".wl[194].w[1:5]"  0.0067109537724146682 0.034488848969772966 
		0.32445093870486325 0.060162279062672804 0.57418696825619786;
	setAttr -s 5 ".wl[195].w[1:5]"  0.0067109540833413641 0.034488850426415904 
		0.32445094749265807 0.060162281462207721 0.57418697954478914;
	setAttr -s 5 ".wl[196].w[1:5]"  0.0067109547170457499 0.034488852924146031 
		0.32445094458035512 0.060162285059374279 0.57418695148500021;
	setAttr -s 5 ".wl[197].w[1:5]"  0.0067109560333768756 0.034488858528700456 
		0.32445095693110776 0.06016229367429482 0.57418693832497969;
	setAttr -s 5 ".wl[198].w[1:5]"  0.0067109567106593583 0.034488861244035558 
		0.32445095584493105 0.060162297644692886 0.57418691330527394;
	setAttr -s 5 ".wl[199].w[1:5]"  0.0067109568306556438 0.034488861841662839 
		0.32445096080399499 0.060162298668114608 0.574186921506326;
	setAttr -s 5 ".wl[200].w[1:5]"  0.0089262853412722457 0.051228265052358245 
		0.49807471874977238 0.04149430602087098 0.40027642483572612;
	setAttr -s 5 ".wl[201].w[1:5]"  0.0089262858649528983 0.05122826731556044 
		0.49807471440065154 0.041494307946928898 0.40027642447190637;
	setAttr -s 5 ".wl[202].w[1:5]"  0.0089262861424813621 0.051228268683234345 
		0.4980747145933726 0.041494308629505844 0.40027642195140584;
	setAttr -s 5 ".wl[203].w[1:5]"  0.0089262863755557465 0.051228269477654173 
		0.49807470949832228 0.041494309914492648 0.40027642473397523;
	setAttr -s 5 ".wl[204].w[1:5]"  0.0089262868790429602 0.051228271815534063 
		0.49807470772059947 0.041494311440838927 0.4002764221439844;
	setAttr -s 5 ".wl[205].w[1:5]"  0.0089262877969447929 0.05122827550268446 
		0.49807469594512216 0.041494315379013436 0.40027642537623509;
	setAttr -s 5 ".wl[206].w[1:5]"  0.0089262886362225999 0.051228279396666611 
		0.49807469293578815 0.041494317929552764 0.40027642110176992;
	setAttr -s 5 ".wl[207].w[1:5]"  0.0089262888409360735 0.051228280114230439 
		0.49807468875474958 0.041494319018369821 0.40027642327171409;
	setAttr -s 5 ".wl[208].w[1:5]"  0.0089262898875423404 0.051228284840833194 
		0.49807468308263869 0.04149432245884245 0.40027641973014333;
	setAttr -s 5 ".wl[209].w[1:5]"  0.0089262909745718572 0.051228289360210448 
		0.49807467140617612 0.041494326815479245 0.4002764214435624;
	setAttr -s 5 ".wl[210].w[1:5]"  0.0089262903110176837 0.051228286497307221 
		0.49807467698806751 0.041494324365346301 0.40027642183826129;
	setAttr -s 5 ".wl[211].w[1:5]"  0.0089262909741447058 0.051228289357452966 
		0.49807467137102152 0.041494326813507648 0.40027642141838959;
	setAttr -s 5 ".wl[212].w[1:5]"  0.00892629145315889 0.051228291230624015 
		0.49807465862024886 0.041494328452545533 0.40027641496391181;
	setAttr -s 5 ".wl[213].w[1:5]"  0.0089262933560464025 0.051228299679115102 
		0.49807465336918377 0.041494335639480448 0.4002764214486339;
	setAttr -s 5 ".wl[214].w[1:5]"  0.008926294994639962 0.051228306561344444 
		0.49807463114120137 0.041494341564639735 0.40027641450409612;
	setAttr -s 5 ".wl[215].w[1:5]"  0.008926295396501421 0.051228308603427822 
		0.49807464165584636 0.041494343255441539 0.40027642409819525;
	setAttr -s 5 ".wl[216].w[1:5]"  0.0089262961765104107 0.051228311660375357 
		0.49807462119701701 0.041494345928915717 0.40027641380310303;
	setAttr -s 5 ".wl[217].w[1:5]"  0.0089262978309755815 0.051228318985262478 
		0.49807461570072614 0.04149435216373866 0.40027641878265297;
	setAttr -s 5 ".wl[218].w[1:5]"  0.0089262986685518571 0.051228322360712425 
		0.49807459791871944 0.041494355096847735 0.40027641069020964;
	setAttr -s 5 ".wl[219].w[1:5]"  0.0089262988268407964 0.051228323233497242 
		0.49807460514461421 0.041494355808749134 0.40027641665160452;
	setAttr -s 5 ".wl[220].w[1:5]"  0.011149121279618477 0.072066603455435904 
		0.6463216262129764 0.027098840524147867 0.2433638085278215;
	setAttr -s 5 ".wl[221].w[1:5]"  0.01114912198964004 0.072066606713743459 
		0.64632161599527205 0.02709884206260816 0.24336381323873629;
	setAttr -s 5 ".wl[222].w[1:5]"  0.011149122365841957 0.072066608706618601 
		0.64632161232078444 0.027098842644431523 0.24336381396232348;
	setAttr -s 5 ".wl[223].w[1:5]"  0.011149122682078318 0.072066609821499691 
		0.64632160557461105 0.027098843624139158 0.24336381829767179;
	setAttr -s 5 ".wl[224].w[1:5]"  0.011149123364538414 0.072066613209157082 
		0.6463215974233788 0.027098844878876583 0.243363821124049;
	setAttr -s 5 ".wl[225].w[1:5]"  0.011149124609520944 0.072066618481346795 
		0.64632157662830947 0.027098847962674383 0.2433638323181484;
	setAttr -s 5 ".wl[226].w[1:5]"  0.011149125747138259 0.072066624123462153 
		0.6463215630087964 0.027098850058524995 0.24336383706207829;
	setAttr -s 5 ".wl[227].w[1:5]"  0.011149126024943565 0.07206662513462557 
		0.64632155728982932 0.027098850891354782 0.24336384065924671;
	setAttr -s 5 ".wl[228].w[1:5]"  0.011149127443768031 0.072066631967260722 
		0.64632153897118882 0.027098853684031508 0.24336384793375093;
	setAttr -s 5 ".wl[229].w[1:5]"  0.011149128917932405 0.072066638451130288 
		0.64632151592212195 0.027098857124356026 0.24336385958445925;
	setAttr -s 5 ".wl[230].w[1:5]"  0.011149128018204347 0.072066634329492979 
		0.64632152891706407 0.027098855168507133 0.24336385356673135;
	setAttr -s 5 ".wl[231].w[1:5]"  0.011149128917496941 0.072066638447784312 
		0.64632151588057429 0.027098857123355895 0.24336385957258089;
	setAttr -s 5 ".wl[232].w[1:5]"  0.011149129581439727 0.072066641169637846 
		0.64632149400141625 0.02709885852318128 0.24336386144481398;
	setAttr -s 5 ".wl[233].w[1:5]"  0.011149132143695258 0.072066653301017344 
		0.64632147214763735 0.027098864147102244 0.24336388175300733;
	setAttr -s 5 ".wl[234].w[1:5]"  0.011149134379553909 0.072066663233947142 
		0.64632142796299541 0.027098868965606177 0.24336389422381874;
	setAttr -s 5 ".wl[235].w[1:5]"  0.011149134901313073 0.072066666133015655 
		0.64632143999988978 0.027098870169249632 0.24336390180594419;
	setAttr -s 5 ".wl[236].w[1:5]"  0.011149135982078819 0.072066670574851222 
		0.64632140481593658 0.02709887244941156 0.24336390494364327;
	setAttr -s 5 ".wl[237].w[1:5]"  0.011149138211380817 0.072066681095480062 
		0.64632138448177301 0.027098877337850217 0.24336392233687171;
	setAttr -s 5 ".wl[238].w[1:5]"  0.011149139365102796 0.072066685987608001 
		0.64632135270852253 0.027098879792436897 0.24336392689592271;
	setAttr -s 5 ".wl[239].w[1:5]"  0.011149139565321193 0.072066687217920686 
		0.64632136185890754 0.027098880270378545 0.24336393075277807;
	setAttr -s 5 ".wl[240].w[1:5]"  0.014147519661174009 0.10355325522328512 
		0.71887878710755027 0.018074148629848519 0.14534628937814215;
	setAttr -s 5 ".wl[241].w[1:5]"  0.014147520632894418 0.10355325987416752 
		0.71887877481418172 0.018074149834250482 0.14534629484450601;
	setAttr -s 5 ".wl[242].w[1:5]"  0.014147521170218644 0.10355326294106178 
		0.71887876893616198 0.018074150323984323 0.14534629662857318;
	setAttr -s 5 ".wl[243].w[1:5]"  0.014147521574426523 0.10355326424936867 
		0.71887876265903128 0.018074151047936519 0.14534630046923702;
	setAttr -s 5 ".wl[244].w[1:5]"  0.014147522529989498 0.10355326929825917 
		0.71887875145305113 0.018074152063103231 0.14534630465559706;
	setAttr -s 5 ".wl[245].w[1:5]"  0.014147524196357633 0.10355327645252699 
		0.71887872884587212 0.018074154420870823 0.14534631608437243;
	setAttr -s 5 ".wl[246].w[1:5]"  0.014147525788805926 0.10355328485762162 
		0.71887871015455707 0.018074156115814921 0.1453463230832005;
	setAttr -s 5 ".wl[247].w[1:5]"  0.01414752614665221 0.10355328607966166 
		0.71887870471589699 0.018074156734023187 0.14534632632376596;
	setAttr -s 5 ".wl[248].w[1:5]"  0.01414752811545978 0.10355329609997818 
		0.71887868091748108 0.018074158961700955 0.14534633590538001;
	setAttr -s 5 ".wl[249].w[1:5]"  0.014147530108988999 0.10355330511747431 
		0.71887865472371693 0.018074161619116767 0.14534634843070302;
	setAttr -s 5 ".wl[250].w[1:5]"  0.014147528878369186 0.10355329924158695 
		0.71887867031872765 0.018074160088785596 0.1453463414725305;
	setAttr -s 5 ".wl[251].w[1:5]"  0.014147530108343655 0.10355330511179495 
		0.71887865467263357 0.018074161618368337 0.14534634842337599;
	setAttr -s 5 ".wl[252].w[1:5]"  0.014147531033328902 0.1035533089803904 
		0.71887862928568236 0.018074162761389418 0.14534635265969786;
	setAttr -s 5 ".wl[253].w[1:5]"  0.014147534517188184 0.10355332629011411 
		0.7188786019956569 0.018074167102979773 0.14534637358652072;
	setAttr -s 5 ".wl[254].w[1:5]"  0.014147537591523408 0.10355334043842081 
		0.71887854980818011 0.018074170919197791 0.14534639000859947;
	setAttr -s 5 ".wl[255].w[1:5]"  0.014147538278452273 0.10355334459108603 
		0.71887856287756791 0.018074171785111511 0.1453463954771945;
	setAttr -s 5 ".wl[256].w[1:5]"  0.014147539783387135 0.10355335090356342 
		0.71887852203103664 0.018074173645031395 0.14534640240290275;
	setAttr -s 5 ".wl[257].w[1:5]"  0.014147542816336164 0.1035533659136869 
		0.71887849679572224 0.018074177423906958 0.1453464205137035;
	setAttr -s 5 ".wl[258].w[1:5]"  0.014147544415170767 0.10355337287411429 
		0.71887845973891451 0.018074179403263637 0.14534642833268158;
	setAttr -s 5 ".wl[259].w[1:5]"  0.014147544672381319 0.10355337463869799 
		0.71887846986307313 0.01807417973028828 0.14534643076086531;
	setAttr -s 5 ".wl[260].w[1:5]"  0.019750902395365356 0.16334331233152796 
		0.70923523167418978 0.013282513457866773 0.094388040141050192;
	setAttr -s 5 ".wl[261].w[1:5]"  0.019750903070095638 0.16334331126303697 
		0.70923522506367398 0.013282514519209898 0.094388046083983601;
	setAttr -s 5 ".wl[262].w[1:5]"  0.019750903824729431 0.16334331557003626 
		0.70923521803967193 0.013282514899538163 0.094388047666024363;
	setAttr -s 5 ".wl[263].w[1:5]"  0.019750904918434734 0.16334332308131322 
		0.70923520794484196 0.013282515264686736 0.094388048790723267;
	setAttr -s 5 ".wl[264].w[1:5]"  0.019750905613251324 0.16334332307399707 
		0.70923520121090755 0.013282516197373098 0.094388053904470984;
	setAttr -s 5 ".wl[265].w[1:5]"  0.019750908362350373 0.16334333741779541 
		0.70923517553238247 0.01328251778030334 0.094388060907168295;
	setAttr -s 5 ".wl[266].w[1:5]"  0.019750909927272423 0.16334334183784915 
		0.70923516066349634 0.013282519230494203 0.094388068340887782;
	setAttr -s 5 ".wl[267].w[1:5]"  0.019750910971446173 0.16334334941087625 
		0.7092351510528232 0.013282519520176547 0.094388069044677878;
	setAttr -s 5 ".wl[268].w[1:5]"  0.019750913018714584 0.16334335555636145 
		0.70923513162536544 0.013282521364118418 0.09438807843544024;
	setAttr -s 5 ".wl[269].w[1:5]"  0.019750915614486882 0.16334336582343842 
		0.70923510715906035 0.013282523339192472 0.094388088063821832;
	setAttr -s 5 ".wl[270].w[1:5]"  0.01975091459801219 0.16334336542840514 
		0.70923511698316066 0.013282522034217394 0.094388080956204504;
	setAttr -s 5 ".wl[271].w[1:5]"  0.019750915088083656 0.1633433614683259 
		0.70923508823715953 0.013282522985198511 0.094388085547571804;
	setAttr -s 5 ".wl[272].w[1:5]"  0.019750918086980124 0.16334338197618545 
		0.70923510005136692 0.013282524476550353 0.094388093133149886;
	setAttr -s 5 ".wl[273].w[1:5]"  0.019750920927717998 0.1633433871416515 
		0.70923503651492958 0.013282527088818871 0.094388105189336852;
	setAttr -s 5 ".wl[274].w[1:5]"  0.019750926772278989 0.16334342006391306 
		0.70923502201253452 0.013282530580623002 0.094388122311211714;
	setAttr -s 5 ".wl[275].w[1:5]"  0.019750925916609294 0.16334340957779897 
		0.70923499814091862 0.013282530590682294 0.09438812215339823;
	setAttr -s 5 ".wl[276].w[1:5]"  0.019750929674443023 0.1633434326891286 
		0.70923499476120611 0.013282532621071897 0.094388132023815435;
	setAttr -s 5 ".wl[277].w[1:5]"  0.019750931914674013 0.1633434349294165 
		0.70923493324878006 0.013282534813577281 0.094388141956006838;
	setAttr -s 5 ".wl[278].w[1:5]"  0.019750935801331429 0.16334345902588437 
		0.70923493356760381 0.013282536931226923 0.094388152412738124;
	setAttr -s 5 ".wl[279].w[1:5]"  0.01975093436739344 0.16334344530171208 
		0.70923490677743373 0.013282536540352906 0.094388150055684975;
	setAttr -s 5 ".wl[280].w[1:5]"  0.030028047444570955 0.27559099534568515 
		0.61717493104613863 0.0106045024560313 0.066601523707573732;
	setAttr -s 5 ".wl[281].w[1:5]"  0.030028049073058526 0.27559099937714721 
		0.61717492177169619 0.010604503112646536 0.06660152666545166;
	setAttr -s 5 ".wl[282].w[1:5]"  0.030028050065787279 0.27559100376436962 
		0.61717491503423605 0.010604503385809242 0.066601527749797815;
	setAttr -s 5 ".wl[283].w[1:5]"  0.030028050626609123 0.27559100271259479 
		0.6171749132107428 0.010604503772675047 0.066601529677378368;
	setAttr -s 5 ".wl[284].w[1:5]"  0.030028052317468138 0.2755910087584007 
		0.61717490253648777 0.010604504331918948 0.066601532055724499;
	setAttr -s 5 ".wl[285].w[1:5]"  0.030028054957232514 0.27559101209351172 
		0.61717488929983499 0.010604505607070724 0.066601538042350014;
	setAttr -s 5 ".wl[286].w[1:5]"  0.030028057772639172 0.27559102212195602 
		0.61717487154789985 0.010604506540774789 0.066601542016730145;
	setAttr -s 5 ".wl[287].w[1:5]"  0.030028058280844434 0.27559102146696263 
		0.61717486972806346 0.010604506871707695 0.066601543652421852;
	setAttr -s 5 ".wl[288].w[1:5]"  0.030028061692117278 0.27559103224355957 
		0.61717484899088315 0.010604508093555631 0.066601548979884309;
	setAttr -s 5 ".wl[289].w[1:5]"  0.030028064935990473 0.27559103823663345 
		0.61717483166089471 0.010604509535713852 0.066601555630767612;
	setAttr -s 5 ".wl[290].w[1:5]"  0.030028062875921264 0.27559103318913714 
		0.61717484336382678 0.010604508701632029 0.066601551869482828;
	setAttr -s 5 ".wl[291].w[1:5]"  0.03002806493466827 0.27559103822069603 
		0.61717483162307962 0.01060450953533078 0.066601555628017811;
	setAttr -s 5 ".wl[292].w[1:5]"  0.030028066387183749 0.27559103870962859 
		0.61717481140425379 0.010604510147080796 0.066601558101445954;
	setAttr -s 5 ".wl[293].w[1:5]"  0.03002807233731327 0.27559105707231785 
		0.61717479236875183 0.010604512527221225 0.066601569186855419;
	setAttr -s 5 ".wl[294].w[1:5]"  0.030028077390220183 0.27559106647520976 
		0.61717475206441974 0.010604514596084023 0.066601578239987858;
	setAttr -s 5 ".wl[295].w[1:5]"  0.030028078693957148 0.27559107456691834 
		0.61717476375628399 0.010604515086302347 0.066601580905950294;
	setAttr -s 5 ".wl[296].w[1:5]"  0.03002808105934061 0.27559107546345668 
		0.61717473122166644 0.010604516081749596 0.066601584939708192;
	setAttr -s 5 ".wl[297].w[1:5]"  0.030028086230551181 0.27559109110659308 
		0.61717471344702191 0.010604518152739828 0.066601594555553534;
	setAttr -s 5 ".wl[298].w[1:5]"  0.030028088786553424 0.27559109357844475 
		0.61717468415124532 0.010604519216844421 0.066601599001952977;
	setAttr -s 5 ".wl[299].w[1:5]"  0.03002808931254591 0.27559109788334918 
		0.61717469292464366 0.010604519406620145 0.066601600138147102;
	setAttr -s 6 ".wl[300].w[0:5]"  6.1855881756087485e-010 0.045575042302750453 
		0.44269167736265291 0.45639987172543001 0.0084010238592186065 0.046932384131388269;
	setAttr -s 6 ".wl[301].w[0:5]"  6.2195924630977581e-010 0.045575044366023901 
		0.44269167537910326 0.45639986905647889 0.0084010243482975245 0.046932386228137175;
	setAttr -s 6 ".wl[302].w[0:5]"  1.5865920445058682e-010 0.045575044466083708 
		0.4426916671401781 0.45639987537037902 0.0084010249507127672 0.046932387913987142;
	setAttr -s 6 ".wl[303].w[0:5]"  5.842302760345355e-010 0.04557504633631209 
		0.44269167276502502 0.45639986707748093 0.0084010248664993133 0.046932388370452459;
	setAttr -s 6 ".wl[304].w[0:5]"  1.1599583045802863e-010 0.04557504731968124 
		0.442691663564652 0.45639987233761226 0.008401025686273423 0.046932390975785158;
	setAttr -s 6 ".wl[305].w[0:5]"  4.8463184966357766e-010 0.045575051826260413 
		0.44269166557837153 0.45639986148640366 0.0084010263034974535 0.046932394320835236;
	setAttr -s 6 ".wl[306].w[0:5]"  1.1599585442730342e-010 0.045575054231746945 
		0.44269165671952426 0.45639986355486506 0.0084010273389354059 0.04693239803893251;
	setAttr -s 6 ".wl[307].w[0:5]"  5.8423044540540512e-010 0.045575056034165812 
		0.44269166316108632 0.45639985475500111 0.0084010271852378617 0.046932398280278453;
	setAttr -s 6 ".wl[308].w[0:5]"  1.580519660971588e-010 0.04557505919657992 
		0.44269165254166537 0.45639985666166399 0.0084010284735052052 0.046932402968533564;
	setAttr -s 6 ".wl[309].w[0:5]"  6.2195962001637089e-010 0.045575064465417495 
		0.44269165547435363 0.45639984351738838 0.0084010291540247712 0.046932406766856095;
	setAttr -s 6 ".wl[310].w[0:5]"  6.2188365794683545e-010 0.045575061855174903 
		0.44269165805798494 0.4563998468351218 0.0084010285300153992 0.046932404099819199;
	setAttr -s 6 ".wl[311].w[0:5]"  6.2188375141858537e-010 0.04557506567630764 
		0.44269166722915337 0.45639985563847846 0.0084010293773573077 0.046932408014064793;
	setAttr -s 6 ".wl[312].w[0:5]"  6.2188387830888284e-010 0.045575067401719432 
		0.44269165810221073 0.45639984562512814 0.0084010298278542738 0.046932409771697436;
	setAttr -s 5 ".wl[313].w[1:5]"  0.045575071212183058 0.44269162346921842 
		0.4563998284135477 0.0084010316174194261 0.046932415776347346;
	setAttr -s 6 ".wl[314].w[0:5]"  6.2188402132053599e-010 0.045575081373533534 
		0.44269164622496743 0.45639982993761896 0.0084010331584652952 0.04693242405035325;
	setAttr -s 5 ".wl[315].w[1:5]"  0.045575079339439772 0.44269162007747553 
		0.45639982299635623 0.0084010335368060098 0.046932424084694821;
	setAttr -s 6 ".wl[316].w[0:5]"  6.2188420558341673e-010 0.045575086023880593 
		0.44269164163385061 0.45639982404367269 0.0084010342702821334 0.046932428802356173;
	setAttr -s 5 ".wl[317].w[1:5]"  0.04557508881584104 0.44269160603603613 
		0.45639980604563585 0.0084010358264225878 0.046932433764780283;
	setAttr -s 6 ".wl[318].w[0:5]"  6.2188428100577321e-010 0.045575095783768629 
		0.44269162999501255 0.45639980956176618 0.0084010366139509844 0.046932438774111324;
	setAttr -s 6 ".wl[319].w[0:5]"  6.2188329457325196e-010 0.045575096562621119 
		0.44269163650707377 0.45639981625088843 0.0084010367629100344 0.04693243957538222;
	setAttr -s 5 ".wl[320].w";
	setAttr ".wl[320].w[0]" 0.010433470359026193;
	setAttr ".wl[320].w[1]" 0.064924996840192206;
	setAttr ".wl[320].w[2]" 0.60683736494523099;
	setAttr ".wl[320].w[3]" 0.28676146597169011;
	setAttr ".wl[320].w[5]" 0.031042701883860598;
	setAttr -s 5 ".wl[321].w";
	setAttr ".wl[321].w[0]" 0.010433471001463177;
	setAttr ".wl[321].w[1]" 0.064924999727782734;
	setAttr ".wl[321].w[2]" 0.60683735613880463;
	setAttr ".wl[321].w[3]" 0.2867614696011595;
	setAttr ".wl[321].w[5]" 0.031042703530790073;
	setAttr -s 5 ".wl[322].w";
	setAttr ".wl[322].w[0]" 0.010433471340110677;
	setAttr ".wl[322].w[1]" 0.064925001477241354;
	setAttr ".wl[322].w[2]" 0.6068373535102084;
	setAttr ".wl[322].w[3]" 0.28676146953442322;
	setAttr ".wl[322].w[5]" 0.031042704138016252;
	setAttr -s 5 ".wl[323].w";
	setAttr ".wl[323].w[0]" 0.010433471628389354;
	setAttr ".wl[323].w[1]" 0.064925002485717059;
	setAttr ".wl[323].w[2]" 0.60683734701408798;
	setAttr ".wl[323].w[3]" 0.28676147366505222;
	setAttr ".wl[323].w[5]" 0.031042705206753424;
	setAttr -s 5 ".wl[324].w";
	setAttr ".wl[324].w[0]" 0.010433472244164264;
	setAttr ".wl[324].w[1]" 0.064925005471428043;
	setAttr ".wl[324].w[2]" 0.60683734050372629;
	setAttr ".wl[324].w[3]" 0.28676147524551915;
	setAttr ".wl[324].w[5]" 0.03104270653516239;
	setAttr -s 5 ".wl[325].w";
	setAttr ".wl[325].w[0]" 0.010433473373519086;
	setAttr ".wl[325].w[1]" 0.064925010171263883;
	setAttr ".wl[325].w[2]" 0.60683732168939619;
	setAttr ".wl[325].w[3]" 0.28676148490354314;
	setAttr ".wl[325].w[5]" 0.031042709862277678;
	setAttr -s 5 ".wl[326].w";
	setAttr ".wl[326].w[0]" 0.010433474400008943;
	setAttr ".wl[326].w[1]" 0.064925015144227591;
	setAttr ".wl[326].w[2]" 0.6068373107996512;
	setAttr ".wl[326].w[3]" 0.28676148757459125;
	setAttr ".wl[326].w[5]" 0.031042712081521047;
	setAttr -s 5 ".wl[327].w";
	setAttr ".wl[327].w[0]" 0.010433474653109715;
	setAttr ".wl[327].w[1]" 0.064925016056970195;
	setAttr ".wl[327].w[2]" 0.60683730533830194;
	setAttr ".wl[327].w[3]" 0.28676149096314268;
	setAttr ".wl[327].w[5]" 0.031042712988475493;
	setAttr -s 5 ".wl[328].w";
	setAttr ".wl[328].w[0]" 0.010433475934729505;
	setAttr ".wl[328].w[1]" 0.064925022091621612;
	setAttr ".wl[328].w[2]" 0.60683729019789501;
	setAttr ".wl[328].w[3]" 0.28676149581636723;
	setAttr ".wl[328].w[5]" 0.031042715959386638;
	setAttr -s 5 ".wl[329].w";
	setAttr ".wl[329].w[0]" 0.010433477270343081;
	setAttr ".wl[329].w[1]" 0.064925027854642714;
	setAttr ".wl[329].w[2]" 0.60683726976177033;
	setAttr ".wl[329].w[3]" 0.2867615054542042;
	setAttr ".wl[329].w[5]" 0.031042719659039542;
	setAttr -s 5 ".wl[330].w";
	setAttr ".wl[330].w[0]" 0.010433476456244175;
	setAttr ".wl[330].w[1]" 0.064925024201850992;
	setAttr ".wl[330].w[2]" 0.60683728097776601;
	setAttr ".wl[330].w[3]" 0.28676150079941137;
	setAttr ".wl[330].w[5]" 0.03104271756472738;
	setAttr -s 5 ".wl[331].w";
	setAttr ".wl[331].w[0]" 0.0104334772698539;
	setAttr ".wl[331].w[1]" 0.064925027851151687;
	setAttr ".wl[331].w[2]" 0.60683726971838359;
	setAttr ".wl[331].w[3]" 0.28676150543749479;
	setAttr ".wl[331].w[5]" 0.031042719657632341;
	setAttr -s 5 ".wl[332].w";
	setAttr ".wl[332].w[0]" 0.010433477865426472;
	setAttr ".wl[332].w[1]" 0.064925030247792517;
	setAttr ".wl[332].w[2]" 0.6068372500928001;
	setAttr ".wl[332].w[3]" 0.28676150538850897;
	setAttr ".wl[332].w[5]" 0.031042721125960994;
	setAttr -s 5 ".wl[333].w";
	setAttr ".wl[333].w[0]" 0.010433480190313116;
	setAttr ".wl[333].w[1]" 0.06492504101904735;
	setAttr ".wl[333].w[2]" 0.6068372321497395;
	setAttr ".wl[333].w[3]" 0.28676152294729484;
	setAttr ".wl[333].w[5]" 0.03104272718606492;
	setAttr -s 5 ".wl[334].w";
	setAttr ".wl[334].w[0]" 0.010433482208295273;
	setAttr ".wl[334].w[1]" 0.064925049806552865;
	setAttr ".wl[334].w[2]" 0.60683719329156194;
	setAttr ".wl[334].w[3]" 0.28676153114362668;
	setAttr ".wl[334].w[5]" 0.031042732315884846;
	setAttr -s 5 ".wl[335].w";
	setAttr ".wl[335].w[0]" 0.010433482688772257;
	setAttr ".wl[335].w[1]" 0.064925052401452424;
	setAttr ".wl[335].w[2]" 0.606837204868378;
	setAttr ".wl[335].w[3]" 0.28676153939696469;
	setAttr ".wl[335].w[5]" 0.031042733653844728;
	setAttr -s 5 ".wl[336].w";
	setAttr ".wl[336].w[0]" 0.010433483658305804;
	setAttr ".wl[336].w[1]" 0.064925056312427301;
	setAttr ".wl[336].w[2]" 0.60683717331276499;
	setAttr ".wl[336].w[3]" 0.28676153943608568;
	setAttr ".wl[336].w[5]" 0.031042736046337609;
	setAttr -s 5 ".wl[337].w";
	setAttr ".wl[337].w[0]" 0.010433485680519126;
	setAttr ".wl[337].w[1]" 0.064925065651852534;
	setAttr ".wl[337].w[2]" 0.60683715648174608;
	setAttr ".wl[337].w[3]" 0.28676155433860195;
	setAttr ".wl[337].w[5]" 0.031042741310636168;
	setAttr -s 5 ".wl[338].w";
	setAttr ".wl[338].w[0]" 0.010433486718127521;
	setAttr ".wl[338].w[1]" 0.06492506996868315;
	setAttr ".wl[338].w[2]" 0.60683712814967805;
	setAttr ".wl[338].w[3]" 0.2867615560261022;
	setAttr ".wl[338].w[5]" 0.031042743901553874;
	setAttr -s 5 ".wl[339].w";
	setAttr ".wl[339].w[0]" 0.0104334869042913;
	setAttr ".wl[339].w[1]" 0.064925071073853452;
	setAttr ".wl[339].w[2]" 0.60683713676936035;
	setAttr ".wl[339].w[3]" 0.28676156047471069;
	setAttr ".wl[339].w[5]" 0.031042744443090201;
	setAttr -s 5 ".wl[340].w";
	setAttr ".wl[340].w[0]" 0.013028722698424014;
	setAttr ".wl[340].w[1]" 0.091702862263379925;
	setAttr ".wl[340].w[2]" 0.70512456630622788;
	setAttr ".wl[340].w[3]" 0.16979432409595488;
	setAttr ".wl[340].w[5]" 0.02034952463601318;
	setAttr -s 5 ".wl[341].w";
	setAttr ".wl[341].w[0]" 0.013028723581541472;
	setAttr ".wl[341].w[1]" 0.091702866466460239;
	setAttr ".wl[341].w[2]" 0.70512455434542576;
	setAttr ".wl[341].w[3]" 0.16979432966327856;
	setAttr ".wl[341].w[5]" 0.020349525943293964;
	setAttr -s 5 ".wl[342].w";
	setAttr ".wl[342].w[0]" 0.013028724061856891;
	setAttr ".wl[342].w[1]" 0.091702869154059424;
	setAttr ".wl[342].w[2]" 0.70512454900613108;
	setAttr ".wl[342].w[3]" 0.16979433131354046;
	setAttr ".wl[342].w[5]" 0.020349526464412036;
	setAttr -s 5 ".wl[343].w";
	setAttr ".wl[343].w[0]" 0.013028724439289241;
	setAttr ".wl[343].w[1]" 0.091702870442048806;
	setAttr ".wl[343].w[2]" 0.70512454241829159;
	setAttr ".wl[343].w[3]" 0.16979433543687544;
	setAttr ".wl[343].w[5]" 0.020349527263494874;
	setAttr -s 5 ".wl[344].w";
	setAttr ".wl[344].w[0]" 0.013028725300142303;
	setAttr ".wl[344].w[1]" 0.091702874925382274;
	setAttr ".wl[344].w[2]" 0.70512453188039081;
	setAttr ".wl[344].w[3]" 0.16979433953888676;
	setAttr ".wl[344].w[5]" 0.020349528355197769;
	setAttr -s 5 ".wl[345].w";
	setAttr ".wl[345].w[0]" 0.013028726827996795;
	setAttr ".wl[345].w[1]" 0.091702881531578795;
	setAttr ".wl[345].w[2]" 0.70512450925536796;
	setAttr ".wl[345].w[3]" 0.16979435145353231;
	setAttr ".wl[345].w[5]" 0.020349530931524043;
	setAttr -s 5 ".wl[346].w";
	setAttr ".wl[346].w[0]" 0.013028728262402088;
	setAttr ".wl[346].w[1]" 0.0917028889927895;
	setAttr ".wl[346].w[2]" 0.70512449166980506;
	setAttr ".wl[346].w[3]" 0.16979435832007311;
	setAttr ".wl[346].w[5]" 0.02034953275493015;
	setAttr -s 5 ".wl[347].w";
	setAttr ".wl[347].w[0]" 0.013028728595754904;
	setAttr ".wl[347].w[1]" 0.091702890182465358;
	setAttr ".wl[347].w[2]" 0.70512448600263955;
	setAttr ".wl[347].w[3]" 0.16979436178308949;
	setAttr ".wl[347].w[5]" 0.020349533436050796;
	setAttr -s 5 ".wl[348].w";
	setAttr ".wl[348].w[0]" 0.013028730375311577;
	setAttr ".wl[348].w[1]" 0.091702899135980634;
	setAttr ".wl[348].w[2]" 0.70512446330573897;
	setAttr ".wl[348].w[3]" 0.16979437134146969;
	setAttr ".wl[348].w[5]" 0.020349535841499008;
	setAttr -s 5 ".wl[349].w";
	setAttr ".wl[349].w[0]" 0.013028732195729255;
	setAttr ".wl[349].w[1]" 0.09170290737605212;
	setAttr ".wl[349].w[2]" 0.70512443741936071;
	setAttr ".wl[349].w[3]" 0.16979438427212371;
	setAttr ".wl[349].w[5]" 0.020349538736734049;
	setAttr -s 5 ".wl[350].w";
	setAttr ".wl[350].w[0]" 0.013028731077051334;
	setAttr ".wl[350].w[1]" 0.091702902063100541;
	setAttr ".wl[350].w[2]" 0.7051244526032;
	setAttr ".wl[350].w[3]" 0.16979437718121265;
	setAttr ".wl[350].w[5]" 0.020349537075435332;
	setAttr -s 5 ".wl[351].w";
	setAttr ".wl[351].w[0]" 0.013028732195230317;
	setAttr ".wl[351].w[1]" 0.091702907371751602;
	setAttr ".wl[351].w[2]" 0.70512443737423014;
	setAttr ".wl[351].w[3]" 0.16979438426455321;
	setAttr ".wl[351].w[5]" 0.020349538736026948;
	setAttr -s 5 ".wl[352].w";
	setAttr ".wl[352].w[0]" 0.01302873303342649;
	setAttr ".wl[352].w[1]" 0.091702910898445789;
	setAttr ".wl[352].w[2]" 0.70512441257221525;
	setAttr ".wl[352].w[3]" 0.16979438825076021;
	setAttr ".wl[352].w[5]" 0.020349539965641254;
	setAttr -s 5 ".wl[353].w";
	setAttr ".wl[353].w[0]" 0.013028736203546712;
	setAttr ".wl[353].w[1]" 0.091702926513708885;
	setAttr ".wl[353].w[2]" 0.70512438609882966;
	setAttr ".wl[353].w[3]" 0.16979440998389453;
	setAttr ".wl[353].w[5]" 0.020349544692479838;
	setAttr -s 5 ".wl[354].w";
	setAttr ".wl[354].w[0]" 0.013028738995763355;
	setAttr ".wl[354].w[1]" 0.091702939335071607;
	setAttr ".wl[354].w[2]" 0.70512433521024576;
	setAttr ".wl[354].w[3]" 0.1697944264002624;
	setAttr ".wl[354].w[5]" 0.020349548824578352;
	setAttr -s 5 ".wl[355].w";
	setAttr ".wl[355].w[0]" 0.013028739624283359;
	setAttr ".wl[355].w[1]" 0.091702943043126192;
	setAttr ".wl[355].w[2]" 0.70512434806105262;
	setAttr ".wl[355].w[3]" 0.16979443249868748;
	setAttr ".wl[355].w[5]" 0.020349549782262465;
	setAttr -s 5 ".wl[356].w";
	setAttr ".wl[356].w[0]" 0.013028740988253773;
	setAttr ".wl[356].w[1]" 0.091702948797681594;
	setAttr ".wl[356].w[2]" 0.7051243081651356;
	setAttr ".wl[356].w[3]" 0.16979443903114949;
	setAttr ".wl[356].w[5]" 0.020349551783700941;
	setAttr -s 5 ".wl[357].w";
	setAttr ".wl[357].w[0]" 0.013028743748173234;
	setAttr ".wl[357].w[1]" 0.091702962344174466;
	setAttr ".wl[357].w[2]" 0.70512428369168345;
	setAttr ".wl[357].w[3]" 0.16979445781113955;
	setAttr ".wl[357].w[5]" 0.02034955589728895;
	setAttr -s 5 ".wl[358].w";
	setAttr ".wl[358].w[0]" 0.013028745198054872;
	setAttr ".wl[358].w[1]" 0.091702968671237325;
	setAttr ".wl[358].w[2]" 0.70512424749387459;
	setAttr ".wl[358].w[3]" 0.169794465369145;
	setAttr ".wl[358].w[5]" 0.020349558031832964;
	setAttr -s 5 ".wl[359].w";
	setAttr ".wl[359].w[0]" 0.013028745434373828;
	setAttr ".wl[359].w[1]" 0.091702970238015338;
	setAttr ".wl[359].w[2]" 0.70512425742857476;
	setAttr ".wl[359].w[3]" 0.16979446816664065;
	setAttr ".wl[359].w[5]" 0.020349558397701459;
	setAttr -s 5 ".wl[360].w";
	setAttr ".wl[360].w[0]" 0.017584350843940447;
	setAttr ".wl[360].w[1]" 0.14010905309625082;
	setAttr ".wl[360].w[2]" 0.7210158586784402;
	setAttr ".wl[360].w[3]" 0.10683385675648394;
	setAttr ".wl[360].w[5]" 0.014456880624884623;
	setAttr -s 5 ".wl[361].w";
	setAttr ".wl[361].w[0]" 0.017584352028028844;
	setAttr ".wl[361].w[1]" 0.14010905855533878;
	setAttr ".wl[361].w[2]" 0.72101584631941529;
	setAttr ".wl[361].w[3]" 0.10683386148116865;
	setAttr ".wl[361].w[5]" 0.014456881616048448;
	setAttr -s 5 ".wl[362].w";
	setAttr ".wl[362].w[0]" 0.017584352710156154;
	setAttr ".wl[362].w[1]" 0.14010906250942648;
	setAttr ".wl[362].w[2]" 0.72101583955940263;
	setAttr ".wl[362].w[3]" 0.10683386318972897;
	setAttr ".wl[362].w[5]" 0.014456882031285818;
	setAttr -s 5 ".wl[363].w";
	setAttr ".wl[363].w[0]" 0.017584353168208798;
	setAttr ".wl[363].w[1]" 0.14010906359838574;
	setAttr ".wl[363].w[2]" 0.7210158343237284;
	setAttr ".wl[363].w[3]" 0.10683386629810697;
	setAttr ".wl[363].w[5]" 0.014456882611570269;
	setAttr -s 5 ".wl[364].w";
	setAttr ".wl[364].w[0]" 0.017584354359014447;
	setAttr ".wl[364].w[1]" 0.14010906986612076;
	setAttr ".wl[364].w[2]" 0.72101582224031724;
	setAttr ".wl[364].w[3]" 0.10683387007586911;
	setAttr ".wl[364].w[5]" 0.014456883458678651;
	setAttr -s 5 ".wl[365].w";
	setAttr ".wl[365].w[0]" 0.017584356344808524;
	setAttr ".wl[365].w[1]" 0.14010907768301684;
	setAttr ".wl[365].w[2]" 0.72101580091844575;
	setAttr ".wl[365].w[3]" 0.10683387967521339;
	setAttr ".wl[365].w[5]" 0.014456885378515392;
	setAttr -s 5 ".wl[366].w";
	setAttr ".wl[366].w[0]" 0.017584358328383558;
	setAttr ".wl[366].w[1]" 0.14010908810692088;
	setAttr ".wl[366].w[2]" 0.72101578078325645;
	setAttr ".wl[366].w[3]" 0.10683388598867929;
	setAttr ".wl[366].w[5]" 0.014456886792759789;
	setAttr -s 5 ".wl[367].w";
	setAttr ".wl[367].w[0]" 0.01758435873761437;
	setAttr ".wl[367].w[1]" 0.14010908919354728;
	setAttr ".wl[367].w[2]" 0.72101577615619272;
	setAttr ".wl[367].w[3]" 0.10683388862334169;
	setAttr ".wl[367].w[5]" 0.014456887289303926;
	setAttr -s 5 ".wl[368].w";
	setAttr ".wl[368].w[0]" 0.017584361169659439;
	setAttr ".wl[368].w[1]" 0.14010910138179081;
	setAttr ".wl[368].w[2]" 0.7210157512052392;
	setAttr ".wl[368].w[3]" 0.10683389710599156;
	setAttr ".wl[368].w[5]" 0.014456889137318945;
	setAttr -s 5 ".wl[369].w";
	setAttr ".wl[369].w[0]" 0.017584363570441061;
	setAttr ".wl[369].w[1]" 0.14010911159722381;
	setAttr ".wl[369].w[2]" 0.72101572576764827;
	setAttr ".wl[369].w[3]" 0.1068339077535614;
	setAttr ".wl[369].w[5]" 0.014456891311125467;
	setAttr -s 5 ".wl[370].w";
	setAttr ".wl[370].w[0]" 0.017584362071483631;
	setAttr ".wl[370].w[1]" 0.14010910470853921;
	setAttr ".wl[370].w[2]" 0.72101574142294811;
	setAttr ".wl[370].w[3]" 0.10683390174488107;
	setAttr ".wl[370].w[5]" 0.014456890052148031;
	setAttr -s 5 ".wl[371].w";
	setAttr ".wl[371].w[0]" 0.01758436356987467;
	setAttr ".wl[371].w[1]" 0.1401091115912084;
	setAttr ".wl[371].w[2]" 0.72101572572731298;
	setAttr ".wl[371].w[3]" 0.1068339077499311;
	setAttr ".wl[371].w[5]" 0.014456891310741175;
	setAttr -s 5 ".wl[372].w";
	setAttr ".wl[372].w[0]" 0.017584364691186863;
	setAttr ".wl[372].w[1]" 0.1401091158418494;
	setAttr ".wl[372].w[2]" 0.7210157002523675;
	setAttr ".wl[372].w[3]" 0.10683391169228308;
	setAttr ".wl[372].w[5]" 0.014456892257354142;
	setAttr -s 5 ".wl[373].w";
	setAttr ".wl[373].w[0]" 0.017584368941020913;
	setAttr ".wl[373].w[1]" 0.14010913648384074;
	setAttr ".wl[373].w[2]" 0.72101567283537238;
	setAttr ".wl[373].w[3]" 0.10683392941108681;
	setAttr ".wl[373].w[5]" 0.014456895821138932;
	setAttr -s 5 ".wl[374].w";
	setAttr ".wl[374].w[0]" 0.017584372680499113;
	setAttr ".wl[374].w[1]" 0.14010915279487521;
	setAttr ".wl[374].w[2]" 0.72101562045669565;
	setAttr ".wl[374].w[3]" 0.10683394386711727;
	setAttr ".wl[374].w[5]" 0.014456898966734194;
	setAttr -s 5 ".wl[375].w";
	setAttr ".wl[375].w[0]" 0.017584373525742252;
	setAttr ".wl[375].w[1]" 0.1401091581167857;
	setAttr ".wl[375].w[2]" 0.72101563356115816;
	setAttr ".wl[375].w[3]" 0.10683394813661946;
	setAttr ".wl[375].w[5]" 0.014456899669106679;
	setAttr -s 5 ".wl[376].w";
	setAttr ".wl[376].w[0]" 0.017584375350276914;
	setAttr ".wl[376].w[1]" 0.14010916506353585;
	setAttr ".wl[376].w[2]" 0.72101559257290115;
	setAttr ".wl[376].w[3]" 0.10683395456998687;
	setAttr ".wl[376].w[5]" 0.01445690120922059;
	setAttr -s 5 ".wl[377].w";
	setAttr ".wl[377].w[0]" 0.017584379049705348;
	setAttr ".wl[377].w[1]" 0.14010918293542643;
	setAttr ".wl[377].w[2]" 0.72101556723153726;
	setAttr ".wl[377].w[3]" 0.10683396993472459;
	setAttr ".wl[377].w[5]" 0.014456904311962235;
	setAttr -s 5 ".wl[378].w";
	setAttr ".wl[378].w[0]" 0.017584380990565824;
	setAttr ".wl[378].w[1]" 0.14010919074552367;
	setAttr ".wl[378].w[2]" 0.72101553004409957;
	setAttr ".wl[378].w[3]" 0.10683397703590755;
	setAttr ".wl[378].w[5]" 0.014456905948048196;
	setAttr -s 5 ".wl[379].w";
	setAttr ".wl[379].w[0]" 0.017584381309105359;
	setAttr ".wl[379].w[1]" 0.14010919309300701;
	setAttr ".wl[379].w[2]" 0.72101554019784531;
	setAttr ".wl[379].w[3]" 0.10683397885440807;
	setAttr ".wl[379].w[5]" 0.014456906210940134;
	setAttr -s 5 ".wl[380].w";
	setAttr ".wl[380].w[0]" 0.026218496477293358;
	setAttr ".wl[380].w[1]" 0.23369910993082266;
	setAttr ".wl[380].w[2]" 0.65480615353380534;
	setAttr ".wl[380].w[3]" 0.073943570698888059;
	setAttr ".wl[380].w[5]" 0.011332669359190624;
	setAttr -s 5 ".wl[381].w";
	setAttr ".wl[381].w[0]" 0.026218497997349696;
	setAttr ".wl[381].w[1]" 0.23369911491610679;
	setAttr ".wl[381].w[2]" 0.65480614296456019;
	setAttr ".wl[381].w[3]" 0.073943574036880594;
	setAttr ".wl[381].w[5]" 0.011332670085102718;
	setAttr -s 5 ".wl[382].w";
	setAttr ".wl[382].w[0]" 0.026218498916647719;
	setAttr ".wl[382].w[1]" 0.23369911954058764;
	setAttr ".wl[382].w[2]" 0.65480613587894276;
	setAttr ".wl[382].w[3]" 0.073943575273800216;
	setAttr ".wl[382].w[5]" 0.011332670390021612;
	setAttr -s 5 ".wl[383].w";
	setAttr ".wl[383].w[0]" 0.026218499449458189;
	setAttr ".wl[383].w[1]" 0.23369911925320058;
	setAttr ".wl[383].w[2]" 0.65480613305105928;
	setAttr ".wl[383].w[3]" 0.073943577432277724;
	setAttr ".wl[383].w[5]" 0.011332670814004219;
	setAttr -s 5 ".wl[384].w";
	setAttr ".wl[384].w[0]" 0.026218501019764882;
	setAttr ".wl[384].w[1]" 0.23369912594774073;
	setAttr ".wl[384].w[2]" 0.654806121466878;
	setAttr ".wl[384].w[3]" 0.073943580130381492;
	setAttr ".wl[384].w[5]" 0.011332671435234701;
	setAttr -s 5 ".wl[385].w";
	setAttr ".wl[385].w[0]" 0.026218503496001959;
	setAttr ".wl[385].w[1]" 0.23369913140065166;
	setAttr ".wl[385].w[2]" 0.65480610539896433;
	setAttr ".wl[385].w[3]" 0.073943586864288202;
	setAttr ".wl[385].w[5]" 0.011332672840093721;
	setAttr -s 5 ".wl[386].w";
	setAttr ".wl[386].w[0]" 0.026218506111509391;
	setAttr ".wl[386].w[1]" 0.23369914252358842;
	setAttr ".wl[386].w[2]" 0.65480608611617441;
	setAttr ".wl[386].w[3]" 0.073943591371618905;
	setAttr ".wl[386].w[5]" 0.011332673877108774;
	setAttr -s 5 ".wl[387].w";
	setAttr ".wl[387].w[0]" 0.026218506593341771;
	setAttr ".wl[387].w[1]" 0.23369914250965651;
	setAttr ".wl[387].w[2]" 0.65480608345286784;
	setAttr ".wl[387].w[3]" 0.073943593204100558;
	setAttr ".wl[387].w[5]" 0.011332674240033204;
	setAttr -s 5 ".wl[388].w";
	setAttr ".wl[388].w[0]" 0.026218509768025002;
	setAttr ".wl[388].w[1]" 0.2336991548618578;
	setAttr ".wl[388].w[2]" 0.65480606054257817;
	setAttr ".wl[388].w[3]" 0.073943599233075807;
	setAttr ".wl[388].w[5]" 0.011332675594463253;
	setAttr -s 5 ".wl[389].w";
	setAttr ".wl[389].w[0]" 0.026218512803280573;
	setAttr ".wl[389].w[1]" 0.2336991631142972;
	setAttr ".wl[389].w[2]" 0.65480604017137845;
	setAttr ".wl[389].w[3]" 0.073943606725254352;
	setAttr ".wl[389].w[5]" 0.011332677185789508;
	setAttr -s 5 ".wl[390].w";
	setAttr ".wl[390].w[0]" 0.026218510880458006;
	setAttr ".wl[390].w[1]" 0.23369915685389248;
	setAttr ".wl[390].w[2]" 0.65480605352138643;
	setAttr ".wl[390].w[3]" 0.073943602480546405;
	setAttr ".wl[390].w[5]" 0.011332676263716686;
	setAttr -s 5 ".wl[391].w";
	setAttr ".wl[391].w[0]" 0.026218512801964692;
	setAttr ".wl[391].w[1]" 0.2336991630995173;
	setAttr ".wl[391].w[2]" 0.65480604012605226;
	setAttr ".wl[391].w[3]" 0.073943606721677366;
	setAttr ".wl[391].w[5]" 0.011332677185304856;
	setAttr -s 5 ".wl[392].w";
	setAttr ".wl[392].w[0]" 0.026218514184624162;
	setAttr ".wl[392].w[1]" 0.23369916534372623;
	setAttr ".wl[392].w[2]" 0.65480601779497349;
	setAttr ".wl[392].w[3]" 0.073943609529889251;
	setAttr ".wl[392].w[5]" 0.011332677867275704;
	setAttr -s 5 ".wl[393].w";
	setAttr ".wl[393].w[0]" 0.026218519705208797;
	setAttr ".wl[393].w[1]" 0.2336991861003796;
	setAttr ".wl[393].w[2]" 0.65480599517598859;
	setAttr ".wl[393].w[3]" 0.073943622019368896;
	setAttr ".wl[393].w[5]" 0.011332680491513768;
	setAttr -s 5 ".wl[394].w";
	setAttr ".wl[394].w[0]" 0.026218524448129606;
	setAttr ".wl[394].w[1]" 0.23369919935600789;
	setAttr ".wl[394].w[2]" 0.65480594992342278;
	setAttr ".wl[394].w[3]" 0.073943632253983621;
	setAttr ".wl[394].w[5]" 0.011332682784377688;
	setAttr -s 5 ".wl[395].w";
	setAttr ".wl[395].w[0]" 0.026218525621152802;
	setAttr ".wl[395].w[1]" 0.23369920677114397;
	setAttr ".wl[395].w[2]" 0.65480596206721131;
	setAttr ".wl[395].w[3]" 0.073943635233061536;
	setAttr ".wl[395].w[5]" 0.011332683316842633;
	setAttr -s 5 ".wl[396].w";
	setAttr ".wl[396].w[0]" 0.026218527872811238;
	setAttr ".wl[396].w[1]" 0.23369921050482576;
	setAttr ".wl[396].w[2]" 0.65480592614673383;
	setAttr ".wl[396].w[3]" 0.07394363981478054;
	setAttr ".wl[396].w[5]" 0.011332684426770141;
	setAttr -s 5 ".wl[397].w";
	setAttr ".wl[397].w[0]" 0.026218532672108649;
	setAttr ".wl[397].w[1]" 0.23369922830892306;
	setAttr ".wl[397].w[2]" 0.6548059051257622;
	setAttr ".wl[397].w[3]" 0.073943650646408288;
	setAttr ".wl[397].w[5]" 0.011332686710153739;
	setAttr -s 5 ".wl[398].w";
	setAttr ".wl[398].w[0]" 0.026218535092906677;
	setAttr ".wl[398].w[1]" 0.23369923341353982;
	setAttr ".wl[398].w[2]" 0.65480587265846268;
	setAttr ".wl[398].w[3]" 0.073943655690349899;
	setAttr ".wl[398].w[5]" 0.01133268789433369;
	setAttr -s 5 ".wl[399].w";
	setAttr ".wl[399].w[0]" 0.026218535556465864;
	setAttr ".wl[399].w[1]" 0.23369923713532009;
	setAttr ".wl[399].w[2]" 0.65480588192207279;
	setAttr ".wl[399].w[3]" 0.073943656953313397;
	setAttr ".wl[399].w[5]" 0.011332688098133726;
	setAttr -s 5 ".wl[400].w";
	setAttr ".wl[400].w[0]" 0.040221543448771817;
	setAttr ".wl[400].w[1]" 0.38674464790117868;
	setAttr ".wl[400].w[2]" 0.51127996262977438;
	setAttr ".wl[400].w[3]" 0.052658857309655124;
	setAttr ".wl[400].w[5]" 0.0090949887106201565;
	setAttr -s 5 ".wl[401].w";
	setAttr ".wl[401].w[0]" 0.040221545349433376;
	setAttr ".wl[401].w[1]" 0.38674464818310728;
	setAttr ".wl[401].w[2]" 0.51127995760745681;
	setAttr ".wl[401].w[3]" 0.05265885961609957;
	setAttr ".wl[401].w[5]" 0.0090949892439029928;
	setAttr -s 5 ".wl[402].w";
	setAttr ".wl[402].w[0]" 0.040221546511702594;
	setAttr ".wl[402].w[1]" 0.38674465094657368;
	setAttr ".wl[402].w[2]" 0.51127995264649373;
	setAttr ".wl[402].w[3]" 0.052658860435947918;
	setAttr ".wl[402].w[5]" 0.0090949894592820962;
	setAttr -s 5 ".wl[403].w";
	setAttr ".wl[403].w[0]" 0.040221547161842425;
	setAttr ".wl[403].w[1]" 0.38674464776802925;
	setAttr ".wl[403].w[2]" 0.51127995331714815;
	setAttr ".wl[403].w[3]" 0.05265886197132931;
	setAttr ".wl[403].w[5]" 0.0090949897816508651;
	setAttr -s 5 ".wl[404].w";
	setAttr ".wl[404].w[0]" 0.040221549137930079;
	setAttr ".wl[404].w[1]" 0.38674465055053103;
	setAttr ".wl[404].w[2]" 0.51127994627990692;
	setAttr ".wl[404].w[3]" 0.052658863801917741;
	setAttr ".wl[404].w[5]" 0.0090949902297143281;
	setAttr -s 5 ".wl[405].w";
	setAttr ".wl[405].w[0]" 0.040221552212918954;
	setAttr ".wl[405].w[1]" 0.38674464671035114;
	setAttr ".wl[405].w[2]" 0.5112799412880199;
	setAttr ".wl[405].w[3]" 0.0526588685126234;
	setAttr ".wl[405].w[5]" 0.0090949912760865583;
	setAttr -s 5 ".wl[406].w";
	setAttr ".wl[406].w[0]" 0.040221555504074677;
	setAttr ".wl[406].w[1]" 0.38674465130054847;
	setAttr ".wl[406].w[2]" 0.51127992959967594;
	setAttr ".wl[406].w[3]" 0.052658871571487111;
	setAttr ".wl[406].w[5]" 0.0090949920242137921;
	setAttr -s 5 ".wl[407].w";
	setAttr ".wl[407].w[0]" 0.040221556093750832;
	setAttr ".wl[407].w[1]" 0.3867446488203295;
	setAttr ".wl[407].w[2]" 0.51127992991423898;
	setAttr ".wl[407].w[3]" 0.052658872872288529;
	setAttr ".wl[407].w[5]" 0.009094992299392134;
	setAttr -s 5 ".wl[408].w";
	setAttr ".wl[408].w[0]" 0.04022156007900634;
	setAttr ".wl[408].w[1]" 0.38674465253742585;
	setAttr ".wl[408].w[2]" 0.5112799171036847;
	setAttr ".wl[408].w[3]" 0.052658876995903887;
	setAttr ".wl[408].w[5]" 0.00909499328397936;
	setAttr -s 5 ".wl[409].w";
	setAttr ".wl[409].w[0]" 0.040221563861358611;
	setAttr ".wl[409].w[1]" 0.38674465036406069;
	setAttr ".wl[409].w[2]" 0.51127990910350252;
	setAttr ".wl[409].w[3]" 0.052658882209002535;
	setAttr ".wl[409].w[5]" 0.00909499446207555;
	setAttr -s 5 ".wl[410].w";
	setAttr ".wl[410].w[0]" 0.040221561457003889;
	setAttr ".wl[410].w[1]" 0.38674465007701714;
	setAttr ".wl[410].w[2]" 0.51127991540601936;
	setAttr ".wl[410].w[3]" 0.052658879275466142;
	setAttr ".wl[410].w[5]" 0.0090949937844934554;
	setAttr -s 5 ".wl[411].w";
	setAttr ".wl[411].w[0]" 0.040221563858952446;
	setAttr ".wl[411].w[1]" 0.3867446503349829;
	setAttr ".wl[411].w[2]" 0.51127990907218179;
	setAttr ".wl[411].w[3]" 0.052658882206693486;
	setAttr ".wl[411].w[5]" 0.0090949944617056602;
	setAttr -s 5 ".wl[412].w";
	setAttr ".wl[412].w[0]" 0.040221565474468465;
	setAttr ".wl[412].w[1]" 0.38674464471346109;
	setAttr ".wl[412].w[2]" 0.51127989545731711;
	setAttr ".wl[412].w[3]" 0.052658884124031483;
	setAttr ".wl[412].w[5]" 0.0090949949512110044;
	setAttr -s 5 ".wl[413].w";
	setAttr ".wl[413].w[0]" 0.040221572515295768;
	setAttr ".wl[413].w[1]" 0.38674465270284858;
	setAttr ".wl[413].w[2]" 0.51127988856741724;
	setAttr ".wl[413].w[3]" 0.052658892783937865;
	setAttr ".wl[413].w[5]" 0.0090949968938563476;
	setAttr -s 5 ".wl[414].w";
	setAttr ".wl[414].w[0]" 0.040221578336902354;
	setAttr ".wl[414].w[1]" 0.38674464777419731;
	setAttr ".wl[414].w[2]" 0.51127986425054994;
	setAttr ".wl[414].w[3]" 0.052658899836448558;
	setAttr ".wl[414].w[5]" 0.0090949985678232988;
	setAttr -s 5 ".wl[415].w";
	setAttr ".wl[415].w[0]" 0.040221579983911591;
	setAttr ".wl[415].w[1]" 0.38674465722939549;
	setAttr ".wl[415].w[2]" 0.51127987488528892;
	setAttr ".wl[415].w[3]" 0.052658901933102596;
	setAttr ".wl[415].w[5]" 0.0090949989777135386;
	setAttr -s 5 ".wl[416].w";
	setAttr ".wl[416].w[0]" 0.040221582618738823;
	setAttr ".wl[416].w[1]" 0.38674464827864974;
	setAttr ".wl[416].w[2]" 0.51127985303151702;
	setAttr ".wl[416].w[3]" 0.052658905062221005;
	setAttr ".wl[416].w[5]" 0.0090949997747948787;
	setAttr -s 5 ".wl[417].w";
	setAttr ".wl[417].w[0]" 0.040221588728602035;
	setAttr ".wl[417].w[1]" 0.3867446546129738;
	setAttr ".wl[417].w[2]" 0.51127984608620169;
	setAttr ".wl[417].w[3]" 0.052658912571486902;
	setAttr ".wl[417].w[5]" 0.0090950014640915292;
	setAttr -s 5 ".wl[418].w";
	setAttr ".wl[418].w[0]" 0.040221591615463112;
	setAttr ".wl[418].w[1]" 0.38674464779874973;
	setAttr ".wl[418].w[2]" 0.5112798269730886;
	setAttr ".wl[418].w[3]" 0.052658916027891724;
	setAttr ".wl[418].w[5]" 0.009095002319847648;
	setAttr -s 5 ".wl[419].w";
	setAttr ".wl[419].w[0]" 0.040221592306909436;
	setAttr ".wl[419].w[1]" 0.38674465358644167;
	setAttr ".wl[419].w[2]" 0.51127983437287627;
	setAttr ".wl[419].w[3]" 0.052658916925101627;
	setAttr ".wl[419].w[5]" 0.0090950024812528792;
	setAttr -s 5 ".wl[420].w";
	setAttr ".wl[420].w[0]" 0.058595352607220437;
	setAttr ".wl[420].w[1]" 0.56204517544418897;
	setAttr ".wl[420].w[2]" 0.33686232687151491;
	setAttr ".wl[420].w[3]" 0.035621763358487282;
	setAttr ".wl[420].w[5]" 0.0068753817185883822;
	setAttr -s 5 ".wl[421].w";
	setAttr ".wl[421].w[0]" 0.058595355193537785;
	setAttr ".wl[421].w[1]" 0.56204516853782016;
	setAttr ".wl[421].w[2]" 0.33686232899393498;
	setAttr ".wl[421].w[3]" 0.035621765132726968;
	setAttr ".wl[421].w[5]" 0.0068753821419801631;
	setAttr -s 5 ".wl[422].w";
	setAttr ".wl[422].w[0]" 0.05859535675834978;
	setAttr ".wl[422].w[1]" 0.56204516721027664;
	setAttr ".wl[422].w[2]" 0.33686232794573351;
	setAttr ".wl[422].w[3]" 0.035621765774771441;
	setAttr ".wl[422].w[5]" 0.0068753823108686505;
	setAttr -s 5 ".wl[423].w";
	setAttr ".wl[423].w[0]" 0.058595357664205393;
	setAttr ".wl[423].w[1]" 0.56204516118790193;
	setAttr ".wl[423].w[2]" 0.33686233163693879;
	setAttr ".wl[423].w[3]" 0.035621766941482121;
	setAttr ".wl[423].w[5]" 0.0068753825694717937;
	setAttr -s 5 ".wl[424].w";
	setAttr ".wl[424].w[0]" 0.058595360337082784;
	setAttr ".wl[424].w[1]" 0.56204515678962241;
	setAttr ".wl[424].w[2]" 0.33686233158952522;
	setAttr ".wl[424].w[3]" 0.035621768360590958;
	setAttr ".wl[424].w[5]" 0.006875382923178552;
	setAttr -s 5 ".wl[425].w";
	setAttr ".wl[425].w[0]" 0.058595364549168472;
	setAttr ".wl[425].w[1]" 0.56204514081489076;
	setAttr ".wl[425].w[2]" 0.33686233891308637;
	setAttr ".wl[425].w[3]" 0.035621771965432265;
	setAttr ".wl[425].w[5]" 0.00687538375742207;
	setAttr -s 5 ".wl[426].w";
	setAttr ".wl[426].w[0]" 0.058595369001105686;
	setAttr ".wl[426].w[1]" 0.56204513344038942;
	setAttr ".wl[426].w[2]" 0.33686233887398603;
	setAttr ".wl[426].w[3]" 0.03562177433647154;
	setAttr ".wl[426].w[5]" 0.0068753843480471736;
	setAttr -s 5 ".wl[427].w";
	setAttr ".wl[427].w[0]" 0.058595369820111994;
	setAttr ".wl[427].w[1]" 0.5620451284281669;
	setAttr ".wl[427].w[2]" 0.33686234185727476;
	setAttr ".wl[427].w[3]" 0.035621775325837497;
	setAttr ".wl[427].w[5]" 0.0068753845686089273;
	setAttr -s 5 ".wl[428].w";
	setAttr ".wl[428].w[0]" 0.058595375223207451;
	setAttr ".wl[428].w[1]" 0.56204511744260055;
	setAttr ".wl[428].w[2]" 0.33686234347498789;
	setAttr ".wl[428].w[3]" 0.035621778511470539;
	setAttr ".wl[428].w[5]" 0.0068753853477335333;
	setAttr -s 5 ".wl[429].w";
	setAttr ".wl[429].w[0]" 0.058595380387395653;
	setAttr ".wl[429].w[1]" 0.56204510064127478;
	setAttr ".wl[429].w[2]" 0.33686235017620064;
	setAttr ".wl[429].w[3]" 0.035621782509815014;
	setAttr ".wl[429].w[5]" 0.0068753862853139875;
	setAttr -s 5 ".wl[430].w";
	setAttr ".wl[430].w[0]" 0.05859537711520673;
	setAttr ".wl[430].w[1]" 0.56204510945554775;
	setAttr ".wl[430].w[2]" 0.33686234742844179;
	setAttr ".wl[430].w[3]" 0.035621780253500532;
	setAttr ".wl[430].w[5]" 0.0068753857473032474;
	setAttr -s 5 ".wl[431].w";
	setAttr ".wl[431].w[0]" 0.058595380384319259;
	setAttr ".wl[431].w[1]" 0.56204510060350088;
	setAttr ".wl[431].w[2]" 0.33686235016027494;
	setAttr ".wl[431].w[3]" 0.035621782508601291;
	setAttr ".wl[431].w[5]" 0.0068753862850960438;
	setAttr -s 5 ".wl[432].w";
	setAttr ".wl[432].w[0]" 0.058595382523872808;
	setAttr ".wl[432].w[1]" 0.56204508387878949;
	setAttr ".wl[432].w[2]" 0.33686234758154621;
	setAttr ".wl[432].w[3]" 0.03562178405729003;
	setAttr ".wl[432].w[5]" 0.0068753866789905312;
	setAttr -s 5 ".wl[433].w";
	setAttr ".wl[433].w[0]" 0.058595392178373777;
	setAttr ".wl[433].w[1]" 0.56204507135432924;
	setAttr ".wl[433].w[2]" 0.33686236108915729;
	setAttr ".wl[433].w[3]" 0.0356217906264946;
	setAttr ".wl[433].w[5]" 0.0068753882150007772;
	setAttr -s 5 ".wl[434].w";
	setAttr ".wl[434].w[0]" 0.058595400044635815;
	setAttr ".wl[434].w[1]" 0.56204503957351448;
	setAttr ".wl[434].w[2]" 0.3368623634759339;
	setAttr ".wl[434].w[3]" 0.035621796122584572;
	setAttr ".wl[434].w[5]" 0.0068753895492527656;
	setAttr -s 5 ".wl[435].w";
	setAttr ".wl[435].w[0]" 0.05859540237961397;
	setAttr ".wl[435].w[1]" 0.56204505073511735;
	setAttr ".wl[435].w[2]" 0.33686237241147099;
	setAttr ".wl[435].w[3]" 0.035621797616889668;
	setAttr ".wl[435].w[5]" 0.0068753898663202187;
	setAttr -s 5 ".wl[436].w";
	setAttr ".wl[436].w[0]" 0.058595405872012764;
	setAttr ".wl[436].w[1]" 0.5620450238689495;
	setAttr ".wl[436].w[2]" 0.33686236837541528;
	setAttr ".wl[436].w[3]" 0.03562180014193158;
	setAttr ".wl[436].w[5]" 0.0068753905076124611;
	setAttr -s 5 ".wl[437].w";
	setAttr ".wl[437].w[0]" 0.058595414245622271;
	setAttr ".wl[437].w[1]" 0.562045011904865;
	setAttr ".wl[437].w[2]" 0.33686237965099997;
	setAttr ".wl[437].w[3]" 0.035621805846913025;
	setAttr ".wl[437].w[5]" 0.006875391844059494;
	setAttr -s 5 ".wl[438].w";
	setAttr ".wl[438].w[0]" 0.058595418103144677;
	setAttr ".wl[438].w[1]" 0.56204498803587344;
	setAttr ".wl[438].w[2]" 0.33686237751226034;
	setAttr ".wl[438].w[3]" 0.035621808597286891;
	setAttr ".wl[438].w[5]" 0.0068753925301312723;
	setAttr -s 5 ".wl[439].w";
	setAttr ".wl[439].w[0]" 0.058595419099207589;
	setAttr ".wl[439].w[1]" 0.5620449960744851;
	setAttr ".wl[439].w[2]" 0.33686238263315826;
	setAttr ".wl[439].w[3]" 0.035621809212912477;
	setAttr ".wl[439].w[5]" 0.0068753926528184123;
	setAttr -s 5 ".wl[440].w";
	setAttr ".wl[440].w[0]" 0.082481841308204032;
	setAttr ".wl[440].w[1]" 0.68814646513539157;
	setAttr ".wl[440].w[2]" 0.20112517620917428;
	setAttr ".wl[440].w[3]" 0.02327374579140104;
	setAttr ".wl[440].w[5]" 0.004972771555828974;
	setAttr -s 5 ".wl[441].w";
	setAttr ".wl[441].w[0]" 0.082481845131102779;
	setAttr ".wl[441].w[1]" 0.68814645399812968;
	setAttr ".wl[441].w[2]" 0.20112518173784036;
	setAttr ".wl[441].w[3]" 0.023273747223966537;
	setAttr ".wl[441].w[5]" 0.0049727719089605596;
	setAttr -s 5 ".wl[442].w";
	setAttr ".wl[442].w[0]" 0.082481847519395177;
	setAttr ".wl[442].w[1]" 0.68814644948750237;
	setAttr ".wl[442].w[2]" 0.20112518315319697;
	setAttr ".wl[442].w[3]" 0.023273747784290564;
	setAttr ".wl[442].w[5]" 0.0049727720556145775;
	setAttr -s 5 ".wl[443].w";
	setAttr ".wl[443].w[0]" 0.082481848763255622;
	setAttr ".wl[443].w[1]" 0.68814644277105785;
	setAttr ".wl[443].w[2]" 0.20112518752837999;
	setAttr ".wl[443].w[3]" 0.023273748673325257;
	setAttr ".wl[443].w[5]" 0.0049727722639810665;
	setAttr -s 5 ".wl[444].w";
	setAttr ".wl[444].w[0]" 0.082481852784638085;
	setAttr ".wl[444].w[1]" 0.68814643339943238;
	setAttr ".wl[444].w[2]" 0.20112519139156962;
	setAttr ".wl[444].w[3]" 0.023273749859749497;
	setAttr ".wl[444].w[5]" 0.0049727725646104099;
	setAttr -s 5 ".wl[445].w";
	setAttr ".wl[445].w[0]" 0.082481858884163595;
	setAttr ".wl[445].w[1]" 0.68814641156577183;
	setAttr ".wl[445].w[2]" 0.20112520359803548;
	setAttr ".wl[445].w[3]" 0.023273752701169652;
	setAttr ".wl[445].w[5]" 0.0049727732508594484;
	setAttr -s 5 ".wl[446].w";
	setAttr ".wl[446].w[0]" 0.082481865582831035;
	setAttr ".wl[446].w[1]" 0.68814639592053806;
	setAttr ".wl[446].w[2]" 0.20112521006179099;
	setAttr ".wl[446].w[3]" 0.023273754682165672;
	setAttr ".wl[446].w[5]" 0.0049727737526741814;
	setAttr -s 5 ".wl[447].w";
	setAttr ".wl[447].w[0]" 0.082481866718364064;
	setAttr ".wl[447].w[1]" 0.68814639018562151;
	setAttr ".wl[447].w[2]" 0.20112521372556474;
	setAttr ".wl[447].w[3]" 0.023273755439541376;
	setAttr ".wl[447].w[5]" 0.0049727739309082461;
	setAttr -s 5 ".wl[448].w";
	setAttr ".wl[448].w[0]" 0.082481874794306326;
	setAttr ".wl[448].w[1]" 0.68814636960709108;
	setAttr ".wl[448].w[2]" 0.20112522294825058;
	setAttr ".wl[448].w[3]" 0.023273758062575582;
	setAttr ".wl[448].w[5]" 0.0049727745877765246;
	setAttr -s 5 ".wl[449].w";
	setAttr ".wl[449].w[0]" 0.082481882346298399;
	setAttr ".wl[449].w[1]" 0.68814634501402516;
	setAttr ".wl[449].w[2]" 0.20112523602898963;
	setAttr ".wl[449].w[3]" 0.023273761246981588;
	setAttr ".wl[449].w[5]" 0.0049727753637052426;
	setAttr -s 5 ".wl[450].w";
	setAttr ".wl[450].w[0]" 0.082481877512625201;
	setAttr ".wl[450].w[1]" 0.68814635916563283;
	setAttr ".wl[450].w[2]" 0.20112522898052171;
	setAttr ".wl[450].w[3]" 0.023273759426120075;
	setAttr ".wl[450].w[5]" 0.0049727749151003411;
	setAttr -s 5 ".wl[451].w";
	setAttr ".wl[451].w[0]" 0.082481882340080664;
	setAttr ".wl[451].w[1]" 0.68814634495425375;
	setAttr ".wl[451].w[2]" 0.20112523601642743;
	setAttr ".wl[451].w[3]" 0.02327376124575185;
	setAttr ".wl[451].w[5]" 0.0049727753634508038;
	setAttr -s 5 ".wl[452].w";
	setAttr ".wl[452].w[0]" 0.08248188556435361;
	setAttr ".wl[452].w[1]" 0.68814632138131715;
	setAttr ".wl[452].w[2]" 0.20112523949194336;
	setAttr ".wl[452].w[3]" 0.023273762579316362;
	setAttr ".wl[452].w[5]" 0.0049727757035584862;
	setAttr -s 5 ".wl[453].w";
	setAttr ".wl[453].w[0]" 0.082481899751702351;
	setAttr ".wl[453].w[1]" 0.68814629728647614;
	setAttr ".wl[453].w[2]" 0.20112526170544345;
	setAttr ".wl[453].w[3]" 0.023273767778644015;
	setAttr ".wl[453].w[5]" 0.0049727769701936684;
	setAttr -s 5 ".wl[454].w";
	setAttr ".wl[454].w[0]" 0.082481911428933144;
	setAttr ".wl[454].w[1]" 0.68814624939914903;
	setAttr ".wl[454].w[2]" 0.20112527755048332;
	setAttr ".wl[454].w[3]" 0.0232737722936305;
	setAttr ".wl[454].w[5]" 0.0049727780937255392;
	setAttr -s 5 ".wl[455].w";
	setAttr ".wl[455].w[0]" 0.082481914779333435;
	setAttr ".wl[455].w[1]" 0.68814626212660823;
	setAttr ".wl[455].w[2]" 0.20112528439695931;
	setAttr ".wl[455].w[3]" 0.02327377336683711;
	setAttr ".wl[455].w[5]" 0.0049727783396741106;
	setAttr -s 5 ".wl[456].w";
	setAttr ".wl[456].w[0]" 0.08248192003692971;
	setAttr ".wl[456].w[1]" 0.68814622419104965;
	setAttr ".wl[456].w[2]" 0.2011252901079672;
	setAttr ".wl[456].w[3]" 0.023273775537163394;
	setAttr ".wl[456].w[5]" 0.0049727788928114608;
	setAttr -s 5 ".wl[457].w";
	setAttr ".wl[457].w[0]" 0.082481932343746983;
	setAttr ".wl[457].w[1]" 0.68814620181520048;
	setAttr ".wl[457].w[2]" 0.20112530924889169;
	setAttr ".wl[457].w[3]" 0.023273780059704222;
	setAttr ".wl[457].w[5]" 0.0049727799958124786;
	setAttr -s 5 ".wl[458].w";
	setAttr ".wl[458].w[0]" 0.082481938116966899;
	setAttr ".wl[458].w[1]" 0.6881461674970718;
	setAttr ".wl[458].w[2]" 0.20112531615771997;
	setAttr ".wl[458].w[3]" 0.023273782381269918;
	setAttr ".wl[458].w[5]" 0.0049727805820125271;
	setAttr -s 5 ".wl[459].w";
	setAttr ".wl[459].w[0]" 0.082481939529451292;
	setAttr ".wl[459].w[1]" 0.6881461772276769;
	setAttr ".wl[459].w[2]" 0.2011253194234546;
	setAttr ".wl[459].w[3]" 0.023273782797071606;
	setAttr ".wl[459].w[5]" 0.0049727806730995401;
	setAttr -s 5 ".wl[460].w";
	setAttr ".wl[460].w[0]" 0.12280971943179037;
	setAttr ".wl[460].w[1]" 0.73366861937938155;
	setAttr ".wl[460].w[2]" 0.12365538452880269;
	setAttr ".wl[460].w[3]" 0.016094783517166724;
	setAttr ".wl[460].w[5]" 0.0037714931428588518;
	setAttr -s 5 ".wl[461].w";
	setAttr ".wl[461].w[0]" 0.12280972473711745;
	setAttr ".wl[461].w[1]" 0.7336686073897678;
	setAttr ".wl[461].w[2]" 0.12365538981151342;
	setAttr ".wl[461].w[3]" 0.016094784629157453;
	setAttr ".wl[461].w[5]" 0.0037714934324438267;
	setAttr -s 5 ".wl[462].w";
	setAttr ".wl[462].w[0]" 0.1228097284022434;
	setAttr ".wl[462].w[1]" 0.73366860126791544;
	setAttr ".wl[462].w[2]" 0.12365539167955765;
	setAttr ".wl[462].w[3]" 0.016094785092040369;
	setAttr ".wl[462].w[5]" 0.0037714935582432297;
	setAttr -s 5 ".wl[463].w";
	setAttr ".wl[463].w[0]" 0.12280972968408133;
	setAttr ".wl[463].w[1]" 0.73366859563792552;
	setAttr ".wl[463].w[2]" 0.12365539520900151;
	setAttr ".wl[463].w[3]" 0.016094785746865285;
	setAttr ".wl[463].w[5]" 0.0037714937221264046;
	setAttr -s 5 ".wl[464].w";
	setAttr ".wl[464].w[0]" 0.12280973560269694;
	setAttr ".wl[464].w[1]" 0.73366858433564175;
	setAttr ".wl[464].w[2]" 0.12365539939324555;
	setAttr ".wl[464].w[3]" 0.016094786694471577;
	setAttr ".wl[464].w[5]" 0.003771493973944288;
	setAttr -s 5 ".wl[465].w";
	setAttr ".wl[465].w[0]" 0.12280974348705771;
	setAttr ".wl[465].w[1]" 0.7336685629325308;
	setAttr ".wl[465].w[2]" 0.12365541019937201;
	setAttr ".wl[465].w[3]" 0.01609478885354635;
	setAttr ".wl[465].w[5]" 0.0037714945274929107;
	setAttr -s 5 ".wl[466].w";
	setAttr ".wl[466].w[0]" 0.12280975333731194;
	setAttr ".wl[466].w[1]" 0.73366854408812032;
	setAttr ".wl[466].w[2]" 0.12365541719133807;
	setAttr ".wl[466].w[3]" 0.016094790435464912;
	setAttr ".wl[466].w[5]" 0.0037714949477647267;
	setAttr -s 5 ".wl[467].w";
	setAttr ".wl[467].w[0]" 0.12280975456632483;
	setAttr ".wl[467].w[1]" 0.7336685391693395;
	setAttr ".wl[467].w[2]" 0.12365542018030624;
	setAttr ".wl[467].w[3]" 0.016094790995600978;
	setAttr ".wl[467].w[5]" 0.0037714950884282336;
	setAttr -s 5 ".wl[468].w";
	setAttr ".wl[468].w[0]" 0.12280976619409779;
	setAttr ".wl[468].w[1]" 0.73366851549131018;
	setAttr ".wl[468].w[2]" 0.12365542961535421;
	setAttr ".wl[468].w[3]" 0.016094793065455217;
	setAttr ".wl[468].w[5]" 0.0037714956337826767;
	setAttr -s 5 ".wl[469].w";
	setAttr ".wl[469].w[0]" 0.12280977630535171;
	setAttr ".wl[469].w[1]" 0.73366849035595505;
	setAttr ".wl[469].w[2]" 0.12365544156692844;
	setAttr ".wl[469].w[3]" 0.016094795507563514;
	setAttr ".wl[469].w[5]" 0.0037714962642012781;
	setAttr -s 5 ".wl[470].w";
	setAttr ".wl[470].w[0]" 0.12280976960849109;
	setAttr ".wl[470].w[1]" 0.73366850555403229;
	setAttr ".wl[470].w[2]" 0.1236554348460977;
	setAttr ".wl[470].w[3]" 0.016094794094907085;
	setAttr ".wl[470].w[5]" 0.0037714958964717251;
	setAttr -s 5 ".wl[471].w";
	setAttr ".wl[471].w[0]" 0.12280977629906124;
	setAttr ".wl[471].w[1]" 0.73366849030393666;
	setAttr ".wl[471].w[2]" 0.12365544156058886;
	setAttr ".wl[471].w[3]" 0.016094795506879048;
	setAttr ".wl[471].w[5]" 0.0037714962640504864;
	setAttr -s 5 ".wl[472].w";
	setAttr ".wl[472].w[0]" 0.12280978063578622;
	setAttr ".wl[472].w[1]" 0.73366846505969685;
	setAttr ".wl[472].w[2]" 0.12365544590665813;
	setAttr ".wl[472].w[3]" 0.016094796570947281;
	setAttr ".wl[472].w[5]" 0.003771496547400572;
	setAttr -s 5 ".wl[473].w";
	setAttr ".wl[473].w[0]" 0.12280980045518651;
	setAttr ".wl[473].w[1]" 0.73366843908520507;
	setAttr ".wl[473].w[2]" 0.12365546580462113;
	setAttr ".wl[473].w[3]" 0.016094800567540049;
	setAttr ".wl[473].w[5]" 0.0037714975799068673;
	setAttr -s 5 ".wl[474].w";
	setAttr ".wl[474].w[0]" 0.12280981651109105;
	setAttr ".wl[474].w[1]" 0.73366838773859211;
	setAttr ".wl[474].w[2]" 0.12365548191201438;
	setAttr ".wl[474].w[3]" 0.01609480409890655;
	setAttr ".wl[474].w[5]" 0.0037714985053172671;
	setAttr -s 5 ".wl[475].w";
	setAttr ".wl[475].w[0]" 0.12280982136018151;
	setAttr ".wl[475].w[1]" 0.73366840127745958;
	setAttr ".wl[475].w[2]" 0.12365548678830619;
	setAttr ".wl[475].w[3]" 0.016094804883934027;
	setAttr ".wl[475].w[5]" 0.0037714986995308806;
	setAttr -s 5 ".wl[476].w";
	setAttr ".wl[476].w[0]" 0.12280982843929597;
	setAttr ".wl[476].w[1]" 0.73366836066832719;
	setAttr ".wl[476].w[2]" 0.12365549388291394;
	setAttr ".wl[476].w[3]" 0.016094806615080084;
	setAttr ".wl[476].w[5]" 0.0037714991603041825;
	setAttr -s 5 ".wl[477].w";
	setAttr ".wl[477].w[0]" 0.12280984562170397;
	setAttr ".wl[477].w[1]" 0.73366833658280839;
	setAttr ".wl[477].w[2]" 0.12365551113280335;
	setAttr ".wl[477].w[3]" 0.016094810095108946;
	setAttr ".wl[477].w[5]" 0.0037715000600350708;
	setAttr -s 5 ".wl[478].w";
	setAttr ".wl[478].w[0]" 0.12280985346406489;
	setAttr ".wl[478].w[1]" 0.73366829983970816;
	setAttr ".wl[478].w[2]" 0.12365551899563491;
	setAttr ".wl[478].w[3]" 0.016094811933004473;
	setAttr ".wl[478].w[5]" 0.0037715005462841803;
	setAttr -s 5 ".wl[479].w";
	setAttr ".wl[479].w[0]" 0.12280985554656144;
	setAttr ".wl[479].w[1]" 0.73366831019921519;
	setAttr ".wl[479].w[2]" 0.12365552109163659;
	setAttr ".wl[479].w[3]" 0.016094812226096301;
	setAttr ".wl[479].w[5]" 0.0037715006163481827;
	setAttr -s 5 ".wl[480].w";
	setAttr ".wl[480].w[0]" 0.20208634449340046;
	setAttr ".wl[480].w[1]" 0.69836651645589565;
	setAttr ".wl[480].w[2]" 0.084005398769936374;
	setAttr ".wl[480].w[3]" 0.012386201650256662;
	setAttr ".wl[480].w[5]" 0.0031555386305107446;
	setAttr -s 5 ".wl[481].w";
	setAttr ".wl[481].w[0]" 0.20208635033798417;
	setAttr ".wl[481].w[1]" 0.69836650560979963;
	setAttr ".wl[481].w[2]" 0.084005402705563073;
	setAttr ".wl[481].w[3]" 0.012386202483823078;
	setAttr ".wl[481].w[5]" 0.0031555388628299714;
	setAttr -s 5 ".wl[482].w";
	setAttr ".wl[482].w[0]" 0.20208635520485346;
	setAttr ".wl[482].w[1]" 0.69836649880026724;
	setAttr ".wl[482].w[2]" 0.084005404191018873;
	setAttr ".wl[482].w[3]" 0.012386202838358139;
	setAttr ".wl[482].w[5]" 0.0031555389655022917;
	setAttr -s 5 ".wl[483].w";
	setAttr ".wl[483].w[0]" 0.2020863555697423;
	setAttr ".wl[483].w[1]" 0.69836649531420947;
	setAttr ".wl[483].w[2]" 0.084005406701635407;
	setAttr ".wl[483].w[3]" 0.012386203319652589;
	setAttr ".wl[483].w[5]" 0.0031555390947603165;
	setAttr -s 5 ".wl[484].w";
	setAttr ".wl[484].w[0]" 0.20208636288609633;
	setAttr ".wl[484].w[1]" 0.69836648386945854;
	setAttr ".wl[484].w[2]" 0.084005409908758863;
	setAttr ".wl[484].w[3]" 0.01238620403722809;
	setAttr ".wl[484].w[5]" 0.0031555392984581984;
	setAttr -s 5 ".wl[485].w";
	setAttr ".wl[485].w[0]" 0.20208637019973411;
	setAttr ".wl[485].w[1]" 0.69836646661429069;
	setAttr ".wl[485].w[2]" 0.084005417803221488;
	setAttr ".wl[485].w[3]" 0.012386205643123975;
	setAttr ".wl[485].w[5]" 0.0031555397396296927;
	setAttr -s 5 ".wl[486].w";
	setAttr ".wl[486].w[0]" 0.20208638236310997;
	setAttr ".wl[486].w[1]" 0.6983664475561524;
	setAttr ".wl[486].w[2]" 0.084005423160305459;
	setAttr ".wl[486].w[3]" 0.01238620684087627;
	setAttr ".wl[486].w[5]" 0.003155540079555999;
	setAttr -s 5 ".wl[487].w";
	setAttr ".wl[487].w[0]" 0.2020863828966282;
	setAttr ".wl[487].w[1]" 0.69836644436545581;
	setAttr ".wl[487].w[2]" 0.084005425293987648;
	setAttr ".wl[487].w[3]" 0.012386207253262421;
	setAttr ".wl[487].w[5]" 0.003155540190666;
	setAttr -s 5 ".wl[488].w";
	setAttr ".wl[488].w[0]" 0.20208639670773948;
	setAttr ".wl[488].w[1]" 0.69836642141283445;
	setAttr ".wl[488].w[2]" 0.084005432435274682;
	setAttr ".wl[488].w[3]" 0.01238620881388048;
	setAttr ".wl[488].w[5]" 0.0031555406302709002;
	setAttr -s 5 ".wl[489].w";
	setAttr ".wl[489].w[0]" 0.20208640697461738;
	setAttr ".wl[489].w[1]" 0.69836640001540518;
	setAttr ".wl[489].w[2]" 0.084005441239346251;
	setAttr ".wl[489].w[3]" 0.012386210636469656;
	setAttr ".wl[489].w[5]" 0.0031555411341614571;
	setAttr -s 5 ".wl[490].w";
	setAttr ".wl[490].w[0]" 0.20208639961669095;
	setAttr ".wl[490].w[1]" 0.69836641373040675;
	setAttr ".wl[490].w[2]" 0.084005436235868397;
	setAttr ".wl[490].w[3]" 0.012386209577818783;
	setAttr ".wl[490].w[5]" 0.0031555408392151684;
	setAttr -s 5 ".wl[491].w";
	setAttr ".wl[491].w[0]" 0.20208640696166774;
	setAttr ".wl[491].w[1]" 0.69836639997371242;
	setAttr ".wl[491].w[2]" 0.084005441236273681;
	setAttr ".wl[491].w[3]" 0.012386210636075281;
	setAttr ".wl[491].w[5]" 0.0031555411340631664;
	setAttr -s 5 ".wl[492].w";
	setAttr ".wl[492].w[0]" 0.20208641070045164;
	setAttr ".wl[492].w[1]" 0.6983663766380197;
	setAttr ".wl[492].w[2]" 0.084005444594179496;
	setAttr ".wl[492].w[3]" 0.012386211428508549;
	setAttr ".wl[492].w[5]" 0.0031555413593297881;
	setAttr -s 5 ".wl[493].w";
	setAttr ".wl[493].w[0]" 0.20208643372287047;
	setAttr ".wl[493].w[1]" 0.6983663538657936;
	setAttr ".wl[493].w[2]" 0.084005459255398388;
	setAttr ".wl[493].w[3]" 0.012386214429437301;
	setAttr ".wl[493].w[5]" 0.003155542189856047;
	setAttr -s 5 ".wl[494].w";
	setAttr ".wl[494].w[0]" 0.20208645036645589;
	setAttr ".wl[494].w[1]" 0.6983663070020828;
	setAttr ".wl[494].w[2]" 0.084005471366866008;
	setAttr ".wl[494].w[3]" 0.012386217071209581;
	setAttr ".wl[494].w[5]" 0.0031555429302034515;
	setAttr -s 5 ".wl[495].w";
	setAttr ".wl[495].w[0]" 0.20208645732726632;
	setAttr ".wl[495].w[1]" 0.69836632012065591;
	setAttr ".wl[495].w[2]" 0.084005474804495606;
	setAttr ".wl[495].w[3]" 0.012386217667758877;
	setAttr ".wl[495].w[5]" 0.003155543089235587;
	setAttr -s 5 ".wl[496].w";
	setAttr ".wl[496].w[0]" 0.20208646347246581;
	setAttr ".wl[496].w[1]" 0.69836628259827671;
	setAttr ".wl[496].w[2]" 0.084005480282230954;
	setAttr ".wl[496].w[3]" 0.01238621895729004;
	setAttr ".wl[496].w[5]" 0.0031555434556579092;
	setAttr -s 5 ".wl[497].w";
	setAttr ".wl[497].w[0]" 0.20208648333279411;
	setAttr ".wl[497].w[1]" 0.69836626140339031;
	setAttr ".wl[497].w[2]" 0.084005493006890891;
	setAttr ".wl[497].w[3]" 0.012386221570134689;
	setAttr ".wl[497].w[5]" 0.0031555441792496682;
	setAttr -s 5 ".wl[498].w";
	setAttr ".wl[498].w[0]" 0.2020864906790617;
	setAttr ".wl[498].w[1]" 0.69836622754001099;
	setAttr ".wl[498].w[2]" 0.084005499008358742;
	setAttr ".wl[498].w[3]" 0.012386222940919818;
	setAttr ".wl[498].w[5]" 0.0031555445666895734;
	setAttr -s 5 ".wl[499].w";
	setAttr ".wl[499].w[0]" 0.20208649397355988;
	setAttr ".wl[499].w[1]" 0.69836623744981308;
	setAttr ".wl[499].w[2]" 0.084005500451244955;
	setAttr ".wl[499].w[3]" 0.012386223165764891;
	setAttr ".wl[499].w[5]" 0.0031555446249231659;
	setAttr -s 5 ".wl[500].w";
	setAttr ".wl[500].w[0]" 0.34457847841966965;
	setAttr ".wl[500].w[1]" 0.58181975043288925;
	setAttr ".wl[500].w[2]" 0.06071431528520245;
	setAttr ".wl[500].w[3]" 0.010109469404703093;
	setAttr ".wl[500].w[5]" 0.0027779864575356952;
	setAttr -s 5 ".wl[501].w";
	setAttr ".wl[501].w[0]" 0.34457848131160096;
	setAttr ".wl[501].w[1]" 0.58181974397841496;
	setAttr ".wl[501].w[2]" 0.060714318041987611;
	setAttr ".wl[501].w[3]" 0.010109470025330403;
	setAttr ".wl[501].w[5]" 0.002777986642666075;
	setAttr -s 5 ".wl[502].w";
	setAttr ".wl[502].w[0]" 0.34457848554670417;
	setAttr ".wl[502].w[1]" 0.58181973839213819;
	setAttr ".wl[502].w[2]" 0.06071431905620836;
	setAttr ".wl[502].w[3]" 0.01010947028247916;
	setAttr ".wl[502].w[5]" 0.0027779867224701558;
	setAttr -s 5 ".wl[503].w";
	setAttr ".wl[503].w[0]" 0.34457848342553893;
	setAttr ".wl[503].w[1]" 0.58181973824976374;
	setAttr ".wl[503].w[2]" 0.060714320847338681;
	setAttr ".wl[503].w[3]" 0.010109470649357686;
	setAttr ".wl[503].w[5]" 0.0027779868280009006;
	setAttr -s 5 ".wl[504].w";
	setAttr ".wl[504].w[0]" 0.34457848880118486;
	setAttr ".wl[504].w[1]" 0.58181972996498188;
	setAttr ".wl[504].w[2]" 0.060714323068390127;
	setAttr ".wl[504].w[3]" 0.010109471177056756;
	setAttr ".wl[504].w[5]" 0.0027779869883864028;
	setAttr -s 5 ".wl[505].w";
	setAttr ".wl[505].w[0]" 0.34457848942046765;
	setAttr ".wl[505].w[1]" 0.58181972221347689;
	setAttr ".wl[505].w[2]" 0.060714328639134681;
	setAttr ".wl[505].w[3]" 0.010109472383701287;
	setAttr ".wl[505].w[5]" 0.0027779873432195266;
	setAttr -s 5 ".wl[506].w";
	setAttr ".wl[506].w[0]" 0.34457849833177895;
	setAttr ".wl[506].w[1]" 0.58181970844298214;
	setAttr ".wl[506].w[2]" 0.06071433234967423;
	setAttr ".wl[506].w[3]" 0.010109473264657151;
	setAttr ".wl[506].w[5]" 0.0027779876109074574;
	setAttr -s 5 ".wl[507].w";
	setAttr ".wl[507].w[0]" 0.34457849679502472;
	setAttr ".wl[507].w[1]" 0.58181970805570327;
	setAttr ".wl[507].w[2]" 0.060714333869494534;
	setAttr ".wl[507].w[3]" 0.01010947357835427;
	setAttr ".wl[507].w[5]" 0.0027779877014233291;
	setAttr -s 5 ".wl[508].w";
	setAttr ".wl[508].w[0]" 0.34457850584448624;
	setAttr ".wl[508].w[1]" 0.58181969253560462;
	setAttr ".wl[508].w[2]" 0.060714338838705348;
	setAttr ".wl[508].w[3]" 0.010109474731927125;
	setAttr ".wl[508].w[5]" 0.0027779880492768551;
	setAttr -s 5 ".wl[509].w";
	setAttr ".wl[509].w[0]" 0.34457850901468551;
	setAttr ".wl[509].w[1]" 0.58181968140472906;
	setAttr ".wl[509].w[2]" 0.060714345031762817;
	setAttr ".wl[509].w[3]" 0.010109476095921686;
	setAttr ".wl[509].w[5]" 0.0027779884529009749;
	setAttr -s 5 ".wl[510].w";
	setAttr ".wl[510].w[0]" 0.34457850541231588;
	setAttr ".wl[510].w[1]" 0.58181968953486374;
	setAttr ".wl[510].w[2]" 0.060714341527334605;
	setAttr ".wl[510].w[3]" 0.010109475307650589;
	setAttr ".wl[510].w[5]" 0.00277798821783532;
	setAttr -s 5 ".wl[511].w";
	setAttr ".wl[511].w[0]" 0.34457850899500259;
	setAttr ".wl[511].w[1]" 0.58181968138218509;
	setAttr ".wl[511].w[2]" 0.060714345030553833;
	setAttr ".wl[511].w[3]" 0.01010947609574897;
	setAttr ".wl[511].w[5]" 0.0027779884528538177;
	setAttr -s 5 ".wl[512].w";
	setAttr ".wl[512].w[0]" 0.34457850708778404;
	setAttr ".wl[512].w[1]" 0.58181966500601823;
	setAttr ".wl[512].w[2]" 0.060714347354894477;
	setAttr ".wl[512].w[3]" 0.010109476672468356;
	setAttr ".wl[512].w[5]" 0.0027779886284277663;
	setAttr -s 5 ".wl[513].w";
	setAttr ".wl[513].w[0]" 0.34457852295270197;
	setAttr ".wl[513].w[1]" 0.58181965466161389;
	setAttr ".wl[513].w[2]" 0.060714357659212972;
	setAttr ".wl[513].w[3]" 0.010109478923644935;
	setAttr ".wl[513].w[5]" 0.0027779892952857544;
	setAttr -s 5 ".wl[514].w";
	setAttr ".wl[514].w[0]" 0.34457852747300133;
	setAttr ".wl[514].w[1]" 0.58181962441885982;
	setAttr ".wl[514].w[2]" 0.060714366114874713;
	setAttr ".wl[514].w[3]" 0.010109480877717524;
	setAttr ".wl[514].w[5]" 0.0027779898814679865;
	setAttr -s 5 ".wl[515].w";
	setAttr ".wl[515].w[0]" 0.34457853683207851;
	setAttr ".wl[515].w[1]" 0.58181963625324384;
	setAttr ".wl[515].w[2]" 0.06071436856642666;
	setAttr ".wl[515].w[3]" 0.010109481343143512;
	setAttr ".wl[515].w[5]" 0.0027779900145198481;
	setAttr -s 5 ".wl[516].w";
	setAttr ".wl[516].w[0]" 0.34457853387946702;
	setAttr ".wl[516].w[1]" 0.58181960994663207;
	setAttr ".wl[516].w[2]" 0.060714372357771718;
	setAttr ".wl[516].w[3]" 0.010109482281869366;
	setAttr ".wl[516].w[5]" 0.0027779903001811665;
	setAttr -s 5 ".wl[517].w";
	setAttr ".wl[517].w[0]" 0.3445785472009546;
	setAttr ".wl[517].w[1]" 0.58181959984514242;
	setAttr ".wl[517].w[2]" 0.060714381296368448;
	setAttr ".wl[517].w[3]" 0.010109484240215063;
	setAttr ".wl[517].w[5]" 0.002777990880675292;
	setAttr -s 5 ".wl[518].w";
	setAttr ".wl[518].w[0]" 0.34457854618892969;
	setAttr ".wl[518].w[1]" 0.58181957663681505;
	setAttr ".wl[518].w[2]" 0.060714385465718612;
	setAttr ".wl[518].w[3]" 0.010109485244454599;
	setAttr ".wl[518].w[5]" 0.0027779911845710044;
	setAttr -s 5 ".wl[519].w";
	setAttr ".wl[519].w[0]" 0.34457855147419991;
	setAttr ".wl[519].w[1]" 0.58181958502566555;
	setAttr ".wl[519].w[2]" 0.060714386505228868;
	setAttr ".wl[519].w[3]" 0.01010948542526102;
	setAttr ".wl[519].w[5]" 0.0027779912349505777;
	setAttr -s 5 ".wl[520].w";
	setAttr ".wl[520].w[0]" 0.53633244958216797;
	setAttr ".wl[520].w[1]" 0.41067824808608705;
	setAttr ".wl[520].w[2]" 0.0426810937803528;
	setAttr ".wl[520].w[3]" 0.0079643173530056146;
	setAttr ".wl[520].w[5]" 0.0023438911983866047;
	setAttr -s 5 ".wl[521].w";
	setAttr ".wl[521].w[0]" 0.53633244578694639;
	setAttr ".wl[521].w[1]" 0.41067824913132756;
	setAttr ".wl[521].w[2]" 0.042681095882118297;
	setAttr ".wl[521].w[3]" 0.0079643178458537536;
	setAttr ".wl[521].w[5]" 0.0023438913537540715;
	setAttr -s 5 ".wl[522].w";
	setAttr ".wl[522].w[0]" 0.53633244659853796;
	setAttr ".wl[522].w[1]" 0.4106782472864835;
	setAttr ".wl[522].w[2]" 0.042681096650966886;
	setAttr ".wl[522].w[3]" 0.0079643180451157078;
	setAttr ".wl[522].w[5]" 0.0023438914188959026;
	setAttr -s 5 ".wl[523].w";
	setAttr ".wl[523].w[0]" 0.53633244135112479;
	setAttr ".wl[523].w[1]" 0.41067825077467868;
	setAttr ".wl[523].w[2]" 0.042681098021780439;
	setAttr ".wl[523].w[3]" 0.007964318342653846;
	setAttr ".wl[523].w[5]" 0.0023438915097624938;
	setAttr -s 5 ".wl[524].w";
	setAttr ".wl[524].w[0]" 0.53633244041678851;
	setAttr ".wl[524].w[1]" 0.41067824947303622;
	setAttr ".wl[524].w[2]" 0.042681099710654778;
	setAttr ".wl[524].w[3]" 0.0079643187569252098;
	setAttr ".wl[524].w[5]" 0.0023438916425953297;
	setAttr -s 5 ".wl[525].w";
	setAttr ".wl[525].w[0]" 0.5363324290945416;
	setAttr ".wl[525].w[1]" 0.41067825527225943;
	setAttr ".wl[525].w[2]" 0.042681103966286903;
	setAttr ".wl[525].w[3]" 0.0079643197234661456;
	setAttr ".wl[525].w[5]" 0.0023438919434459983;
	setAttr -s 5 ".wl[526].w";
	setAttr ".wl[526].w[0]" 0.53633242748022947;
	setAttr ".wl[526].w[1]" 0.41067825315107337;
	setAttr ".wl[526].w[2]" 0.042681106788272465;
	setAttr ".wl[526].w[3]" 0.0079643204152253684;
	setAttr ".wl[526].w[5]" 0.0023438921651994533;
	setAttr -s 5 ".wl[527].w";
	setAttr ".wl[527].w[0]" 0.53633242320772567;
	setAttr ".wl[527].w[1]" 0.41067825592874657;
	setAttr ".wl[527].w[2]" 0.042681107951334576;
	setAttr ".wl[527].w[3]" 0.0079643206692199264;
	setAttr ".wl[527].w[5]" 0.0023438922429732407;
	setAttr -s 5 ".wl[528].w";
	setAttr ".wl[528].w[0]" 0.53633241903762474;
	setAttr ".wl[528].w[1]" 0.41067825511582245;
	setAttr ".wl[528].w[2]" 0.042681111734556403;
	setAttr ".wl[528].w[3]" 0.0079643215793094805;
	setAttr ".wl[528].w[5]" 0.002343892532687119;
	setAttr -s 5 ".wl[529].w";
	setAttr ".wl[529].w[0]" 0.53633240818739747;
	setAttr ".wl[529].w[1]" 0.41067825981005729;
	setAttr ".wl[529].w[2]" 0.042681116461418193;
	setAttr ".wl[529].w[3]" 0.0079643226677596646;
	setAttr ".wl[529].w[5]" 0.0023438928733675252;
	setAttr -s 5 ".wl[530].w";
	setAttr ".wl[530].w[0]" 0.53633241306805068;
	setAttr ".wl[530].w[1]" 0.41067825842514016;
	setAttr ".wl[530].w[2]" 0.042681113789160591;
	setAttr ".wl[530].w[3]" 0.007964322041612043;
	setAttr ".wl[530].w[5]" 0.0023438926760366088;
	setAttr -s 5 ".wl[531].w";
	setAttr ".wl[531].w[0]" 0.53633240816020611;
	setAttr ".wl[531].w[1]" 0.41067825979475031;
	setAttr ".wl[531].w[2]" 0.042681116460458565;
	setAttr ".wl[531].w[3]" 0.0079643226676053731;
	setAttr ".wl[531].w[5]" 0.0023438928733238995;
	setAttr -s 5 ".wl[532].w";
	setAttr ".wl[532].w[0]" 0.53633239547971512;
	setAttr ".wl[532].w[1]" 0.41067825483499332;
	setAttr ".wl[532].w[2]" 0.042681118287659359;
	setAttr ".wl[532].w[3]" 0.0079643231266953024;
	setAttr ".wl[532].w[5]" 0.0023438930205297507;
	setAttr -s 5 ".wl[533].w";
	setAttr ".wl[533].w[0]" 0.53633239276141542;
	setAttr ".wl[533].w[1]" 0.41067826616010306;
	setAttr ".wl[533].w[2]" 0.042681126076805277;
	setAttr ".wl[533].w[3]" 0.0079643249135849525;
	setAttr ".wl[533].w[5]" 0.002343893580550939;
	setAttr -s 5 ".wl[534].w";
	setAttr ".wl[534].w[0]" 0.53633237183685234;
	setAttr ".wl[534].w[1]" 0.41067826381264549;
	setAttr ".wl[534].w[2]" 0.042681132577291475;
	setAttr ".wl[534].w[3]" 0.0079643264666818658;
	setAttr ".wl[534].w[5]" 0.0023438940724503101;
	setAttr -s 5 ".wl[535].w";
	setAttr ".wl[535].w[0]" 0.53633238347459522;
	setAttr ".wl[535].w[1]" 0.41067827415663116;
	setAttr ".wl[535].w[2]" 0.042681134358976275;
	setAttr ".wl[535].w[3]" 0.0079643268347796298;
	setAttr ".wl[535].w[5]" 0.0023438941844298742;
	setAttr -s 5 ".wl[536].w";
	setAttr ".wl[536].w[0]" 0.53633236313915622;
	setAttr ".wl[536].w[1]" 0.41067826628343046;
	setAttr ".wl[536].w[2]" 0.042681137337386182;
	setAttr ".wl[536].w[3]" 0.0079643275820066965;
	setAttr ".wl[536].w[5]" 0.0023438944239418261;
	setAttr -s 5 ".wl[537].w";
	setAttr ".wl[537].w[0]" 0.5363323598273213;
	setAttr ".wl[537].w[1]" 0.4106782755158061;
	setAttr ".wl[537].w[2]" 0.042681144101051068;
	setAttr ".wl[537].w[3]" 0.0079643291367968959;
	setAttr ".wl[537].w[5]" 0.0023438949114844244;
	setAttr -s 5 ".wl[538].w";
	setAttr ".wl[538].w[0]" 0.53633234238069183;
	setAttr ".wl[538].w[1]" 0.41067826991901951;
	setAttr ".wl[538].w[2]" 0.042681147347812323;
	setAttr ".wl[538].w[3]" 0.007964329935700518;
	setAttr ".wl[538].w[5]" 0.0023438951663687741;
	setAttr -s 5 ".wl[539].w";
	setAttr ".wl[539].w[0]" 0.53633235019636516;
	setAttr ".wl[539].w[1]" 0.4106782760968784;
	setAttr ".wl[539].w[2]" 0.042681148085190142;
	setAttr ".wl[539].w[3]" 0.0079643300781025335;
	setAttr ".wl[539].w[5]" 0.0023438952087697497;
	setAttr -s 5 ".wl[540].w";
	setAttr ".wl[540].w[0]" 0.70813516842718838;
	setAttr ".wl[540].w[1]" 0.25546271275897692;
	setAttr ".wl[540].w[2]" 0.028616259089648235;
	setAttr ".wl[540].w[3]" 0.0059288601839718926;
	setAttr ".wl[540].w[5]" 0.0018569995402145257;
	setAttr -s 5 ".wl[541].w";
	setAttr ".wl[541].w[0]" 0.70813515984815367;
	setAttr ".wl[541].w[1]" 0.25546271901875611;
	setAttr ".wl[541].w[2]" 0.028616260845474691;
	setAttr ".wl[541].w[3]" 0.0059288606077442215;
	setAttr ".wl[541].w[5]" 0.0018569996798711342;
	setAttr -s 5 ".wl[542].w";
	setAttr ".wl[542].w[0]" 0.70813515744365252;
	setAttr ".wl[542].w[1]" 0.25546272049716812;
	setAttr ".wl[542].w[2]" 0.028616261534672494;
	setAttr ".wl[542].w[3]" 0.0059288607847237237;
	setAttr ".wl[542].w[5]" 0.0018569997397831482;
	setAttr -s 5 ".wl[543].w";
	setAttr ".wl[543].w[0]" 0.70813515091523782;
	setAttr ".wl[543].w[1]" 0.25546272560998934;
	setAttr ".wl[543].w[2]" 0.028616262621440409;
	setAttr ".wl[543].w[3]" 0.0059288610335542502;
	setAttr ".wl[543].w[5]" 0.0018569998197781226;
	setAttr -s 5 ".wl[544].w";
	setAttr ".wl[544].w[0]" 0.70813514472335193;
	setAttr ".wl[544].w[1]" 0.25546272986317559;
	setAttr ".wl[544].w[2]" 0.028616264077736198;
	setAttr ".wl[544].w[3]" 0.0059288613952400157;
	setAttr ".wl[544].w[5]" 0.0018569999404963386;
	setAttr -s 5 ".wl[545].w";
	setAttr ".wl[545].w[0]" 0.70813512612843388;
	setAttr ".wl[545].w[1]" 0.25546274388948886;
	setAttr ".wl[545].w[2]" 0.028616267556243049;
	setAttr ".wl[545].w[3]" 0.0059288622171186651;
	setAttr ".wl[545].w[5]" 0.0018570002087155712;
	setAttr -s 5 ".wl[546].w";
	setAttr ".wl[546].w[0]" 0.70813511576761889;
	setAttr ".wl[546].w[1]" 0.25546275101305393;
	setAttr ".wl[546].w[2]" 0.028616269988224176;
	setAttr ".wl[546].w[3]" 0.0059288628208991776;
	setAttr ".wl[546].w[5]" 0.0018570004102038051;
	setAttr -s 5 ".wl[547].w";
	setAttr ".wl[547].w[0]" 0.70813511028940002;
	setAttr ".wl[547].w[1]" 0.25546275528395879;
	setAttr ".wl[547].w[2]" 0.028616270914047823;
	setAttr ".wl[547].w[3]" 0.0059288630338005426;
	setAttr ".wl[547].w[5]" 0.0018570004787930134;
	setAttr -s 5 ".wl[548].w";
	setAttr ".wl[548].w[0]" 0.70813509572437661;
	setAttr ".wl[548].w[1]" 0.25546276557929432;
	setAttr ".wl[548].w[2]" 0.028616274132144171;
	setAttr ".wl[548].w[3]" 0.0059288638232981652;
	setAttr ".wl[548].w[5]" 0.0018570007408866265;
	setAttr -s 5 ".wl[549].w";
	setAttr ".wl[549].w[0]" 0.70813507564785749;
	setAttr ".wl[549].w[1]" 0.25546278052056087;
	setAttr ".wl[549].w[2]" 0.028616278032472561;
	setAttr ".wl[549].w[3]" 0.005928864753386871;
	setAttr ".wl[549].w[5]" 0.0018570010457222995;
	setAttr -s 5 ".wl[550].w";
	setAttr ".wl[550].w[0]" 0.70813508658043622;
	setAttr ".wl[550].w[1]" 0.25546277253544181;
	setAttr ".wl[550].w[2]" 0.028616275800707344;
	setAttr ".wl[550].w[3]" 0.0059288642150560822;
	setAttr ".wl[550].w[5]" 0.0018570008683585942;
	setAttr -s 5 ".wl[551].w";
	setAttr ".wl[551].w[0]" 0.70813507560223188;
	setAttr ".wl[551].w[1]" 0.25546278050917598;
	setAttr ".wl[551].w[2]" 0.028616278031516253;
	setAttr ".wl[551].w[3]" 0.0059288647532025826;
	setAttr ".wl[551].w[5]" 0.0018570010456656551;
	setAttr -s 5 ".wl[552].w";
	setAttr ".wl[552].w[0]" 0.70813505469218507;
	setAttr ".wl[552].w[1]" 0.25546278402081962;
	setAttr ".wl[552].w[2]" 0.028616279663957824;
	setAttr ".wl[552].w[3]" 0.0059288651617809846;
	setAttr ".wl[552].w[5]" 0.0018570011817454881;
	setAttr -s 5 ".wl[553].w";
	setAttr ".wl[553].w[0]" 0.70813503938971656;
	setAttr ".wl[553].w[1]" 0.25546280970315566;
	setAttr ".wl[553].w[2]" 0.028616286038113236;
	setAttr ".wl[553].w[3]" 0.0059288666810040332;
	setAttr ".wl[553].w[5]" 0.001857001680470247;
	setAttr -s 5 ".wl[554].w";
	setAttr ".wl[554].w[0]" 0.70813499979359285;
	setAttr ".wl[554].w[1]" 0.25546282724580471;
	setAttr ".wl[554].w[2]" 0.028616291570462485;
	setAttr ".wl[554].w[3]" 0.0059288680297913243;
	setAttr ".wl[554].w[5]" 0.0018570021262701158;
	setAttr -s 5 ".wl[555].w";
	setAttr ".wl[555].w[0]" 0.7081350139052035;
	setAttr ".wl[555].w[1]" 0.25546283567132105;
	setAttr ".wl[555].w[2]" 0.028616292888028118;
	setAttr ".wl[555].w[3]" 0.0059288683239952459;
	setAttr ".wl[555].w[5]" 0.0018570022208643782;
	setAttr -s 5 ".wl[556].w";
	setAttr ".wl[556].w[0]" 0.70813498031812605;
	setAttr ".wl[556].w[1]" 0.25546284147109227;
	setAttr ".wl[556].w[2]" 0.028616295545827272;
	setAttr ".wl[556].w[3]" 0.0059288689886828217;
	setAttr ".wl[556].w[5]" 0.001857002442193128;
	setAttr -s 5 ".wl[557].w";
	setAttr ".wl[557].w[0]" 0.70813496566586775;
	setAttr ".wl[557].w[1]" 0.25546286357508274;
	setAttr ".wl[557].w[2]" 0.028616301091787668;
	setAttr ".wl[557].w[3]" 0.0059288703120488366;
	setAttr ".wl[557].w[5]" 0.0018570028767765294;
	setAttr -s 5 ".wl[558].w";
	setAttr ".wl[558].w[0]" 0.70813493584689979;
	setAttr ".wl[558].w[1]" 0.25546287088412023;
	setAttr ".wl[558].w[2]" 0.028616303935453714;
	setAttr ".wl[558].w[3]" 0.0059288710161994346;
	setAttr ".wl[558].w[5]" 0.0018570031105755837;
	setAttr -s 5 ".wl[559].w";
	setAttr ".wl[559].w[0]" 0.70813494596608129;
	setAttr ".wl[559].w[1]" 0.25546287498448883;
	setAttr ".wl[559].w[2]" 0.028616304445184555;
	setAttr ".wl[559].w[3]" 0.005928871124671037;
	setAttr ".wl[559].w[5]" 0.0018570031448802602;
	setAttr -s 5 ".wl[560].w";
	setAttr ".wl[560].w[0]" 0.81443464405131427;
	setAttr ".wl[560].w[1]" 0.15951916009310102;
	setAttr ".wl[560].w[2]" 0.019983018462874199;
	setAttr ".wl[560].w[3]" 0.0045536801710448329;
	setAttr ".wl[560].w[5]" 0.0015094972216656078;
	setAttr -s 5 ".wl[561].w";
	setAttr ".wl[561].w[0]" 0.81443463500777213;
	setAttr ".wl[561].w[1]" 0.15951916718057071;
	setAttr ".wl[561].w[2]" 0.019983019921783508;
	setAttr ".wl[561].w[3]" 0.0045536805408254713;
	setAttr ".wl[561].w[5]" 0.0015094973490482055;
	setAttr -s 5 ".wl[562].w";
	setAttr ".wl[562].w[0]" 0.81443463155826579;
	setAttr ".wl[562].w[1]" 0.15951916978757857;
	setAttr ".wl[562].w[2]" 0.019983020542793203;
	setAttr ".wl[562].w[3]" 0.0045536807046970933;
	setAttr ".wl[562].w[5]" 0.001509497406665388;
	setAttr -s 5 ".wl[563].w";
	setAttr ".wl[563].w[0]" 0.81443462583418258;
	setAttr ".wl[563].w[1]" 0.15951917439549618;
	setAttr ".wl[563].w[2]" 0.019983021384574595;
	setAttr ".wl[563].w[3]" 0.0045536809098763202;
	setAttr ".wl[563].w[5]" 0.0015094974758703668;
	setAttr -s 5 ".wl[564].w";
	setAttr ".wl[564].w[0]" 0.81443461842974696;
	setAttr ".wl[564].w[1]" 0.15951918010591576;
	setAttr ".wl[564].w[2]" 0.019983022640975383;
	setAttr ".wl[564].w[3]" 0.0045536812345339222;
	setAttr ".wl[564].w[5]" 0.0015094975888279871;
	setAttr -s 5 ".wl[565].w";
	setAttr ".wl[565].w[0]" 0.81443460035207915;
	setAttr ".wl[565].w[1]" 0.15951919443286069;
	setAttr ".wl[565].w[2]" 0.019983025450563296;
	setAttr ".wl[565].w[3]" 0.0045536819359669562;
	setAttr ".wl[565].w[5]" 0.001509497828529898;
	setAttr -s 5 ".wl[566].w";
	setAttr ".wl[566].w[0]" 0.81443458798472246;
	setAttr ".wl[566].w[1]" 0.15951920397284114;
	setAttr ".wl[566].w[2]" 0.019983027547693141;
	setAttr ".wl[566].w[3]" 0.0045536824777389004;
	setAttr ".wl[566].w[5]" 0.0015094980170043408;
	setAttr -s 5 ".wl[567].w";
	setAttr ".wl[567].w[0]" 0.81443458311822081;
	setAttr ".wl[567].w[1]" 0.15951920788211596;
	setAttr ".wl[567].w[2]" 0.019983028268905932;
	setAttr ".wl[567].w[3]" 0.0045536826541401343;
	setAttr ".wl[567].w[5]" 0.0015094980766171492;
	setAttr -s 5 ".wl[568].w";
	setAttr ".wl[568].w[0]" 0.81443456666715186;
	setAttr ".wl[568].w[1]" 0.15951922065849455;
	setAttr ".wl[568].w[2]" 0.019983031000738425;
	setAttr ".wl[568].w[3]" 0.0045536833543722557;
	setAttr ".wl[568].w[5]" 0.0015094983192428745;
	setAttr -s 5 ".wl[569].w";
	setAttr ".wl[569].w[0]" 0.81443454647325686;
	setAttr ".wl[569].w[1]" 0.15951923658643125;
	setAttr ".wl[569].w[2]" 0.019983034190218792;
	setAttr ".wl[569].w[3]" 0.0045536841559532439;
	setAttr ".wl[569].w[5]" 0.0015094985941398115;
	setAttr -s 5 ".wl[570].w";
	setAttr ".wl[570].w[0]" 0.81443455796958086;
	setAttr ".wl[570].w[1]" 0.15951922757408196;
	setAttr ".wl[570].w[2]" 0.01998303233738094;
	setAttr ".wl[570].w[3]" 0.0045536836865019631;
	setAttr ".wl[570].w[5]" 0.0015094984324542573;
	setAttr -s 5 ".wl[571].w";
	setAttr ".wl[571].w[0]" 0.81443454642802593;
	setAttr ".wl[571].w[1]" 0.15951923658133985;
	setAttr ".wl[571].w[2]" 0.019983034189743107;
	setAttr ".wl[571].w[3]" 0.0045536841558524088;
	setAttr ".wl[571].w[5]" 0.0015094985941069515;
	setAttr -s 5 ".wl[572].w";
	setAttr ".wl[572].w[0]" 0.81443452337242772;
	setAttr ".wl[572].w[1]" 0.15951924250334931;
	setAttr ".wl[572].w[2]" 0.019983035602279958;
	setAttr ".wl[572].w[3]" 0.0045536845214967005;
	setAttr ".wl[572].w[5]" 0.0015094987209351479;
	setAttr -s 5 ".wl[573].w";
	setAttr ".wl[573].w[0]" 0.8144345085931699;
	setAttr ".wl[573].w[1]" 0.15951926906922648;
	setAttr ".wl[573].w[2]" 0.019983040823201143;
	setAttr ".wl[573].w[3]" 0.0045536858347365559;
	setAttr ".wl[573].w[5]" 0.0015094991721254912;
	setAttr -s 5 ".wl[574].w";
	setAttr ".wl[574].w[0]" 0.81443446592992264;
	setAttr ".wl[574].w[1]" 0.15951929076310173;
	setAttr ".wl[574].w[2]" 0.01998304547168395;
	setAttr ".wl[574].w[3]" 0.0045536870200020346;
	setAttr ".wl[574].w[5]" 0.0015094995812111344;
	setAttr -s 5 ".wl[575].w";
	setAttr ".wl[575].w[0]" 0.81443448246126227;
	setAttr ".wl[575].w[1]" 0.15951929714951882;
	setAttr ".wl[575].w[2]" 0.019983046474021455;
	setAttr ".wl[575].w[3]" 0.0045536872616118761;
	setAttr ".wl[575].w[5]" 0.0015094996629977956;
	setAttr -s 5 ".wl[576].w";
	setAttr ".wl[576].w[0]" 0.8144344454517608;
	setAttr ".wl[576].w[1]" 0.15951930681677537;
	setAttr ".wl[576].w[2]" 0.019983048771995519;
	setAttr ".wl[576].w[3]" 0.0045536878561869432;
	setAttr ".wl[576].w[5]" 0.0015094998692028602;
	setAttr -s 5 ".wl[577].w";
	setAttr ".wl[577].w[0]" 0.8144344310756797;
	setAttr ".wl[577].w[1]" 0.15951932986160131;
	setAttr ".wl[577].w[2]" 0.019983053320514421;
	setAttr ".wl[577].w[3]" 0.0045536890011090595;
	setAttr ".wl[577].w[5]" 0.0015095002626589837;
	setAttr -s 5 ".wl[578].w";
	setAttr ".wl[578].w[0]" 0.81443439841347309;
	setAttr ".wl[578].w[1]" 0.15951934052187791;
	setAttr ".wl[578].w[2]" 0.019983055751979659;
	setAttr ".wl[578].w[3]" 0.0045536896266971964;
	setAttr ".wl[578].w[5]" 0.0015095004792207828;
	setAttr -s 5 ".wl[579].w";
	setAttr ".wl[579].w[0]" 0.81443441010417394;
	setAttr ".wl[579].w[1]" 0.1595193432363918;
	setAttr ".wl[579].w[2]" 0.019983056119318072;
	setAttr ".wl[579].w[3]" 0.0045536897121859193;
	setAttr ".wl[579].w[5]" 0.0015095005077881162;
	setAttr -s 5 ".wl[580].w";
	setAttr ".wl[580].w[0]" 0.86551633666030847;
	setAttr ".wl[580].w[1]" 0.11307591215788051;
	setAttr ".wl[580].w[2]" 0.016034287769405003;
	setAttr ".wl[580].w[3]" 0.0039829859023318981;
	setAttr ".wl[580].w[5]" 0.0013904775100741179;
	setAttr -s 5 ".wl[581].w";
	setAttr ".wl[581].w[0]" 0.86551632892865848;
	setAttr ".wl[581].w[1]" 0.11307591822763;
	setAttr ".wl[581].w[2]" 0.01603428898438268;
	setAttr ".wl[581].w[3]" 0.003982986230800685;
	setAttr ".wl[581].w[5]" 0.0013904776285281655;
	setAttr -s 5 ".wl[582].w";
	setAttr ".wl[582].w[0]" 0.8655163253228858;
	setAttr ".wl[582].w[1]" 0.11307592105834996;
	setAttr ".wl[582].w[2]" 0.016034289551006008;
	setAttr ".wl[582].w[3]" 0.003982986383987106;
	setAttr ".wl[582].w[5]" 0.0013904776837710127;
	setAttr -s 5 ".wl[583].w";
	setAttr ".wl[583].w[0]" 0.86551632125980449;
	setAttr ".wl[583].w[1]" 0.11307592424808137;
	setAttr ".wl[583].w[2]" 0.016034290189492425;
	setAttr ".wl[583].w[3]" 0.0039829865566016866;
	setAttr ".wl[583].w[5]" 0.0013904777460201408;
	setAttr -s 5 ".wl[584].w";
	setAttr ".wl[584].w[0]" 0.86551631429948406;
	setAttr ".wl[584].w[1]" 0.1130759297122966;
	setAttr ".wl[584].w[2]" 0.016034291283260785;
	setAttr ".wl[584].w[3]" 0.0039829868523015869;
	setAttr ".wl[584].w[5]" 0.0013904778526569095;
	setAttr -s 5 ".wl[585].w";
	setAttr ".wl[585].w[0]" 0.86551629993009138;
	setAttr ".wl[585].w[1]" 0.11307594099302086;
	setAttr ".wl[585].w[2]" 0.016034293541316053;
	setAttr ".wl[585].w[3]" 0.0039829874627660593;
	setAttr ".wl[585].w[5]" 0.0013904780728056427;
	setAttr -s 5 ".wl[586].w";
	setAttr ".wl[586].w[0]" 0.86551628831867289;
	setAttr ".wl[586].w[1]" 0.11307595010859106;
	setAttr ".wl[586].w[2]" 0.016034295365973922;
	setAttr ".wl[586].w[3]" 0.0039829879560617058;
	setAttr ".wl[586].w[5]" 0.0013904782507003736;
	setAttr -s 5 ".wl[587].w";
	setAttr ".wl[587].w[0]" 0.86551628480787901;
	setAttr ".wl[587].w[1]" 0.11307595286474771;
	setAttr ".wl[587].w[2]" 0.016034295917672088;
	setAttr ".wl[587].w[3]" 0.0039829881052131175;
	setAttr ".wl[587].w[5]" 0.0013904783044880987;
	setAttr -s 5 ".wl[588].w";
	setAttr ".wl[588].w[0]" 0.86551626995022057;
	setAttr ".wl[588].w[1]" 0.11307596452878572;
	setAttr ".wl[588].w[2]" 0.01603429825245534;
	setAttr ".wl[588].w[3]" 0.003982988736421003;
	setAttr ".wl[588].w[5]" 0.001390478532117429;
	setAttr -s 5 ".wl[589].w";
	setAttr ".wl[589].w[0]" 0.86551625337981952;
	setAttr ".wl[589].w[1]" 0.11307597753741569;
	setAttr ".wl[589].w[2]" 0.016034300856384933;
	setAttr ".wl[589].w[3]" 0.0039829894403925273;
	setAttr ".wl[589].w[5]" 0.0013904787859871474;
	setAttr -s 5 ".wl[590].w";
	setAttr ".wl[590].w[0]" 0.86551626319057129;
	setAttr ".wl[590].w[1]" 0.11307596983546339;
	setAttr ".wl[590].w[2]" 0.016034299314689766;
	setAttr ".wl[590].w[3]" 0.0039829890235957375;
	setAttr ".wl[590].w[5]" 0.0013904786356798123;
	setAttr -s 5 ".wl[591].w";
	setAttr ".wl[591].w[0]" 0.86551625332687387;
	setAttr ".wl[591].w[1]" 0.11307597753284823;
	setAttr ".wl[591].w[2]" 0.016034300855854843;
	setAttr ".wl[591].w[3]" 0.0039829894402696993;
	setAttr ".wl[591].w[5]" 0.0013904787859455236;
	setAttr -s 5 ".wl[592].w";
	setAttr ".wl[592].w[0]" 0.86551623104957787;
	setAttr ".wl[592].w[1]" 0.11307598294649011;
	setAttr ".wl[592].w[2]" 0.016034302040057756;
	setAttr ".wl[592].w[3]" 0.0039829897657797523;
	setAttr ".wl[592].w[5]" 0.0013904789040317062;
	setAttr -s 5 ".wl[593].w";
	setAttr ".wl[593].w[0]" 0.86551622160158892;
	setAttr ".wl[593].w[1]" 0.1130760052068069;
	setAttr ".wl[593].w[2]" 0.016034306372284691;
	setAttr ".wl[593].w[3]" 0.0039829909304058631;
	setAttr ".wl[593].w[5]" 0.0013904793231656011;
	setAttr -s 5 ".wl[594].w";
	setAttr ".wl[594].w[0]" 0.86551618273485853;
	setAttr ".wl[594].w[1]" 0.11307602409381229;
	setAttr ".wl[594].w[2]" 0.01603431024969797;
	setAttr ".wl[594].w[3]" 0.0039829919838248479;
	setAttr ".wl[594].w[5]" 0.0013904797037278995;
	setAttr -s 5 ".wl[595].w";
	setAttr ".wl[595].w[0]" 0.86551620097591697;
	setAttr ".wl[595].w[1]" 0.11307602898784204;
	setAttr ".wl[595].w[2]" 0.016034311069324864;
	setAttr ".wl[595].w[3]" 0.0039829921968799588;
	setAttr ".wl[595].w[5]" 0.0013904797794484429;
	setAttr -s 5 ".wl[596].w";
	setAttr ".wl[596].w[0]" 0.86551616528548847;
	setAttr ".wl[596].w[1]" 0.11307603781554403;
	setAttr ".wl[596].w[2]" 0.016034312996177656;
	setAttr ".wl[596].w[3]" 0.003982992726324585;
	setAttr ".wl[596].w[5]" 0.0013904799714905315;
	setAttr -s 5 ".wl[597].w";
	setAttr ".wl[597].w[0]" 0.86551615550919769;
	setAttr ".wl[597].w[1]" 0.11307605716197974;
	setAttr ".wl[597].w[2]" 0.016034316771547805;
	setAttr ".wl[597].w[3]" 0.0039829937418128644;
	setAttr ".wl[597].w[5]" 0.0013904803370252405;
	setAttr -s 5 ".wl[598].w";
	setAttr ".wl[598].w[0]" 0.86551612438081149;
	setAttr ".wl[598].w[1]" 0.11307606669856857;
	setAttr ".wl[598].w[2]" 0.016034318804570364;
	setAttr ".wl[598].w[3]" 0.0039829942980556567;
	setAttr ".wl[598].w[5]" 0.0013904805384830222;
	setAttr -s 5 ".wl[599].w";
	setAttr ".wl[599].w[0]" 0.86551613692071372;
	setAttr ".wl[599].w[1]" 0.11307606867556021;
	setAttr ".wl[599].w[2]" 0.016034319101859189;
	setAttr ".wl[599].w[3]" 0.0039829943731790754;
	setAttr ".wl[599].w[5]" 0.0013904805648899711;
	setAttr -s 5 ".wl[600].w[1:5]"  0.0015113970462445612 0.0041146607782121675 
		0.015233955323574156 0.88503607826791186 0.094103908584057289;
	setAttr -s 5 ".wl[601].w[1:5]"  0.001511397161171374 0.0041146610815060002 
		0.01523395636322118 0.88503607197845335 0.094103913415647958;
	setAttr -s 5 ".wl[602].w[1:5]"  0.0015113972147625847 0.0041146612229341281 
		0.015233956848016147 0.88503606904563326 0.094103915668653865;
	setAttr -s 5 ".wl[603].w[1:5]"  0.0015113972751576844 0.0041146613823178331 
		0.015233957394360231 0.88503606574046512 0.094103918207699172;
	setAttr -s 5 ".wl[604].w[1:5]"  0.0015113973786247828 0.0041146616553692809 
		0.015233958330340735 0.88503606007814872 0.094103922557516401;
	setAttr -s 5 ".wl[605].w[1:5]"  0.0015113975922340136 0.0041146622190877035 
		0.015233960262685175 0.88503604838822048 0.094103931537772606;
	setAttr -s 5 ".wl[606].w[1:5]"  0.0015113977647982484 0.0041146626744876834 
		0.015233961823729764 0.88503603894451144 0.094103938792472905;
	setAttr -s 5 ".wl[607].w[1:5]"  0.0015113978169396533 0.0041146628120897451 
		0.015233962295409518 0.88503603609103343 0.094103940984527581;
	setAttr -s 5 ".wl[608].w[1:5]"  0.0015113980377970864 0.0041146633949362913 
		0.015233964293322307 0.88503602400444326 0.094103950269501052;
	setAttr -s 5 ".wl[609].w[1:5]"  0.0015113982840652372 0.0041146640448421487 
		0.015233966521104576 0.88503601052723335 0.094103960622754751;
	setAttr -s 5 ".wl[610].w[1:5]"  0.0015113981382235948 0.0041146636599635614 
		0.015233965201797064 0.88503601850852687 0.094103954491488909;
	setAttr -s 5 ".wl[611].w[1:5]"  0.0015113982840652372 0.0041146640448421487 
		0.015233966521104576 0.88503601052723335 0.094103960622754751;
	setAttr -s 5 ".wl[612].w[1:5]"  0.0015113984191168859 0.0041146644012457602 
		0.015233967742804019 0.8850360031364306 0.094103966300402797;
	setAttr -s 5 ".wl[613].w[1:5]"  0.0015113988004367539 0.0041146654075553957 
		0.01523397119228621 0.88503598226841629 0.094103982331305347;
	setAttr -s 5 ".wl[614].w[1:5]"  0.0015113991895060661 0.0041146664343159368 
		0.015233974711871004 0.88503596097631043 0.094103998687996598;
	setAttr -s 5 ".wl[615].w[1:5]"  0.0015113992302031667 0.0041146665417162781 
		0.015233975080023643 0.88503595874913166 0.094104000398925317;
	setAttr -s 5 ".wl[616].w[1:5]"  0.0015113994491397116 0.004114667119493539 
		0.015233977060559432 0.88503594676766839 0.094104009603138888;
	setAttr -s 5 ".wl[617].w[1:5]"  0.00151139978393429 0.0041146680030221192 
		0.015233980089165888 0.88503592844579082 0.094104023678086984;
	setAttr -s 5 ".wl[618].w[1:5]"  0.0015114000047919207 0.0041146685858691485 
		0.015233982087080027 0.88503591635919676 0.094104032963062176;
	setAttr -s 5 ".wl[619].w[1:5]"  0.0015114000105871496 0.0041146686011628531 
		0.015233982139504608 0.88503591604204868 0.094104033206696747;
	setAttr -s 5 ".wl[620].w[1:5]"  0.0013907927338780992 0.0039688822039572963 
		0.015877934761561418 0.86785491029726813 0.11090748000333503;
	setAttr -s 5 ".wl[621].w[1:5]"  0.0013907928518788627 0.003968882530013252 
		0.015877935961245367 0.86785490267743504 0.11090748597942743;
	setAttr -s 5 ".wl[622].w[1:5]"  0.001390792906903479 0.0039688826820555231 
		0.015877936520666731 0.86785489912425151 0.11090748876612276;
	setAttr -s 5 ".wl[623].w[1:5]"  0.001390792968913968 0.0039688828534009306 
		0.015877937151111684 0.86785489511995917 0.1109074919066142;
	setAttr -s 5 ".wl[624].w[1:5]"  0.0013907930751485031 0.0039688831469448177 
		0.015877938231171337 0.8678548882599243 0.11090749728681105;
	setAttr -s 5 ".wl[625].w[1:5]"  0.0013907932944711493 0.0039688837529701692 
		0.015877940460969152 0.86785487409728956 0.1109075083943;
	setAttr -s 5 ".wl[626].w[1:5]"  0.001390793471650967 0.003968884242547795 
		0.015877942262311439 0.86785486265600487 0.11090751736748496;
	setAttr -s 5 ".wl[627].w[1:5]"  0.0013907935251870006 0.0039688843904768555 
		0.015877942806598721 0.86785485919894645 0.11090752007879104;
	setAttr -s 5 ".wl[628].w[1:5]"  0.0013907937519517192 0.0039688850170658931 
		0.015877945112058065 0.86785484455574657 0.11090753156317781;
	setAttr -s 5 ".wl[629].w[1:5]"  0.0013907940048068182 0.0039688857157470329 
		0.015877947682771613 0.86785482822777682 0.11090754436889766;
	setAttr -s 5 ".wl[630].w[1:5]"  0.0013907938550643401 0.0039688853019833967 
		0.015877946160377888 0.86785483789730922 0.11090753678526506;
	setAttr -s 5 ".wl[631].w[1:5]"  0.0013907940048068182 0.0039688857157470329 
		0.015877947682771613 0.86785482822777682 0.11090754436889766;
	setAttr -s 5 ".wl[632].w[1:5]"  0.0013907941434707016 0.0039688860988986475 
		0.015877949092532047 0.86785481927363872 0.11090755139146;
	setAttr -s 5 ".wl[633].w[1:5]"  0.0013907945349897555 0.0039688871807315807 
		0.015877953073006556 0.86785479399152976 0.11090757121974232;
	setAttr -s 5 ".wl[634].w[1:5]"  0.0013907949344655339 0.0039688882845502673 
		0.015877957134374853 0.86785476819562402 0.11090759145098537;
	setAttr -s 5 ".wl[635].w[1:5]"  0.0013907949762511642 0.0039688884000109821 
		0.015877957559198668 0.86785476549734253 0.11090759356719671;
	setAttr -s 5 ".wl[636].w[1:5]"  0.0013907952010436223 0.0039688890211503009 
		0.015877959844606132 0.86785475098150777 0.11090760495169213;
	setAttr -s 5 ".wl[637].w[1:5]"  0.0013907955447929816 0.0039688899709875063 
		0.01587796333941785 0.86785472878410697 0.11090762236069479;
	setAttr -s 5 ".wl[638].w[1:5]"  0.0013907957715579137 0.0039688905975770851 
		0.015877965644878773 0.86785471414090398 0.11090763384508223;
	setAttr -s 5 ".wl[639].w[1:5]"  0.0013907957775081497 0.0039688906140185869 
		0.015877965705373292 0.86785471375667134 0.11090763414642869;
	setAttr -s 5 ".wl[640].w[1:5]"  0.0014921145466464849 0.0044827017657832974 
		0.019536148419873205 0.81997727090785344 0.15451176435984362;
	setAttr -s 5 ".wl[641].w[1:5]"  0.0014921146732322303 0.0044827021320486219 
		0.019536149858894892 0.81997726191984899 0.15451177141597527;
	setAttr -s 5 ".wl[642].w[1:5]"  0.001492114732260086 0.0044827023028408061 
		0.019536150529921175 0.81997725772867713 0.15451177470630081;
	setAttr -s 5 ".wl[643].w[1:5]"  0.0014921147987820623 0.0044827024953166079 
		0.019536151286140301 0.81997725300539837 0.15451177841436264;
	setAttr -s 5 ".wl[644].w[1:5]"  0.0014921149127455451 0.0044827028250604573 
		0.019536152581672551 0.81997724491361701 0.15451178476690447;
	setAttr -s 5 ".wl[645].w[1:5]"  0.001492115148024701 0.0044827035058211109 
		0.019536155256316402 0.81997722820802599 0.15451179788181182;
	setAttr -s 5 ".wl[646].w[1:5]"  0.0014921153380949915 0.0044827040557736631 
		0.019536157417027623 0.81997721471241392 0.15451180847668983;
	setAttr -s 5 ".wl[647].w[1:5]"  0.001492115395525964 0.0044827042219453984 
		0.019536158069900549 0.81997721063462725 0.1545118116780009;
	setAttr -s 5 ".wl[648].w[1:5]"  0.0014921156387886294 0.004482704925805654 
		0.019536160835300395 0.81997719336218466 0.15451182523792059;
	setAttr -s 5 ".wl[649].w[1:5]"  0.0014921159100398475 0.0044827057106484464 
		0.019536163918872848 0.81997717410246562 0.15451184035797319;
	setAttr -s 5 ".wl[650].w[1:5]"  0.0014921157494030668 0.0044827052458593104 
		0.019536162092760691 0.81997718550819942 0.1545118314037775;
	setAttr -s 5 ".wl[651].w[1:5]"  0.0014921159100398475 0.0044827057106484464 
		0.019536163918872848 0.81997717410246562 0.15451184035797319;
	setAttr -s 5 ".wl[652].w[1:5]"  0.0014921160587920269 0.0044827061410504737 
		0.019536165609881303 0.81997716354057815 0.15451184864969811;
	setAttr -s 5 ".wl[653].w[1:5]"  0.0014921164787954978 0.0044827073562954921 
		0.019536170384462759 0.81997713371897174 0.15451187206147451;
	setAttr -s 5 ".wl[654].w[1:5]"  0.0014921169073345722 0.0044827085962375404 
		0.019536175256076291 0.81997710329131557 0.15451189594903597;
	setAttr -s 5 ".wl[655].w[1:5]"  0.0014921169521602555 0.0044827087259369132 
		0.019536175765652686 0.81997710010854785 0.15451189844770227;
	setAttr -s 5 ".wl[656].w[1:5]"  0.0014921171933071728 0.0044827094236753809 
		0.019536178507000179 0.81997708298634209 0.1545119118896752;
	setAttr -s 5 ".wl[657].w[1:5]"  0.0014921175620655283 0.004482710490646879 
		0.019536182699028692 0.81997705680331789 0.1545119324449411;
	setAttr -s 5 ".wl[658].w[1:5]"  0.0014921178053284201 0.0044827111945077262 
		0.019536185464430245 0.81997703953087575 0.15451194600485788;
	setAttr -s 5 ".wl[659].w[1:5]"  0.001492117811711555 0.0044827112129767963 
		0.01953618553699344 0.81997703907765263 0.15451194636066554;
	setAttr -s 5 ".wl[660].w[1:5]"  0.0018233833023441647 0.0057952405576435278 
		0.027759173370243063 0.71870251722548395 0.24591968554428537;
	setAttr -s 5 ".wl[661].w[1:5]"  0.0018233834411359911 0.0057952409775086601 
		0.02775917510577933 0.71870250844193806 0.24591969203363787;
	setAttr -s 5 ".wl[662].w[1:5]"  0.0018233835058556315 0.0057952411732948277 
		0.027759175915072515 0.71870250434610716 0.24591969505966993;
	setAttr -s 5 ".wl[663].w[1:5]"  0.0018233835787920124 0.0057952413939378134 
		0.027759176827112743 0.71870249973027367 0.24591969846988382;
	setAttr -s 5 ".wl[664].w[1:5]"  0.0018233837037444681 0.0057952417719368638 
		0.027759178389593107 0.71870249182256407 0.24591970431216151;
	setAttr -s 5 ".wl[665].w[1:5]"  0.0018233839617105086 0.0057952425523210239 
		0.027759181615354973 0.71870247549699218 0.24591971637362134;
	setAttr -s 5 ".wl[666].w[1:5]"  0.0018233841701083958 0.0057952431827544316 
		0.027759184221286891 0.71870246230837886 0.24591972611747143;
	setAttr -s 5 ".wl[667].w[1:5]"  0.0018233842330771721 0.0057952433732439777 
		0.02775918500868612 0.71870245832335422 0.24591972906163856;
	setAttr -s 5 ".wl[668].w[1:5]"  0.0018233844997965305 0.0057952441801081608 
		0.027759188343904419 0.71870244144382656 0.24591974153236426;
	setAttr -s 5 ".wl[669].w[1:5]"  0.0018233847972032459 0.0057952450798059683 
		0.027759192062855587 0.71870242262223016 0.24591975543790492;
	setAttr -s 5 ".wl[670].w[1:5]"  0.0018233846210770055 0.0057952445469989242 
		0.027759189860467923 0.71870243376850496 0.24591974720295126;
	setAttr -s 5 ".wl[671].w[1:5]"  0.0018233847972032459 0.0057952450798059683 
		0.027759192062855587 0.71870242262223016 0.24591975543790492;
	setAttr -s 5 ".wl[672].w[1:5]"  0.0018233849602989074 0.0057952455731936489 
		0.027759194102301103 0.71870241230060605 0.24591976306360028;
	setAttr -s 5 ".wl[673].w[1:5]"  0.0018233854208013593 0.00579524696627934 
		0.027759199860698275 0.71870238315738755 0.24591978459483338;
	setAttr -s 5 ".wl[674].w[1:5]"  0.0018233858906624594 0.0057952483876762438 
		0.027759205736121131 0.7187023534219078 0.24591980656363224;
	setAttr -s 5 ".wl[675].w[1:5]"  0.0018233859398104743 0.0057952485363559989 
		0.02775920635069714 0.71870235031154273 0.24591980886159365;
	setAttr -s 5 ".wl[676].w[1:5]"  0.0018233862042100594 0.0057952493362024788 
		0.027759209656906706 0.71870233357883839 0.24591982122384232;
	setAttr -s 5 ".wl[677].w[1:5]"  0.0018233866085260559 0.0057952505593160536 
		0.027759214712713989 0.71870230799143509 0.24591984012800883;
	setAttr -s 5 ".wl[678].w[1:5]"  0.0018233868752456474 0.005795251366180856 
		0.027759218047933944 0.71870229111191364 0.24591985259872598;
	setAttr -s 5 ".wl[679].w[1:5]"  0.0018233868822442796 0.0057952513873527128 
		0.027759218135448963 0.71870229066900071 0.24591985292595334;
	setAttr -s 5 ".wl[680].w[1:5]"  0.0023062397728336212 0.0077974690694012066 
		0.04143978590442178 0.55115449789769033 0.39730200735565302;
	setAttr -s 5 ".wl[681].w[1:5]"  0.0023062399268362734 0.0077974695563055273 
		0.041439787978306657 0.55115449353679324 0.39730200900175822;
	setAttr -s 5 ".wl[682].w[1:5]"  0.0023062399986488341 0.0077974697833525604 
		0.041439788945374277 0.55115449150327545 0.39730200976934893;
	setAttr -s 5 ".wl[683].w[1:5]"  0.0023062400795786442 0.0077974700392252532 
		0.041439790035219817 0.55115448921158428 0.39730201063439197;
	setAttr -s 5 ".wl[684].w[1:5]"  0.0023062402182252068 0.0077974704775788028 
		0.041439791902310973 0.55115448528552646 0.39730201211635846;
	setAttr -s 5 ".wl[685].w[1:5]"  0.0023062405044629139 0.0077974713825656392 
		0.041439795756945917 0.55115447718012833 0.39730201517589736;
	setAttr -s 5 ".wl[686].w[1:5]"  0.0023062407357000692 0.0077974721136593239 
		0.04143979887091289 0.55115447063218237 0.39730201764754547;
	setAttr -s 5 ".wl[687].w[1:5]"  0.0023062408055698784 0.0077974723345640255 
		0.04143979981181823 0.55115446865367812 0.39730201839436974;
	setAttr -s 5 ".wl[688].w[1:5]"  0.0023062411015202203 0.0077974732702588978 
		0.041439803797248403 0.55115446027324944 0.3973020215577231;
	setAttr -s 5 ".wl[689].w[1:5]"  0.0023062414315210816 0.007797474313609983 
		0.041439808241221406 0.55115445092861304 0.39730202508503454;
	setAttr -s 5 ".wl[690].w[1:5]"  0.0023062412360923702 0.0077974736957305149 
		0.041439805609470998 0.55115445646256889 0.39730202299613721;
	setAttr -s 5 ".wl[691].w[1:5]"  0.0023062414315210816 0.007797474313609983 
		0.041439808241221406 0.55115445092861304 0.39730202508503454;
	setAttr -s 5 ".wl[692].w[1:5]"  0.0023062416124911365 0.0077974748857760658 
		0.041439810678263488 0.55115444580408346 0.39730202701938583;
	setAttr -s 5 ".wl[693].w[1:5]"  0.0023062421234621342 0.0077974765012934644 
		0.041439817559279141 0.5511544313349187 0.39730203248104651;
	setAttr -s 5 ".wl[694].w[1:5]"  0.0023062426448174369 0.0077974781496424721 
		0.041439824580134822 0.55115441657170561 0.39730203805369968;
	setAttr -s 5 ".wl[695].w[1:5]"  0.0023062426993518043 0.0077974783220616838 
		0.041439825314524413 0.55115441502745643 0.39730203863660568;
	setAttr -s 5 ".wl[696].w[1:5]"  0.0023062429927281358 0.007797479249618329 
		0.041439829265290266 0.55115440671992322 0.39730204177243994;
	setAttr -s 5 ".wl[697].w[1:5]"  0.0023062434413549469 0.0077974806680244204 
		0.041439835306743486 0.55115439401616706 0.39730204656771012;
	setAttr -s 5 ".wl[698].w[1:5]"  0.0023062437373055421 0.0077974816037199857 
		0.041439839292175255 0.55115438563574148 0.39730204973105782;
	setAttr -s 5 ".wl[699].w[1:5]"  0.0023062437450711839 0.0077974816282723198 
		0.041439839396751624 0.55115438541584194 0.39730204981406286;
	setAttr -s 5 ".wl[700].w[1:5]"  0.002748971492316303 0.0099491387043044548 
		0.059214834635576752 0.35815009999408148 0.569936955173721;
	setAttr -s 5 ".wl[701].w[1:5]"  0.0027489716746230018 0.0099491393127429054 
		0.059214837328957083 0.35815010240536821 0.56993694927830874;
	setAttr -s 5 ".wl[702].w[1:5]"  0.0027489717596339423 0.0099491395964621827 
		0.059214838584899898 0.3581501035297685 0.56993694652923554;
	setAttr -s 5 ".wl[703].w[1:5]"  0.0027489718554377898 0.0099491399162021845 
		0.059214840000296011 0.35815010479692172 0.56993694343114232;
	setAttr -s 5 ".wl[704].w[1:5]"  0.0027489720195661062 0.0099491404639712906 
		0.059214842425110645 0.35815010696777067 0.56993693812358126;
	setAttr -s 5 ".wl[705].w[1:5]"  0.0027489723584112457 0.0099491415948480457 
		0.059214847431173265 0.35815011144951703 0.56993692716605049;
	setAttr -s 5 ".wl[706].w[1:5]"  0.002748972632147322 0.0099491425084269197 
		0.059214851475321101 0.35815011507009542 0.56993691831400917;
	setAttr -s 5 ".wl[707].w[1:5]"  0.002748972714858456 0.009949142784470703 
		0.059214852697286623 0.35815011616407649 0.56993691563930782;
	setAttr -s 5 ".wl[708].w[1:5]"  0.0027489730652013058 0.0099491439537203828 
		0.059214857873214441 0.3581501207978951 0.56993690430996879;
	setAttr -s 5 ".wl[709].w[1:5]"  0.0027489734558527957 0.0099491452574978784 
		0.059214863644657452 0.35815012596485568 0.56993689167713624;
	setAttr -s 5 ".wl[710].w[1:5]"  0.0027489732245063797 0.0099491444853921571 
		0.059214860226770492 0.35815012290494752 0.5699368991583833;
	setAttr -s 5 ".wl[711].w[1:5]"  0.0027489734558527957 0.0099491452574978784 
		0.059214863644657452 0.35815012596485568 0.56993689167713624;
	setAttr -s 5 ".wl[712].w[1:5]"  0.0027489736700832116 0.0099491459724798878 
		0.059214866809674339 0.35815012879837821 0.56993688474938442;
	setAttr -s 5 ".wl[713].w[1:5]"  0.0027489742749652068 0.0099491479912396513 
		0.059214875746134599 0.35815013679885893 0.5699368651888016;
	setAttr -s 5 ".wl[714].w[1:5]"  0.002748974892140025 0.0099491500510259477 
		0.059214884864206563 0.35815014496192688 0.56993684523070065;
	setAttr -s 5 ".wl[715].w[1:5]"  0.002748974956697227 0.0099491502664819775 
		0.05921488581796739 0.35815014581579324 0.56993684314306015;
	setAttr -s 5 ".wl[716].w[1:5]"  0.0027489753039929813 0.0099491514255620229 
		0.059214890948875658 0.35815015040930143 0.56993683191226796;
	setAttr -s 5 ".wl[717].w[1:5]"  0.0027489758350725856 0.0099491531980103187 
		0.059214898794985149 0.3581501574336251 0.56993681473830682;
	setAttr -s 5 ".wl[718].w[1:5]"  0.0027489761854157242 0.0099491543672607895 
		0.059214903970914265 0.35815016206743661 0.56993680340897268;
	setAttr -s 5 ".wl[719].w[1:5]"  0.0027489761946086072 0.0099491543979415217 
		0.05921490410672884 0.35815016218902607 0.56993680311169503;
	setAttr -s 5 ".wl[720].w[1:5]"  0.0031229671136061535 0.01218430524538024 
		0.081855030986683827 0.21055607728338363 0.69228161937094623;
	setAttr -s 5 ".wl[721].w[1:5]"  0.0031229673420342485 0.012184306060902756 
		0.081855034825829481 0.21055608301234618 0.69228160875888733;
	setAttr -s 5 ".wl[722].w[1:5]"  0.0031229674485519342 0.012184306441186848 
		0.081855036616051063 0.21055608568380293 0.69228160381040726;
	setAttr -s 5 ".wl[723].w[1:5]"  0.0031229675685929994 0.012184306869751433 
		0.081855038633557323 0.21055608869442516 0.69228159823367308;
	setAttr -s 5 ".wl[724].w[1:5]"  0.0031229677742438053 0.012184307603955591 
		0.081855042089889266 0.21055609385213384 0.69228158867977752;
	setAttr -s 5 ".wl[725].w[1:5]"  0.0031229681988126884 0.012184309119730053 
		0.081855049225533161 0.21055610450029225 0.69228156895563187;
	setAttr -s 5 ".wl[726].w[1:5]"  0.0031229685418006879 0.012184310344248531 
		0.081855054990063084 0.21055611310240646 0.69228155302148131;
	setAttr -s 5 ".wl[727].w[1:5]"  0.0031229686454367438 0.012184310714244747 
		0.081855056731853226 0.21055611570159108 0.69228154820687415;
	setAttr -s 5 ".wl[728].w[1:5]"  0.0031229690844121073 0.01218431228145243 
		0.081855064109622608 0.21055612671105919 0.69228152781345365;
	setAttr -s 5 ".wl[729].w[1:5]"  0.0031229695738937088 0.012184314028974906 
		0.081855072336239287 0.21055613898721773 0.69228150507367447;
	setAttr -s 5 ".wl[730].w[1:5]"  0.0031229692840194401 0.012184312994080447 
		0.081855067464382147 0.21055613171719509 0.69228151854032283;
	setAttr -s 5 ".wl[731].w[1:5]"  0.0031229695738937088 0.012184314028974906 
		0.081855072336239287 0.21055613898721773 0.69228150507367447;
	setAttr -s 5 ".wl[732].w[1:5]"  0.0031229698423218271 0.012184314987303387 
		0.081855076847655181 0.21055614571937201 0.69228149260334759;
	setAttr -s 5 ".wl[733].w[1:5]"  0.0031229706002316609 0.012184317693154652 
		0.081855089585687699 0.21055616472768207 0.69228145739324387;
	setAttr -s 5 ".wl[734].w[1:5]"  0.0031229713735442372 0.012184320453995923 
		0.081855102582588934 0.21055618412228577 0.6922814214675852;
	setAttr -s 5 ".wl[735].w[1:5]"  0.0031229714544336274 0.012184320742783101 
		0.081855103942079677 0.21055618615098337 0.69228141770972029;
	setAttr -s 5 ".wl[736].w[1:5]"  0.0031229718895909994 0.012184322296359792 
		0.08185511125567678 0.21055619706468479 0.69228139749368778;
	setAttr -s 5 ".wl[737].w[1:5]"  0.003122972555027307 0.012184324672066548 
		0.081855122439521491 0.21055621375375411 0.69228136657963057;
	setAttr -s 5 ".wl[738].w[1:5]"  0.0031229729940030065 0.012184326239275151 
		0.081855129817290748 0.21055622476321417 0.69228134618621706;
	setAttr -s 5 ".wl[739].w[1:5]"  0.0031229730055215791 0.012184326280398169 
		0.081855130010880864 0.21055622505209856 0.69228134565110078;
	setAttr -s 5 ".wl[740].w[1:5]"  0.0037074950971851413 0.015716114005258051 
		0.11960823813162387 0.12714799562758891 0.73382015713834403;
	setAttr -s 5 ".wl[741].w[1:5]"  0.0037074953823564715 0.015716115095404874 
		0.11960824333909181 0.12714800100344717 0.73382014517969973;
	setAttr -s 5 ".wl[742].w[1:5]"  0.0037074955153339364 0.015716115603748269 
		0.11960824576737183 0.12714800351024882 0.73382013960329717;
	setAttr -s 5 ".wl[743].w[1:5]"  0.003707495665194095 0.015716116176630449 
		0.11960824850394394 0.1271480063353117 0.73382013331891982;
	setAttr -s 5 ".wl[744].w[1:5]"  0.0037074959219300847 0.015716117158075239 
		0.11960825319215815 0.12714801117512539 0.73382012255271112;
	setAttr -s 5 ".wl[745].w[1:5]"  0.0037074964519650229 0.015716119184281306 
		0.11960826287103912 0.12714802116698565 0.73382010032572886;
	setAttr -s 5 ".wl[746].w[1:5]"  0.0037074968801537856 0.015716120821151994 
		0.11960827069012304 0.12714802923890992 0.73382008236966123;
	setAttr -s 5 ".wl[747].w[1:5]"  0.0037074970095338027 0.015716121315743098 
		0.11960827305270996 0.12714803167789415 0.7338200769441191;
	setAttr -s 5 ".wl[748].w[1:5]"  0.0037074975575538938 0.015716123410702325 
		0.11960828306001245 0.12714804200879579 0.73382005396293548;
	setAttr -s 5 ".wl[749].w[1:5]"  0.0037074981686263464 0.015716125746696671 
		0.11960829421870225 0.12714805352831623 0.73382002833765858;
	setAttr -s 5 ".wl[750].w[1:5]"  0.0037074978067451669 0.015716124363305259 
		0.11960828761045204 0.12714804670637969 0.73382004351311791;
	setAttr -s 5 ".wl[751].w[1:5]"  0.0037074981686263464 0.015716125746696671 
		0.11960829421870225 0.12714805352831623 0.73382002833765858;
	setAttr -s 5 ".wl[752].w[1:5]"  0.0037074985037339912 0.015716127027738794 
		0.11960830033804515 0.12714805984553598 0.73382001428494614;
	setAttr -s 5 ".wl[753].w[1:5]"  0.0037074994499142295 0.015716130644775641 
		0.11960831761607689 0.12714807768227501 0.73381997460695836;
	setAttr -s 5 ".wl[754].w[1:5]"  0.0037075004153233572 0.015716134335320087 
		0.11960833524524031 0.12714809588149989 0.73381993412261637;
	setAttr -s 5 ".wl[755].w[1:5]"  0.0037075005163062684 0.015716134721355305 
		0.119608337089271 0.1271480977851597 0.73381992988790778;
	setAttr -s 5 ".wl[756].w[1:5]"  0.0037075010595599418 0.015716136798093236 
		0.11960834700952737 0.12714810802620008 0.73381990710661937;
	setAttr -s 5 ".wl[757].w[1:5]"  0.0037075018902955306 0.015716139973810477 
		0.11960836217943643 0.12714812368664719 0.73381987226981038;
	setAttr -s 5 ".wl[758].w[1:5]"  0.0037075024383160238 0.015716142068770773 
		0.11960837218673581 0.12714813401754521 0.7338198492886322;
	setAttr -s 5 ".wl[759].w[1:5]"  0.0037075024526958965 0.015716142123741828 
		0.11960837244932393 0.12714813428862448 0.7338198486856139;
	setAttr -s 5 ".wl[760].w[1:5]"  0.0048548324844379246 0.022554534297557601 
		0.19328587032504638 0.084768847078367154 0.69453591581459095;
	setAttr -s 5 ".wl[761].w[1:5]"  0.0048548328330092049 0.022554535707526763 
		0.19328587595522631 0.084768850999358103 0.69453590450487968;
	setAttr -s 5 ".wl[762].w[1:5]"  0.0048548329955505325 0.022554536365005658 
		0.19328587858062019 0.084768852827744712 0.69453589923107906;
	setAttr -s 5 ".wl[763].w[1:5]"  0.0048548331787279459 0.022554537105957416 
		0.19328588153933116 0.084768854888261386 0.69453589328772214;
	setAttr -s 5 ".wl[764].w[1:5]"  0.0048548334925420759 0.022554538375334023 
		0.19328588660810705 0.084768858418277554 0.69453588310573933;
	setAttr -s 5 ".wl[765].w[1:5]"  0.0048548341404156007 0.022554540995979203 
		0.19328589707266261 0.08476886570604332 0.69453586208489937;
	setAttr -s 5 ".wl[766].w[1:5]"  0.0048548346638002731 0.022554543113067548 
		0.19328590552645342 0.084768871593464967 0.69453584510321387;
	setAttr -s 5 ".wl[767].w[1:5]"  0.0048548348219443491 0.022554543752759518 
		0.19328590808082091 0.08476887337238756 0.69453583997208768;
	setAttr -s 5 ".wl[768].w[1:5]"  0.0048548354918015301 0.02255454646232832 
		0.19328591890045652 0.0847688809074406 0.69453581823797306;
	setAttr -s 5 ".wl[769].w[1:5]"  0.0048548362387290083 0.022554549483645967 
		0.19328593096494123 0.084768889309436976 0.69453579400324683;
	setAttr -s 5 ".wl[770].w[1:5]"  0.0048548357963935735 0.022554547694401527 
		0.19328592382027321 0.084768884333718819 0.694535808355213;
	setAttr -s 5 ".wl[771].w[1:5]"  0.0048548362387290083 0.022554549483645967 
		0.19328593096494123 0.084768889309436976 0.69453579400324683;
	setAttr -s 5 ".wl[772].w[1:5]"  0.0048548366483385568 0.022554551140514342 
		0.1932859375810152 0.084768893917029839 0.69453578071310207;
	setAttr -s 5 ".wl[773].w[1:5]"  0.0048548378048757319 0.022554555818700722 
		0.19328595626157116 0.084768906926618842 0.69453574318823352;
	setAttr -s 5 ".wl[774].w[1:5]"  0.0048548389849168063 0.022554560591960007 
		0.19328597532176003 0.084768920200595135 0.6945357049007681;
	setAttr -s 5 ".wl[775].w[1:5]"  0.0048548391083504698 0.022554561091248444 
		0.19328597731547764 0.084768921589068333 0.69453570089585515;
	setAttr -s 5 ".wl[776].w[1:5]"  0.0048548397723815256 0.022554563777250059 
		0.19328598804099772 0.08476892905858055 0.69453567935079019;
	setAttr -s 5 ".wl[777].w[1:5]"  0.0048548407878081234 0.022554567884644383 
		0.19328600444230304 0.084768940480848404 0.69453564640439602;
	setAttr -s 5 ".wl[778].w[1:5]"  0.0048548414576657642 0.022554570594214295 
		0.19328601526193062 0.084768948015900736 0.69453562467028862;
	setAttr -s 5 ".wl[779].w[1:5]"  0.0048548414752425991 0.022554570665312489 
		0.19328601554583386 0.084768948213617912 0.69453562409999314;
	setAttr -s 5 ".wl[780].w[1:5]"  0.0067109460525987766 0.034488816725263154 
		0.32445089386444842 0.060162230253035999 0.57418711310465365;
	setAttr -s 5 ".wl[781].w[1:5]"  0.0067109464705940626 0.034488818475057262 
		0.32445089646433567 0.060162232906552753 0.57418710568346032;
	setAttr -s 5 ".wl[782].w[1:5]"  0.0067109466655083079 0.034488819290998979 
		0.32445089767668206 0.060162234143906916 0.57418710222290381;
	setAttr -s 5 ".wl[783].w[1:5]"  0.006710946885168676 0.034488820210531873 
		0.32445089904294649 0.060162235538354328 0.57418709832299875;
	setAttr -s 5 ".wl[784].w[1:5]"  0.0067109472614843178 0.034488821785848389 
		0.32445090138359017 0.060162237927280385 0.57418709164179682;
	setAttr -s 5 ".wl[785].w[1:5]"  0.006710948038393073 0.034488825038110626 
		0.32445090621587991 0.060162242859250314 0.57418707784836609;
	setAttr -s 5 ".wl[786].w[1:5]"  0.0067109486660188577 0.034488827665450826 
		0.32445091011964455 0.060162246843542391 0.57418706670534347;
	setAttr -s 5 ".wl[787].w[1:5]"  0.0067109488556600649 0.034488828459318652 
		0.32445091129919218 0.060162248047422054 0.57418706333840708;
	setAttr -s 5 ".wl[788].w[1:5]"  0.0067109496589308993 0.034488831821936468 
		0.32445091629544859 0.060162253146743089 0.57418704907694107;
	setAttr -s 5 ".wl[789].w[1:5]"  0.0067109505546219059 0.034488835571439475 
		0.32445092186654667 0.060162258832765228 0.57418703317462672;
	setAttr -s 5 ".wl[790].w[1:5]"  0.0067109500241877154 0.0344888333509588 
		0.32445091856730546 0.060162255465465032 0.57418704259208297;
	setAttr -s 5 ".wl[791].w[1:5]"  0.0067109505546219059 0.034488835571439475 
		0.32445092186654667 0.060162258832765228 0.57418703317462672;
	setAttr -s 5 ".wl[792].w[1:5]"  0.0067109510458122764 0.034488837627639352 
		0.32445092492169531 0.06016226195093783 0.57418702445391523;
	setAttr -s 5 ".wl[793].w[1:5]"  0.0067109524326938418 0.034488843433342596 
		0.32445093354793947 0.060162270755132842 0.57418699983089128;
	setAttr -s 5 ".wl[794].w[1:5]"  0.006710953847760502 0.034488849357032732 
		0.32445094234948729 0.060162279738251431 0.57418697470746816;
	setAttr -s 5 ".wl[795].w[1:5]"  0.0067109539957781149 0.034488849976657535 
		0.32445094327013924 0.060162280677895995 0.57418697207952907;
	setAttr -s 5 ".wl[796].w[1:5]"  0.0067109547920624337 0.034488853310027927 
		0.32445094822293191 0.060162285732863398 0.57418695794211427;
	setAttr -s 5 ".wl[797].w[1:5]"  0.0067109560097287991 0.034488858407369018 
		0.32445095579666761 0.060162293462845198 0.57418693632338935;
	setAttr -s 5 ".wl[798].w[1:5]"  0.006710956813000173 0.034488861769987951 
		0.32445096079291541 0.060162298562166976 0.57418692206192956;
	setAttr -s 5 ".wl[799].w[1:5]"  0.0067109568340777415 0.034488861858221968 
		0.32445096092401521 0.06016229869597145 0.57418692168771368;
	setAttr -s 5 ".wl[800].w[1:5]"  0.0089262853419839697 0.051228265059030442 
		0.49807471879723952 0.041494306016261688 0.40027642478548436;
	setAttr -s 5 ".wl[801].w[1:5]"  0.0089262858649566852 0.051228267315331248 
		0.49807471439697554 0.041494307947436262 0.40027642447530037;
	setAttr -s 5 ".wl[802].w[1:5]"  0.0089262861088226769 0.051228268367460764 
		0.49807471234510031 0.04149430884795699 0.40027642433065924;
	setAttr -s 5 ".wl[803].w[1:5]"  0.0089262863836496471 0.051228269553167616 
		0.4980747100327213 0.041494309862806951 0.40027642416765452;
	setAttr -s 5 ".wl[804].w[1:5]"  0.0089262868544750986 0.051228271584485494 
		0.49807470607122145 0.041494311601417894 0.40027642388839996;
	setAttr -s 5 ".wl[805].w[1:5]"  0.0089262878265006125 0.05122827577816854 
		0.49807469789265307 0.041494315190803599 0.40027642331187413;
	setAttr -s 5 ".wl[806].w[1:5]"  0.008926288611751489 0.051228279166035458 
		0.49807469128559617 0.041494318090489042 0.4002764228461278;
	setAttr -s 5 ".wl[807].w[1:5]"  0.0089262888490201434 0.051228280189701457 
		0.49807468928923126 0.041494318966647806 0.40027642270539937;
	setAttr -s 5 ".wl[808].w[1:5]"  0.008926289854028437 0.051228284525684231 
		0.49807468083314871 0.041494322677828349 0.40027642210931025;
	setAttr -s 5 ".wl[809].w[1:5]"  0.0089262909746677666 0.051228289360542398 
		0.4980746714041544 0.041494326815997871 0.4002764214446376;
	setAttr -s 5 ".wl[810].w[1:5]"  0.0089262903110176837 0.051228286497307221 
		0.49807467698806751 0.041494324365346301 0.40027642183826129;
	setAttr -s 5 ".wl[811].w[1:5]"  0.0089262909746677666 0.051228289360542398 
		0.4980746714041544 0.041494326815997871 0.4002764214446376;
	setAttr -s 5 ".wl[812].w[1:5]"  0.0089262915892181546 0.051228292011943059 
		0.49807466623336372 0.041494329085339607 0.40027642108013556;
	setAttr -s 5 ".wl[813].w[1:5]"  0.0089262933244080959 0.051228299498202248 
		0.49807465163357878 0.041494335492851267 0.40027642005095959;
	setAttr -s 5 ".wl[814].w[1:5]"  0.0089262950948616731 0.051228307136601398 
		0.49807463673709046 0.041494342030579993 0.40027641900086663;
	setAttr -s 5 ".wl[815].w[1:5]"  0.0089262952800531672 0.051228307935586699 
		0.49807463517890072 0.041494342714434015 0.4002764188910255;
	setAttr -s 5 ".wl[816].w[1:5]"  0.0089262962763203089 0.051228312233855593 
		0.49807462679637104 0.041494346393335275 0.40027641830011784;
	setAttr -s 5 ".wl[817].w[1:5]"  0.0089262977997974779 0.051228318806705218 
		0.49807461397793074 0.041494352019057192 0.40027641739650938;
	setAttr -s 5 ".wl[818].w[1:5]"  0.0089262988048064273 0.05122832314268904 
		0.49807460552185012 0.041494355730238852 0.4002764168004157;
	setAttr -s 5 ".wl[819].w[1:5]"  0.0089262988311775149 0.051228323256463745 
		0.49807460529996528 0.041494355827618991 0.40027641678477449;
	setAttr -s 5 ".wl[820].w[1:5]"  0.011149121280578527 0.072066603465517562 
		0.64632162623620848 0.027098840521258244 0.24336380849643729;
	setAttr -s 5 ".wl[821].w[1:5]"  0.011149121989689148 0.072066606713839243 
		0.64632161599371973 0.027098842062828005 0.24336381323992387;
	setAttr -s 5 ".wl[822].w[1:5]"  0.011149122320352591 0.072066608228555235 
		0.64632161121757292 0.027098842781673207 0.24336381545184596;
	setAttr -s 5 ".wl[823].w[1:5]"  0.011149122692996741 0.072066609935578077 
		0.64632160583505138 0.027098843591782294 0.24336381794459155;
	setAttr -s 5 ".wl[824].w[1:5]"  0.011149123331399675 0.072066612859998977 
		0.64632159661387523 0.027098844979637163 0.2433638222150889;
	setAttr -s 5 ".wl[825].w[1:5]"  0.011149124649391195 0.072066618897505402 
		0.64632157757663322 0.027098847844882371 0.24336383103158779;
	setAttr -s 5 ".wl[826].w[1:5]"  0.011149125714130707 0.072066623774904984 
		0.64632156219739778 0.027098850159570798 0.24336383815399576;
	setAttr -s 5 ".wl[827].w[1:5]"  0.011149126035848658 0.072066625248642879 
		0.64632155755046228 0.027098850858968924 0.24336384030607727;
	setAttr -s 5 ".wl[828].w[1:5]"  0.01114912739856224 0.072066631491013 
		0.64632153786725333 0.027098853821437407 0.24336384942173406;
	setAttr -s 5 ".wl[829].w[1:5]"  0.011149128918062563 0.072066638451597373 
		0.6463215159193989 0.027098857124752077 0.24336385958618903;
	setAttr -s 5 ".wl[830].w[1:5]"  0.011149128018204347 0.072066634329492979 
		0.64632152891706407 0.027098855168507133 0.24336385356673135;
	setAttr -s 5 ".wl[831].w[1:5]"  0.011149128918062563 0.072066638451597373 
		0.6463215159193989 0.027098857124752077 0.24336385958618903;
	setAttr -s 5 ".wl[832].w[1:5]"  0.011149129751345377 0.07206664226873051 
		0.64632150388335796 0.027098858936265534 0.24336386516030067;
	setAttr -s 5 ".wl[833].w[1:5]"  0.011149132104128776 0.072066653046448007 
		0.64632146989946515 0.027098864051094036 0.24336388089886396;
	setAttr -s 5 ".wl[834].w[1:5]"  0.01114913450472689 0.072066664043195741 
		0.64632143522493735 0.027098869269869017 0.24336389695727098;
	setAttr -s 5 ".wl[835].w[1:5]"  0.011149134755832235 0.072066665193468202 
		0.64632143159794209 0.027098869815758927 0.24336389863699867;
	setAttr -s 5 ".wl[836].w[1:5]"  0.011149136106693412 0.072066671381541936 
		0.64632141208594396 0.027098872752460496 0.24336390767336025;
	setAttr -s 5 ".wl[837].w[1:5]"  0.011149138172410561 0.072066680844252967 
		0.64632138224848612 0.02709887724322145 0.24336392149162894;
	setAttr -s 5 ".wl[838].w[1:5]"  0.01114913953512491 0.072066687086623171 
		0.64632136256528472 0.027098880205691067 0.24336393060727624;
	setAttr -s 5 ".wl[839].w[1:5]"  0.011149139570882071 0.072066687250420841 
		0.64632136204880442 0.02709888028342524 0.24336393084646754;
	setAttr -s 5 ".wl[840].w[1:5]"  0.01414751966293766 0.10355325524210396 
		0.71887878710451503 0.018074148628340343 0.14534628936210303;
	setAttr -s 5 ".wl[841].w[1:5]"  0.014147520632828344 0.10355325987289056 
		0.71887877481323292 0.018074149834510573 0.14534629484653763;
	setAttr -s 5 ".wl[842].w[1:5]"  0.01414752108509543 0.10355326203226002 
		0.71887876908171877 0.018074150396956534 0.14534629740396918;
	setAttr -s 5 ".wl[843].w[1:5]"  0.014147521594781894 0.10355326446578073 
		0.71887876262253769 0.018074151030810077 0.14534630028608972;
	setAttr -s 5 ".wl[844].w[1:5]"  0.014147522467961667 0.10355326863481636 
		0.71887875155685965 0.018074152116709191 0.14534630522365319;
	setAttr -s 5 ".wl[845].w[1:5]"  0.014147524270653132 0.10355327724184644 
		0.71887872871161895 0.01807415435856265 0.14534631541731882;
	setAttr -s 5 ".wl[846].w[1:5]"  0.014147525726957526 0.10355328419503552 
		0.71887871025609151 0.01807415616964405 0.14534632365227135;
	setAttr -s 5 ".wl[847].w[1:5]"  0.014147526166989347 0.10355328629598665 
		0.71887870467963444 0.018074156716874058 0.14534632614051551;
	setAttr -s 5 ".wl[848].w[1:5]"  0.014147528030849697 0.10355329519506869 
		0.7188786810592136 0.018074159034797987 0.14534633668007005;
	setAttr -s 5 ".wl[849].w[1:5]"  0.014147530109156096 0.10355330511803174 
		0.71887865472115287 0.018074161619410136 0.14534634843224919;
	setAttr -s 5 ".wl[850].w[1:5]"  0.014147528878369186 0.10355329924158695 
		0.71887867031872765 0.018074160088785596 0.1453463414725305;
	setAttr -s 5 ".wl[851].w[1:5]"  0.014147530109156096 0.10355330511803174 
		0.71887865472115287 0.018074161619410136 0.14534634843224919;
	setAttr -s 5 ".wl[852].w[1:5]"  0.014147531248884054 0.10355331055971134 
		0.71887864027755488 0.018074163036792441 0.14534635487705724;
	setAttr -s 5 ".wl[853].w[1:5]"  0.014147534466918736 0.10355332592435336 
		0.71887859949589794 0.018074167038787271 0.14534637307404272;
	setAttr -s 5 ".wl[854].w[1:5]"  0.01414753775035227 0.10355334160124256 
		0.71887855788545763 0.018074171122113014 0.14534639164083463;
	setAttr -s 5 ".wl[855].w[1:5]"  0.014147538093803206 0.10355334324106316 
		0.71887855353295771 0.018074171549233593 0.14534639358294235;
	setAttr -s 5 ".wl[856].w[1:5]"  0.014147539941452259 0.10355335206273868 
		0.71887853011799296 0.018074173846996819 0.14534640403081919;
	setAttr -s 5 ".wl[857].w[1:5]"  0.014147542766850145 0.10355336555271455 
		0.71887849431217521 0.018074177360702711 0.14534642000755738;
	setAttr -s 5 ".wl[858].w[1:5]"  0.014147544630711405 0.10355337445179409 
		0.7188784706917607 0.01807417967862765 0.14534643054710614;
	setAttr -s 5 ".wl[859].w[1:5]"  0.014147544679618493 0.10355337468530294 
		0.71887847007196903 0.018074179739449216 0.14534643082366033;
	setAttr -s 5 ".wl[860].w[1:5]"  0.01975090239862403 0.16334331236711952 
		0.70923523164499935 0.013282513457017619 0.094388040132239587;
	setAttr -s 5 ".wl[861].w[1:5]"  0.019750903682565327 0.16334331795162857 
		0.7092352195772551 0.01328251435973673 0.094388044428814336;
	setAttr -s 5 ".wl[862].w[1:5]"  0.019750904281276495 0.16334332055572565 
		0.70923521394997846 0.013282514780681213 0.094388046432338293;
	setAttr -s 5 ".wl[863].w[1:5]"  0.019750904955999446 0.16334332349043634 
		0.70923520760826808 0.013282515255068402 0.09438804869022771;
	setAttr -s 5 ".wl[864].w[1:5]"  0.01975090611191482 0.16334332851809535 
		0.7092351967438385 0.013282516067774487 0.094388052558376831;
	setAttr -s 5 ".wl[865].w[1:5]"  0.019750908498317787 0.16334333889776481 
		0.70923517431407734 0.013282517745617234 0.094388060544222774;
	setAttr -s 5 ".wl[866].w[1:5]"  0.019750910426173524 0.16334334728298036 
		0.70923515619419519 0.013282519101062568 0.094388066995588341;
	setAttr -s 5 ".wl[867].w[1:5]"  0.019750911008687644 0.16334334981662749 
		0.70923515071915544 0.013282519510619175 0.094388068944910211;
	setAttr -s 5 ".wl[868].w[1:5]"  0.019750913476065914 0.16334336054849682 
		0.70923512752831264 0.013282521245394427 0.094388077201730355;
	setAttr -s 5 ".wl[869].w[1:5]"  0.019750916227327851 0.16334337251511752 
		0.70923510166925441 0.013282523179763889 0.094388086408536354;
	setAttr -s 5 ".wl[870].w[1:5]"  0.01975091459801219 0.16334336542840514 
		0.70923511698316066 0.013282522034217394 0.094388080956204504;
	setAttr -s 5 ".wl[871].w[1:5]"  0.019750916227327851 0.16334337251511752 
		0.70923510166925441 0.013282523179763889 0.094388086408536354;
	setAttr -s 5 ".wl[872].w[1:5]"  0.019750917736099681 0.16334337907752375 
		0.70923508748833775 0.013282524240557895 0.094388091457480866;
	setAttr -s 5 ".wl[873].w[1:5]"  0.019750921996133777 0.16334339760654837 
		0.70923504744836552 0.013282527235721648 0.094388105713230711;
	setAttr -s 5 ".wl[874].w[1:5]"  0.019750926342742836 0.16334341651212689 
		0.70923500659468253 0.013282530291754956 0.094388120258692754;
	setAttr -s 5 ".wl[875].w[1:5]"  0.019750926797403173 0.16334341848967199 
		0.70923500232134051 0.013282530611419575 0.094388121780164772;
	setAttr -s 5 ".wl[876].w[1:5]"  0.019750929243320798 0.16334342912819011 
		0.70923497933221735 0.013282532331106291 0.094388129965165407;
	setAttr -s 5 ".wl[877].w[1:5]"  0.019750932983582208 0.16334344539645385 
		0.70923494417759037 0.013282534960826061 0.094388142481547463;
	setAttr -s 5 ".wl[878].w[1:5]"  0.019750935450961519 0.16334345612831638 
		0.70923492098675411 0.013282536695602204 0.094388150738365817;
	setAttr -s 5 ".wl[879].w[1:5]"  0.019750935515704705 0.16334345640991679 
		0.70923492037823443 0.013282536741122142 0.094388150955021968;
	setAttr -s 5 ".wl[880].w[1:5]"  0.03002804744953684 0.27559099539905912 
		0.61717493099478526 0.010604502455327477 0.066601523701291146;
	setAttr -s 5 ".wl[881].w[1:5]"  0.030028049073107788 0.27559099937632919 
		0.61717492177194344 0.010604503112728321 0.066601526665891295;
	setAttr -s 5 ".wl[882].w[1:5]"  0.030028049830190744 0.27559100123095909 
		0.61717491747126518 0.010604503419279114 0.066601528048305866;
	setAttr -s 5 ".wl[883].w[1:5]"  0.03002805068339217 0.27559100332105074 
		0.61717491262457747 0.0106045037647493 0.066601529606230392;
	setAttr -s 5 ".wl[884].w[1:5]"  0.030028052145071683 0.27559100690173377 
		0.61717490432137523 0.010604504356598609 0.066601532275220698;
	setAttr -s 5 ".wl[885].w[1:5]"  0.03002805516272871 0.27559101429410149 
		0.61717488717930336 0.010604505578479518 0.066601537785386924;
	setAttr -s 5 ".wl[886].w[1:5]"  0.030028057600543084 0.27559102026602517 
		0.61717487333108068 0.010604506565576086 0.066601542236774877;
	setAttr -s 5 ".wl[887].w[1:5]"  0.030028058337144479 0.27559102207048036 
		0.6171748691467509 0.010604506863833713 0.066601543581790559;
	setAttr -s 5 ".wl[888].w[1:5]"  0.030028061457196477 0.2755910297136826 
		0.61717485142301831 0.010604508127175479 0.066601549278927072;
	setAttr -s 5 ".wl[889].w[1:5]"  0.030028064936225313 0.27559103823627007 
		0.6171748316600878 0.010604509535870778 0.0666015556315461;
	setAttr -s 5 ".wl[890].w[1:5]"  0.030028062875921264 0.27559103318913714 
		0.61717484336382678 0.010604508701632029 0.066601551869482828;
	setAttr -s 5 ".wl[891].w[1:5]"  0.030028064936225313 0.27559103823627007 
		0.6171748316600878 0.010604509535870778 0.0666015556315461;
	setAttr -s 5 ".wl[892].w[1:5]"  0.030028066844099175 0.2755910429099937 
		0.61717482082224262 0.010604510308388937 0.066601559115275558;
	setAttr -s 5 ".wl[893].w[1:5]"  0.030028072231002231 0.27559105610630158 
		0.61717479022146937 0.010604512489602641 0.066601568951624168;
	setAttr -s 5 ".wl[894].w[1:5]"  0.030028077727381045 0.27559106957078805 
		0.61717475899881447 0.010604514715144337 0.066601578987872181;
	setAttr -s 5 ".wl[895].w[1:5]"  0.030028078302308612 0.27559107097918861 
		0.61717475573288882 0.010604514947938572 0.066601580037675287;
	setAttr -s 5 ".wl[896].w[1:5]"  0.030028081395222995 0.27559107855590309 
		0.61717473816332369 0.010604516200292242 0.06660158568525805;
	setAttr -s 5 ".wl[897].w[1:5]"  0.030028086124862324 0.27559109014210098 
		0.61717471129620505 0.010604518115373173 0.066601594321458374;
	setAttr -s 5 ".wl[898].w[1:5]"  0.030028089244915401 0.27559109778529339 
		0.61717469357248023 0.010604519378715668 0.066601600018595233;
	setAttr -s 5 ".wl[899].w[1:5]"  0.030028089326784538 0.27559109798584824 
		0.61717469310741568 0.010604519411865344 0.066601600168086195;
	setAttr -s 5 ".wl[900].w[1:5]"  0.045575041155568825 0.44269166763111001 
		0.45639988178261509 0.0084010243572818152 0.046932385073424183;
	setAttr -s 5 ".wl[901].w[1:5]"  0.045575043212741577 0.44269166559385958 
		0.45639987916868885 0.0084010248491479464 0.046932387175561981;
	setAttr -s 5 ".wl[902].w[1:5]"  0.045575044172016216 0.44269166464387472 
		0.45639987794979625 0.0084010250785087007 0.046932388155804097;
	setAttr -s 5 ".wl[903].w[1:5]"  0.045575045253079413 0.44269166357328077 
		0.45639987657615422 0.0084010253369888772 0.04693238926049681;
	setAttr -s 5 ".wl[904].w[1:5]"  0.045575047105124847 0.44269166173917124 
		0.45639987422287065 0.0084010257798094665 0.046932391153023702;
	setAttr -s 5 ".wl[905].w[1:5]"  0.045575050928697673 0.44269165795262705 
		0.45639986936448584 0.0084010266940185811 0.046932395060170946;
	setAttr -s 5 ".wl[906].w[1:5]"  0.045575054017571129 0.44269165489366685 
		0.45639986543963962 0.0084010274325624704 0.046932398216559999;
	setAttr -s 5 ".wl[907].w[1:5]"  0.045575054950894228 0.4426916539693822 
		0.45639986425372192 0.0084010276557183062 0.046932399170283398;
	setAttr -s 5 ".wl[908].w[1:5]"  0.045575058904208259 0.44269165005435318 
		0.45639985923048254 0.0084010286009483775 0.04693240321000771;
	setAttr -s 5 ".wl[909].w[1:5]"  0.045575063312369837 0.44269164568888109 
		0.45639985362929592 0.0084010296549317017 0.046932407714521444;
	setAttr -s 5 ".wl[910].w[1:5]"  0.045575060701827201 0.44269164827414281 
		0.45639985694635576 0.0084010290307557512 0.046932405046918382;
	setAttr -s 5 ".wl[911].w[1:5]"  0.045575063312369837 0.44269164568888109 
		0.45639985362929592 0.0084010296549317017 0.046932407714521444;
	setAttr -s 5 ".wl[912].w[1:5]"  0.045575065729773247 0.4426916432948883 
		0.45639985055764637 0.0084010302329284355 0.046932410184763657;
	setAttr -s 5 ".wl[913].w[1:5]"  0.04557507255533863 0.44269163653542276 
		0.45639984188480986 0.0084010318649087052 0.04693241715952004;
	setAttr -s 5 ".wl[914].w[1:5]"  0.045575079519617027 0.44269162963858744 
		0.45639983303571902 0.0084010335300551305 0.046932424276021359;
	setAttr -s 5 ".wl[915].w[1:5]"  0.045575080248088568 0.44269162891717045 
		0.45639983211009405 0.0084010337042313699 0.046932425020415593;
	setAttr -s 5 ".wl[916].w[1:5]"  0.045575084167017256 0.44269162503619308 
		0.45639982713054666 0.008401034641240224 0.046932429025002907;
	setAttr -s 5 ".wl[917].w[1:5]"  0.04557509015978544 0.44269161910145932 
		0.4563998195158957 0.0084010360741004764 0.046932435148759055;
	setAttr -s 5 ".wl[918].w[1:5]"  0.045575094113100567 0.44269161518642808 
		0.45639981449265582 0.0084010370193311739 0.046932439188484415;
	setAttr -s 5 ".wl[919].w[1:5]"  0.045575094216834221 0.4426916150836992 
		0.45639981436084742 0.0084010370441337072 0.046932439294485449;
	setAttr -s 5 ".wl[920].w";
	setAttr ".wl[920].w[0]" 0.010433470359847076;
	setAttr ".wl[920].w[1]" 0.064924996848662112;
	setAttr ".wl[920].w[2]" 0.60683736497631968;
	setAttr ".wl[920].w[3]" 0.28676146593469293;
	setAttr ".wl[920].w[5]" 0.031042701880478293;
	setAttr -s 5 ".wl[921].w";
	setAttr ".wl[921].w[0]" 0.010433471001470702;
	setAttr ".wl[921].w[1]" 0.064924999727486166;
	setAttr ".wl[921].w[2]" 0.60683735613577505;
	setAttr ".wl[921].w[3]" 0.28676146960407961;
	setAttr ".wl[921].w[5]" 0.031042703531188581;
	setAttr -s 5 ".wl[922].w";
	setAttr ".wl[922].w[0]" 0.010433471300664467;
	setAttr ".wl[922].w[1]" 0.064925001069902691;
	setAttr ".wl[922].w[2]" 0.60683735201336497;
	setAttr ".wl[922].w[3]" 0.28676147131514107;
	setAttr ".wl[922].w[5]" 0.031042704300926791;
	setAttr -s 5 ".wl[923].w";
	setAttr ".wl[923].w[0]" 0.010433471637843587;
	setAttr ".wl[923].w[1]" 0.064925002582751162;
	setAttr ".wl[923].w[2]" 0.60683734736757777;
	setAttr ".wl[923].w[3]" 0.28676147324343731;
	setAttr ".wl[923].w[5]" 0.031042705168390222;
	setAttr -s 5 ".wl[924].w";
	setAttr ".wl[924].w[0]" 0.010433472215488872;
	setAttr ".wl[924].w[1]" 0.064925005174518269;
	setAttr ".wl[924].w[2]" 0.60683733940855311;
	setAttr ".wl[924].w[3]" 0.28676147654693696;
	setAttr ".wl[924].w[5]" 0.031042706654502861;
	setAttr -s 5 ".wl[925].w";
	setAttr ".wl[925].w[0]" 0.010433473408045386;
	setAttr ".wl[925].w[1]" 0.064925010525256482;
	setAttr ".wl[925].w[2]" 0.60683732297703996;
	setAttr ".wl[925].w[3]" 0.28676148336705559;
	setAttr ".wl[925].w[5]" 0.0310427097226025;
	setAttr -s 5 ".wl[926].w";
	setAttr ".wl[926].w[0]" 0.010433474371452251;
	setAttr ".wl[926].w[1]" 0.064925014847850404;
	setAttr ".wl[926].w[2]" 0.60683730970284255;
	setAttr ".wl[926].w[3]" 0.2867614888766879;
	setAttr ".wl[926].w[5]" 0.031042712201166934;
	setAttr -s 5 ".wl[927].w";
	setAttr ".wl[927].w[0]" 0.010433474662551885;
	setAttr ".wl[927].w[1]" 0.064925016153950202;
	setAttr ".wl[927].w[2]" 0.60683730569195793;
	setAttr ".wl[927].w[3]" 0.28676149054145883;
	setAttr ".wl[927].w[5]" 0.031042712950081246;
	setAttr -s 5 ".wl[928].w";
	setAttr ".wl[928].w[0]" 0.010433475895574222;
	setAttr ".wl[928].w[1]" 0.064925021686248918;
	setAttr ".wl[928].w[2]" 0.60683728870289488;
	setAttr ".wl[928].w[3]" 0.28676149759299452;
	setAttr ".wl[928].w[5]" 0.031042716122287446;
	setAttr -s 5 ".wl[929].w";
	setAttr ".wl[929].w[0]" 0.01043347727046171;
	setAttr ".wl[929].w[1]" 0.064925027855064862;
	setAttr ".wl[929].w[2]" 0.60683726975916052;
	setAttr ".wl[929].w[3]" 0.28676150545584173;
	setAttr ".wl[929].w[5]" 0.031042719659471123;
	setAttr -s 5 ".wl[930].w";
	setAttr ".wl[930].w[0]" 0.010433476456244175;
	setAttr ".wl[930].w[1]" 0.064925024201850992;
	setAttr ".wl[930].w[2]" 0.60683728097776601;
	setAttr ".wl[930].w[3]" 0.28676150079941137;
	setAttr ".wl[930].w[5]" 0.03104271756472738;
	setAttr -s 5 ".wl[931].w";
	setAttr ".wl[931].w[0]" 0.01043347727046171;
	setAttr ".wl[931].w[1]" 0.064925027855064862;
	setAttr ".wl[931].w[2]" 0.60683726975916052;
	setAttr ".wl[931].w[3]" 0.28676150545584173;
	setAttr ".wl[931].w[5]" 0.031042719659471123;
	setAttr -s 5 ".wl[932].w";
	setAttr ".wl[932].w[0]" 0.010433478024439913;
	setAttr ".wl[932].w[1]" 0.064925031237998101;
	setAttr ".wl[932].w[2]" 0.60683725937055688;
	setAttr ".wl[932].w[3]" 0.28676150976776849;
	setAttr ".wl[932].w[5]" 0.031042721599236649;
	setAttr -s 5 ".wl[933].w";
	setAttr ".wl[933].w[0]" 0.010433480153305842;
	setAttr ".wl[933].w[1]" 0.06492504078974734;
	setAttr ".wl[933].w[2]" 0.60683723003822154;
	setAttr ".wl[933].w[3]" 0.28676152194253907;
	setAttr ".wl[933].w[5]" 0.031042727076186181;
	setAttr -s 5 ".wl[934].w";
	setAttr ".wl[934].w[0]" 0.010433482325435915;
	setAttr ".wl[934].w[1]" 0.064925050535612275;
	setAttr ".wl[934].w[2]" 0.60683720010978204;
	setAttr ".wl[934].w[3]" 0.28676153436472845;
	setAttr ".wl[934].w[5]" 0.031042732664441464;
	setAttr -s 5 ".wl[935].w";
	setAttr ".wl[935].w[0]" 0.010433482552643238;
	setAttr ".wl[935].w[1]" 0.064925051555040955;
	setAttr ".wl[935].w[2]" 0.60683719697923277;
	setAttr ".wl[935].w[3]" 0.28676153566410356;
	setAttr ".wl[935].w[5]" 0.031042733248979396;
	setAttr -s 5 ".wl[936].w";
	setAttr ".wl[936].w[0]" 0.010433483774941202;
	setAttr ".wl[936].w[1]" 0.064925057039219788;
	setAttr ".wl[936].w[2]" 0.60683718013794663;
	setAttr ".wl[936].w[3]" 0.28676154265429799;
	setAttr ".wl[936].w[5]" 0.031042736393594381;
	setAttr -s 5 ".wl[937].w";
	setAttr ".wl[937].w[0]" 0.010433485644061389;
	setAttr ".wl[937].w[1]" 0.064925065425545311;
	setAttr ".wl[937].w[2]" 0.60683715438450159;
	setAttr ".wl[937].w[3]" 0.28676155334359826;
	setAttr ".wl[937].w[5]" 0.031042741202293476;
	setAttr -s 5 ".wl[938].w";
	setAttr ".wl[938].w[0]" 0.010433486877084461;
	setAttr ".wl[938].w[1]" 0.064925070957844527;
	setAttr ".wl[938].w[2]" 0.60683713739544565;
	setAttr ".wl[938].w[3]" 0.28676156039512463;
	setAttr ".wl[938].w[5]" 0.031042744374500799;
	setAttr -s 5 ".wl[939].w";
	setAttr ".wl[939].w[0]" 0.010433486909438554;
	setAttr ".wl[939].w[1]" 0.064925071103010129;
	setAttr ".wl[939].w[2]" 0.6068371369496588;
	setAttr ".wl[939].w[3]" 0.28676156058015412;
	setAttr ".wl[939].w[5]" 0.031042744457738441;
	setAttr -s 5 ".wl[940].w";
	setAttr ".wl[940].w[0]" 0.013028722699861429;
	setAttr ".wl[940].w[1]" 0.091702862278653333;
	setAttr ".wl[940].w[2]" 0.70512456631124221;
	setAttr ".wl[940].w[3]" 0.16979432407608913;
	setAttr ".wl[940].w[5]" 0.020349524634153886;
	setAttr -s 5 ".wl[941].w";
	setAttr ".wl[941].w[0]" 0.013028723581530214;
	setAttr ".wl[941].w[1]" 0.09170286646582243;
	setAttr ".wl[941].w[2]" 0.70512455434388199;
	setAttr ".wl[941].w[3]" 0.16979432966521185;
	setAttr ".wl[941].w[5]" 0.020349525943553552;
	setAttr -s 5 ".wl[942].w";
	setAttr ".wl[942].w[0]" 0.013028723992658793;
	setAttr ".wl[942].w[1]" 0.091702868418329933;
	setAttr ".wl[942].w[2]" 0.70512454876341457;
	setAttr ".wl[942].w[3]" 0.16979433227146049;
	setAttr ".wl[942].w[5]" 0.020349526554136174;
	setAttr -s 5 ".wl[943].w";
	setAttr ".wl[943].w[0]" 0.013028724455983841;
	setAttr ".wl[943].w[1]" 0.091702870618725674;
	setAttr ".wl[943].w[2]" 0.70512454247445711;
	setAttr ".wl[943].w[3]" 0.16979433520859569;
	setAttr ".wl[943].w[5]" 0.020349527242237736;
	setAttr -s 5 ".wl[944].w";
	setAttr ".wl[944].w[0]" 0.013028725249738613;
	setAttr ".wl[944].w[1]" 0.091702874388378527;
	setAttr ".wl[944].w[2]" 0.70512453170040135;
	setAttr ".wl[944].w[3]" 0.16979434024040849;
	setAttr ".wl[944].w[5]" 0.02034952842107297;
	setAttr -s 5 ".wl[945].w";
	setAttr ".wl[945].w[0]" 0.013028726888456089;
	setAttr ".wl[945].w[1]" 0.091702882170877464;
	setAttr ".wl[945].w[2]" 0.70512450945721883;
	setAttr ".wl[945].w[3]" 0.16979435062865336;
	setAttr ".wl[945].w[5]" 0.020349530854794264;
	setAttr -s 5 ".wl[946].w";
	setAttr ".wl[946].w[0]" 0.013028728212294095;
	setAttr ".wl[946].w[1]" 0.091702888457969201;
	setAttr ".wl[946].w[2]" 0.705124491488064;
	setAttr ".wl[946].w[3]" 0.16979435902079656;
	setAttr ".wl[946].w[5]" 0.020349532820876121;
	setAttr -s 5 ".wl[947].w";
	setAttr ".wl[947].w[0]" 0.013028728612300344;
	setAttr ".wl[947].w[1]" 0.091702890357654707;
	setAttr ".wl[947].w[2]" 0.70512448605856748;
	setAttr ".wl[947].w[3]" 0.16979436155653699;
	setAttr ".wl[947].w[5]" 0.020349533414940526;
	setAttr -s 5 ".wl[948].w";
	setAttr ".wl[948].w[0]" 0.01302873030662274;
	setAttr ".wl[948].w[1]" 0.091702898404227975;
	setAttr ".wl[948].w[2]" 0.70512446306063392;
	setAttr ".wl[948].w[3]" 0.16979437229727254;
	setAttr ".wl[948].w[5]" 0.020349535931242734;
	setAttr -s 5 ".wl[949].w";
	setAttr ".wl[949].w[0]" 0.013028732195885066;
	setAttr ".wl[949].w[1]" 0.091702907376597295;
	setAttr ".wl[949].w[2]" 0.70512443741668041;
	setAttr ".wl[949].w[3]" 0.16979438427377966;
	setAttr ".wl[949].w[5]" 0.020349538737057551;
	setAttr -s 5 ".wl[950].w";
	setAttr ".wl[950].w[0]" 0.013028731077051334;
	setAttr ".wl[950].w[1]" 0.091702902063100541;
	setAttr ".wl[950].w[2]" 0.7051244526032;
	setAttr ".wl[950].w[3]" 0.16979437718121265;
	setAttr ".wl[950].w[5]" 0.020349537075435332;
	setAttr -s 5 ".wl[951].w";
	setAttr ".wl[951].w[0]" 0.013028732195885066;
	setAttr ".wl[951].w[1]" 0.091702907376597295;
	setAttr ".wl[951].w[2]" 0.70512443741668041;
	setAttr ".wl[951].w[3]" 0.16979438427377966;
	setAttr ".wl[951].w[5]" 0.020349538737057551;
	setAttr -s 5 ".wl[952].w";
	setAttr ".wl[952].w[0]" 0.013028733231942641;
	setAttr ".wl[952].w[1]" 0.091702912296978453;
	setAttr ".wl[952].w[2]" 0.7051244233537256;
	setAttr ".wl[952].w[3]" 0.16979439084160752;
	setAttr ".wl[952].w[5]" 0.020349540275745769;
	setAttr -s 5 ".wl[953].w";
	setAttr ".wl[953].w[0]" 0.013028736157262823;
	setAttr ".wl[953].w[1]" 0.091702926189728418;
	setAttr ".wl[953].w[2]" 0.70512438364681962;
	setAttr ".wl[953].w[3]" 0.16979440938593995;
	setAttr ".wl[953].w[5]" 0.020349544620249162;
	setAttr -s 5 ".wl[954].w";
	setAttr ".wl[954].w[0]" 0.013028739142033159;
	setAttr ".wl[954].w[1]" 0.091702940364813357;
	setAttr ".wl[954].w[2]" 0.70512434313297212;
	setAttr ".wl[954].w[3]" 0.16979442830713731;
	setAttr ".wl[954].w[5]" 0.020349549053044098;
	setAttr -s 5 ".wl[955].w";
	setAttr ".wl[955].w[0]" 0.013028739454243592;
	setAttr ".wl[955].w[1]" 0.091702941847543545;
	setAttr ".wl[955].w[2]" 0.70512433889517701;
	setAttr ".wl[955].w[3]" 0.16979443028631622;
	setAttr ".wl[955].w[5]" 0.020349549516719578;
	setAttr -s 5 ".wl[956].w";
	setAttr ".wl[956].w[0]" 0.013028741133829307;
	setAttr ".wl[956].w[1]" 0.091702949824126176;
	setAttr ".wl[956].w[2]" 0.70512431609728565;
	setAttr ".wl[956].w[3]" 0.16979444093362325;
	setAttr ".wl[956].w[5]" 0.020349552011135606;
	setAttr -s 5 ".wl[957].w";
	setAttr ".wl[957].w[0]" 0.01302874370222722;
	setAttr ".wl[957].w[1]" 0.091702962021798604;
	setAttr ".wl[957].w[2]" 0.7051242812350873;
	setAttr ".wl[957].w[3]" 0.16979445721532682;
	setAttr ".wl[957].w[5]" 0.020349555825560063;
	setAttr -s 5 ".wl[958].w";
	setAttr ".wl[958].w[0]" 0.013028745396550493;
	setAttr ".wl[958].w[1]" 0.091702970068370332;
	setAttr ".wl[958].w[2]" 0.70512425823716052;
	setAttr ".wl[958].w[3]" 0.16979446795605532;
	setAttr ".wl[958].w[5]" 0.020349558341863326;
	setAttr -s 5 ".wl[959].w";
	setAttr ".wl[959].w[0]" 0.013028745441008956;
	setAttr ".wl[959].w[1]" 0.091702970279509619;
	setAttr ".wl[959].w[2]" 0.7051242576337029;
	setAttr ".wl[959].w[3]" 0.16979446823788838;
	setAttr ".wl[959].w[5]" 0.02034955840789026;
	setAttr -s 5 ".wl[960].w";
	setAttr ".wl[960].w[0]" 0.01758435084671842;
	setAttr ".wl[960].w[1]" 0.14010905312636279;
	setAttr ".wl[960].w[2]" 0.7210158586571378;
	setAttr ".wl[960].w[3]" 0.10683385674590165;
	setAttr ".wl[960].w[5]" 0.014456880623879419;
	setAttr -s 5 ".wl[961].w";
	setAttr ".wl[961].w[0]" 0.017584352028084178;
	setAttr ".wl[961].w[1]" 0.14010905855520081;
	setAttr ".wl[961].w[2]" 0.721015846318663;
	setAttr ".wl[961].w[3]" 0.10683386148188162;
	setAttr ".wl[961].w[5]" 0.014456881616170425;
	setAttr -s 5 ".wl[962].w";
	setAttr ".wl[962].w[0]" 0.017584352578963638;
	setAttr ".wl[962].w[1]" 0.14010906108670734;
	setAttr ".wl[962].w[2]" 0.72101584056514256;
	setAttr ".wl[962].w[3]" 0.10683386369030354;
	setAttr ".wl[962].w[5]" 0.014456882078882955;
	setAttr -s 5 ".wl[963].w";
	setAttr ".wl[963].w[0]" 0.017584353199782195;
	setAttr ".wl[963].w[1]" 0.14010906393961139;
	setAttr ".wl[963].w[2]" 0.72101583408116099;
	setAttr ".wl[963].w[3]" 0.10683386617910447;
	setAttr ".wl[963].w[5]" 0.014456882600340995;
	setAttr -s 5 ".wl[964].w";
	setAttr ".wl[964].w[0]" 0.017584354263350203;
	setAttr ".wl[964].w[1]" 0.14010906882712204;
	setAttr ".wl[964].w[2]" 0.72101582297299605;
	setAttr ".wl[964].w[3]" 0.10683387044284436;
	setAttr ".wl[964].w[5]" 0.014456883493687496;
	setAttr -s 5 ".wl[965].w";
	setAttr ".wl[965].w[0]" 0.017584356459100701;
	setAttr ".wl[965].w[1]" 0.14010907891745289;
	setAttr ".wl[965].w[2]" 0.72101580004004051;
	setAttr ".wl[965].w[3]" 0.10683387924539241;
	setAttr ".wl[965].w[5]" 0.014456885338013427;
	setAttr -s 5 ".wl[966].w";
	setAttr ".wl[966].w[0]" 0.017584358232937868;
	setAttr ".wl[966].w[1]" 0.14010908706892661;
	setAttr ".wl[966].w[2]" 0.72101578151365253;
	setAttr ".wl[966].w[3]" 0.10683388635653081;
	setAttr ".wl[966].w[5]" 0.014456886827952231;
	setAttr -s 5 ".wl[967].w";
	setAttr ".wl[967].w[0]" 0.017584358768914274;
	setAttr ".wl[967].w[1]" 0.14010908953194703;
	setAttr ".wl[967].w[2]" 0.72101577591578447;
	setAttr ".wl[967].w[3]" 0.10683388850520735;
	setAttr ".wl[967].w[5]" 0.014456887278146915;
	setAttr -s 5 ".wl[968].w";
	setAttr ".wl[968].w[0]" 0.01758436103917092;
	setAttr ".wl[968].w[1]" 0.14010909996466062;
	setAttr ".wl[968].w[2]" 0.72101575220467218;
	setAttr ".wl[968].w[3]" 0.10683389760644174;
	setAttr ".wl[968].w[5]" 0.014456889185054471;
	setAttr -s 5 ".wl[969].w";
	setAttr ".wl[969].w[0]" 0.017584363570631426;
	setAttr ".wl[969].w[1]" 0.14010911159770634;
	setAttr ".wl[969].w[2]" 0.72101572576548567;
	setAttr ".wl[969].w[3]" 0.1068339077548157;
	setAttr ".wl[969].w[5]" 0.014456891311360864;
	setAttr -s 5 ".wl[970].w";
	setAttr ".wl[970].w[0]" 0.017584362071483631;
	setAttr ".wl[970].w[1]" 0.14010910470853921;
	setAttr ".wl[970].w[2]" 0.72101574142294811;
	setAttr ".wl[970].w[3]" 0.10683390174488107;
	setAttr ".wl[970].w[5]" 0.014456890052148031;
	setAttr -s 5 ".wl[971].w";
	setAttr ".wl[971].w[0]" 0.017584363570631426;
	setAttr ".wl[971].w[1]" 0.14010911159770634;
	setAttr ".wl[971].w[2]" 0.72101572576548567;
	setAttr ".wl[971].w[3]" 0.1068339077548157;
	setAttr ".wl[971].w[5]" 0.014456891311360864;
	setAttr -s 5 ".wl[972].w";
	setAttr ".wl[972].w[0]" 0.01758436495886578;
	setAttr ".wl[972].w[1]" 0.14010911797718259;
	setAttr ".wl[972].w[2]" 0.72101571126643105;
	setAttr ".wl[972].w[3]" 0.10683391332010898;
	setAttr ".wl[972].w[5]" 0.014456892477411666;
	setAttr -s 5 ".wl[973].w";
	setAttr ".wl[973].w[0]" 0.017584368878560998;
	setAttr ".wl[973].w[1]" 0.14010913598970287;
	setAttr ".wl[973].w[2]" 0.72101567032819158;
	setAttr ".wl[973].w[3]" 0.10683392903377543;
	setAttr ".wl[973].w[5]" 0.014456895769769194;
	setAttr -s 5 ".wl[974].w";
	setAttr ".wl[974].w[0]" 0.017584372877914603;
	setAttr ".wl[974].w[1]" 0.14010915436828086;
	setAttr ".wl[974].w[2]" 0.7210156285579864;
	setAttr ".wl[974].w[3]" 0.10683394506678212;
	setAttr ".wl[974].w[5]" 0.014456899129036005;
	setAttr -s 5 ".wl[975].w";
	setAttr ".wl[975].w[0]" 0.01758437329625161;
	setAttr ".wl[975].w[1]" 0.14010915629070123;
	setAttr ".wl[975].w[2]" 0.72101562418877496;
	setAttr ".wl[975].w[3]" 0.10683394674385301;
	setAttr ".wl[975].w[5]" 0.014456899480419193;
	setAttr -s 5 ".wl[976].w";
	setAttr ".wl[976].w[0]" 0.017584375546762142;
	setAttr ".wl[976].w[1]" 0.14010916663266659;
	setAttr ".wl[976].w[2]" 0.7210156006839078;
	setAttr ".wl[976].w[3]" 0.10683395576592239;
	setAttr ".wl[976].w[5]" 0.014456901370741022;
	setAttr -s 5 ".wl[977].w";
	setAttr ".wl[977].w[0]" 0.017584378988209928;
	setAttr ".wl[977].w[1]" 0.14010918244744672;
	setAttr ".wl[977].w[2]" 0.72101556474061246;
	setAttr ".wl[977].w[3]" 0.10683396956233741;
	setAttr ".wl[977].w[5]" 0.014456904261393514;
	setAttr -s 5 ".wl[978].w";
	setAttr ".wl[978].w[0]" 0.01758438125846758;
	setAttr ".wl[978].w[1]" 0.14010919288015497;
	setAttr ".wl[978].w[2]" 0.72101554102950638;
	setAttr ".wl[978].w[3]" 0.10683397866356915;
	setAttr ".wl[978].w[5]" 0.014456906168302006;
	setAttr -s 5 ".wl[979].w";
	setAttr ".wl[979].w[0]" 0.017584381318038373;
	setAttr ".wl[979].w[1]" 0.14010919315390574;
	setAttr ".wl[979].w[2]" 0.72101554040733484;
	setAttr ".wl[979].w[3]" 0.1068339789023824;
	setAttr ".wl[979].w[5]" 0.014456906218338637;
	setAttr -s 5 ".wl[980].w";
	setAttr ".wl[980].w[0]" 0.026218496481787857;
	setAttr ".wl[980].w[1]" 0.23369910997994511;
	setAttr ".wl[980].w[2]" 0.6548061534877383;
	setAttr ".wl[980].w[3]" 0.073943570692056343;
	setAttr ".wl[980].w[5]" 0.011332669358472398;
	setAttr -s 5 ".wl[981].w";
	setAttr ".wl[981].w[0]" 0.026218497997195604;
	setAttr ".wl[981].w[1]" 0.23369911491325956;
	setAttr ".wl[981].w[2]" 0.65480614296664075;
	setAttr ".wl[981].w[3]" 0.073943574037679816;
	setAttr ".wl[981].w[5]" 0.011332670085224251;
	setAttr -s 5 ".wl[982].w";
	setAttr ".wl[982].w[0]" 0.026218498703841291;
	setAttr ".wl[982].w[1]" 0.23369911721369996;
	setAttr ".wl[982].w[2]" 0.65480613806057641;
	setAttr ".wl[982].w[3]" 0.073943575597768388;
	setAttr ".wl[982].w[5]" 0.01133267042411394;
	setAttr -s 5 ".wl[983].w";
	setAttr ".wl[983].w[0]" 0.026218499500201959;
	setAttr ".wl[983].w[1]" 0.23369911980620159;
	setAttr ".wl[983].w[2]" 0.65480613253164355;
	setAttr ".wl[983].w[3]" 0.073943577355924203;
	setAttr ".wl[983].w[5]" 0.01133267080602871;
	setAttr -s 5 ".wl[984].w";
	setAttr ".wl[984].w[0]" 0.026218500864503544;
	setAttr ".wl[984].w[1]" 0.23369912424759887;
	setAttr ".wl[984].w[2]" 0.65480612305963892;
	setAttr ".wl[984].w[3]" 0.073943580367944683;
	setAttr ".wl[984].w[5]" 0.011332671460313829;
	setAttr -s 5 ".wl[985].w";
	setAttr ".wl[985].w[0]" 0.026218503681122579;
	setAttr ".wl[985].w[1]" 0.23369913341692217;
	setAttr ".wl[985].w[2]" 0.65480610350455937;
	setAttr ".wl[985].w[3]" 0.073943586586301485;
	setAttr ".wl[985].w[5]" 0.011332672811094296;
	setAttr -s 5 ".wl[986].w";
	setAttr ".wl[986].w[0]" 0.026218505956528408;
	setAttr ".wl[986].w[1]" 0.23369914082435947;
	setAttr ".wl[986].w[2]" 0.65480608770698856;
	setAttr ".wl[986].w[3]" 0.073943591609801129;
	setAttr ".wl[986].w[5]" 0.011332673902322368;
	setAttr -s 5 ".wl[987].w";
	setAttr ".wl[987].w[0]" 0.026218506644057053;
	setAttr ".wl[987].w[1]" 0.23369914306256467;
	setAttr ".wl[987].w[2]" 0.65480608293365006;
	setAttr ".wl[987].w[3]" 0.073943593127684115;
	setAttr ".wl[987].w[5]" 0.011332674232044027;
	setAttr -s 5 ".wl[988].w";
	setAttr ".wl[988].w[0]" 0.026218509556249436;
	setAttr ".wl[988].w[1]" 0.23369915254301787;
	setAttr ".wl[988].w[2]" 0.65480606271503239;
	setAttr ".wl[988].w[3]" 0.073943599557041217;
	setAttr ".wl[988].w[5]" 0.011332675628659141;
	setAttr -s 5 ".wl[989].w";
	setAttr ".wl[989].w[0]" 0.026218512803503468;
	setAttr ".wl[989].w[1]" 0.23369916311424094;
	setAttr ".wl[989].w[2]" 0.65480604017016786;
	setAttr ".wl[989].w[3]" 0.073943606726126251;
	setAttr ".wl[989].w[5]" 0.011332677185961546;
	setAttr -s 5 ".wl[990].w";
	setAttr ".wl[990].w[0]" 0.026218510880458006;
	setAttr ".wl[990].w[1]" 0.23369915685389248;
	setAttr ".wl[990].w[2]" 0.65480605352138643;
	setAttr ".wl[990].w[3]" 0.073943602480546405;
	setAttr ".wl[990].w[5]" 0.011332676263716686;
	setAttr -s 5 ".wl[991].w";
	setAttr ".wl[991].w[0]" 0.026218512803503468;
	setAttr ".wl[991].w[1]" 0.23369916311424094;
	setAttr ".wl[991].w[2]" 0.65480604017016786;
	setAttr ".wl[991].w[3]" 0.073943606726126251;
	setAttr ".wl[991].w[5]" 0.011332677185961546;
	setAttr -s 5 ".wl[992].w";
	setAttr ".wl[992].w[0]" 0.026218514584273697;
	setAttr ".wl[992].w[1]" 0.23369916891142128;
	setAttr ".wl[992].w[2]" 0.65480602780673047;
	setAttr ".wl[992].w[3]" 0.073943610657599662;
	setAttr ".wl[992].w[5]" 0.011332678039974748;
	setAttr -s 5 ".wl[993].w";
	setAttr ".wl[993].w[0]" 0.026218519612298347;
	setAttr ".wl[993].w[1]" 0.23369918527982153;
	setAttr ".wl[993].w[2]" 0.65480599289843144;
	setAttr ".wl[993].w[3]" 0.073943621758158065;
	setAttr ".wl[993].w[5]" 0.011332680451290614;
	setAttr -s 5 ".wl[994].w";
	setAttr ".wl[994].w[0]" 0.026218524742505439;
	setAttr ".wl[994].w[1]" 0.2336992019808655;
	setAttr ".wl[994].w[2]" 0.65480595728071078;
	setAttr ".wl[994].w[3]" 0.073943633084307625;
	setAttr ".wl[994].w[5]" 0.011332682911610744;
	setAttr -s 5 ".wl[995].w";
	setAttr ".wl[995].w[0]" 0.026218525279130992;
	setAttr ".wl[995].w[1]" 0.23369920372781344;
	setAttr ".wl[995].w[2]" 0.65480595355505666;
	setAttr ".wl[995].w[3]" 0.073943634269035829;
	setAttr ".wl[995].w[5]" 0.011332683168963064;
	setAttr -s 5 ".wl[996].w";
	setAttr ".wl[996].w[0]" 0.026218528165993765;
	setAttr ".wl[996].w[1]" 0.23369921312579864;
	setAttr ".wl[996].w[2]" 0.65480593351230665;
	setAttr ".wl[996].w[3]" 0.07394364064247004;
	setAttr ".wl[996].w[5]" 0.011332684553430918;
	setAttr -s 5 ".wl[997].w";
	setAttr ".wl[997].w[0]" 0.026218532580541992;
	setAttr ".wl[997].w[1]" 0.23369922749705707;
	setAttr ".wl[997].w[2]" 0.65480590286323048;
	setAttr ".wl[997].w[3]" 0.073943650388631599;
	setAttr ".wl[997].w[5]" 0.011332686670538912;
	setAttr -s 5 ".wl[998].w";
	setAttr ".wl[998].w[0]" 0.026218535492735479;
	setAttr ".wl[998].w[1]" 0.233699236977501;
	setAttr ".wl[998].w[2]" 0.65480588264462003;
	setAttr ".wl[998].w[3]" 0.073943656817988673;
	setAttr ".wl[998].w[5]" 0.011332688067154826;
	setAttr -s 5 ".wl[999].w";
	setAttr ".wl[999].w[0]" 0.026218535569150426;
	setAttr ".wl[999].w[1]" 0.23369923722626454;
	setAttr ".wl[999].w[2]" 0.65480588211409074;
	setAttr ".wl[999].w[3]" 0.073943656986692766;
	setAttr ".wl[999].w[5]" 0.011332688103801546;
	setAttr -s 5 ".wl[1000].w";
	setAttr ".wl[1000].w[0]" 0.040221543454526387;
	setAttr ".wl[1000].w[1]" 0.38674464795608188;
	setAttr ".wl[1000].w[2]" 0.51127996257514763;
	setAttr ".wl[1000].w[3]" 0.052658857304319177;
	setAttr ".wl[1000].w[5]" 0.0090949887099249834;
	setAttr -s 5 ".wl[1001].w";
	setAttr ".wl[1001].w[0]" 0.040221545349221816;
	setAttr ".wl[1001].w[1]" 0.38674464817930315;
	setAttr ".wl[1001].w[2]" 0.5112799576107675;
	setAttr ".wl[1001].w[3]" 0.052658859616702733;
	setAttr ".wl[1001].w[5]" 0.0090949892440048592;
	setAttr -s 5 ".wl[1002].w";
	setAttr ".wl[1002].w[0]" 0.040221546232732087;
	setAttr ".wl[1002].w[1]" 0.38674464828339306;
	setAttr ".wl[1002].w[2]" 0.51127995529584069;
	setAttr ".wl[1002].w[3]" 0.052658860694983996;
	setAttr ".wl[1002].w[5]" 0.0090949894930501905;
	setAttr -s 5 ".wl[1003].w";
	setAttr ".wl[1003].w[0]" 0.040221547228411925;
	setAttr ".wl[1003].w[1]" 0.38674464840069761;
	setAttr ".wl[1003].w[2]" 0.51127995268701365;
	setAttr ".wl[1003].w[3]" 0.052658861910162752;
	setAttr ".wl[1003].w[5]" 0.0090949897737140715;
	setAttr -s 5 ".wl[1004].w";
	setAttr ".wl[1004].w[0]" 0.040221548934181145;
	setAttr ".wl[1004].w[1]" 0.38674464860166086;
	setAttr ".wl[1004].w[2]" 0.51127994821764788;
	setAttr ".wl[1004].w[3]" 0.052658863991971061;
	setAttr ".wl[1004].w[5]" 0.009094990254539137;
	setAttr -s 5 ".wl[1005].w";
	setAttr ".wl[1005].w[0]" 0.040221552455764809;
	setAttr ".wl[1005].w[1]" 0.38674464901655137;
	setAttr ".wl[1005].w[2]" 0.51127993899058233;
	setAttr ".wl[1005].w[3]" 0.052658868289892399;
	setAttr ".wl[1005].w[5]" 0.0090949912472090087;
	setAttr -s 5 ".wl[1006].w";
	setAttr ".wl[1006].w[0]" 0.040221555300676261;
	setAttr ".wl[1006].w[1]" 0.38674464935171987;
	setAttr ".wl[1006].w[2]" 0.51127993153649809;
	setAttr ".wl[1006].w[3]" 0.052658871761968269;
	setAttr ".wl[1006].w[5]" 0.0090949920491374195;
	setAttr -s 5 ".wl[1007].w";
	setAttr ".wl[1007].w[0]" 0.040221556160284715;
	setAttr ".wl[1007].w[1]" 0.38674464945299353;
	setAttr ".wl[1007].w[2]" 0.51127992928419796;
	setAttr ".wl[1007].w[3]" 0.052658872811078485;
	setAttr ".wl[1007].w[5]" 0.0090949922914452946;
	setAttr -s 5 ".wl[1008].w";
	setAttr ".wl[1008].w[0]" 0.040221559801362487;
	setAttr ".wl[1008].w[1]" 0.38674464988196067;
	setAttr ".wl[1008].w[2]" 0.51127991974404197;
	setAttr ".wl[1008].w[3]" 0.05265887725483652;
	setAttr ".wl[1008].w[5]" 0.0090949933177984447;
	setAttr -s 5 ".wl[1009].w";
	setAttr ".wl[1009].w[0]" 0.040221563861363614;
	setAttr ".wl[1009].w[1]" 0.38674465036028211;
	setAttr ".wl[1009].w[2]" 0.51127990910624577;
	setAttr ".wl[1009].w[3]" 0.052658882209870007;
	setAttr ".wl[1009].w[5]" 0.0090949944622384631;
	setAttr -s 5 ".wl[1010].w";
	setAttr ".wl[1010].w[0]" 0.040221561457003889;
	setAttr ".wl[1010].w[1]" 0.38674465007701714;
	setAttr ".wl[1010].w[2]" 0.51127991540601936;
	setAttr ".wl[1010].w[3]" 0.052658879275466142;
	setAttr ".wl[1010].w[5]" 0.0090949937844934554;
	setAttr -s 5 ".wl[1011].w";
	setAttr ".wl[1011].w[0]" 0.040221563861363614;
	setAttr ".wl[1011].w[1]" 0.38674465036028211;
	setAttr ".wl[1011].w[2]" 0.51127990910624577;
	setAttr ".wl[1011].w[3]" 0.052658882209870007;
	setAttr ".wl[1011].w[5]" 0.0090949944622384631;
	setAttr -s 5 ".wl[1012].w";
	setAttr ".wl[1012].w[0]" 0.040221566087838369;
	setAttr ".wl[1012].w[1]" 0.38674465062258934;
	setAttr ".wl[1012].w[2]" 0.51127990327255757;
	setAttr ".wl[1012].w[3]" 0.052658884927173889;
	setAttr ".wl[1012].w[5]" 0.0090949950898409643;
	setAttr -s 5 ".wl[1013].w";
	setAttr ".wl[1013].w[0]" 0.040221572374314604;
	setAttr ".wl[1013].w[1]" 0.38674465136321634;
	setAttr ".wl[1013].w[2]" 0.51127988680107372;
	setAttr ".wl[1013].w[3]" 0.052658892599511578;
	setAttr ".wl[1013].w[5]" 0.0090949968618837043;
	setAttr -s 5 ".wl[1014].w";
	setAttr ".wl[1014].w[0]" 0.040221578788548262;
	setAttr ".wl[1014].w[1]" 0.38674465211889281;
	setAttr ".wl[1014].w[2]" 0.5112798699948492;
	setAttr ".wl[1014].w[3]" 0.052658900427770799;
	setAttr ".wl[1014].w[5]" 0.0090949986699390296;
	setAttr -s 5 ".wl[1015].w";
	setAttr ".wl[1015].w[0]" 0.040221579459484458;
	setAttr ".wl[1015].w[1]" 0.3867446521979373;
	setAttr ".wl[1015].w[2]" 0.51127986823689875;
	setAttr ".wl[1015].w[3]" 0.052658901246615722;
	setAttr ".wl[1015].w[5]" 0.0090949988590637038;
	setAttr -s 5 ".wl[1016].w";
	setAttr ".wl[1016].w[0]" 0.040221583068892758;
	setAttr ".wl[1016].w[1]" 0.38674465262316943;
	setAttr ".wl[1016].w[2]" 0.51127985877972537;
	setAttr ".wl[1016].w[3]" 0.052658905651722362;
	setAttr ".wl[1016].w[5]" 0.0090949998764900501;
	setAttr -s 5 ".wl[1017].w";
	setAttr ".wl[1017].w[0]" 0.040221588588346957;
	setAttr ".wl[1017].w[1]" 0.38674465327342711;
	setAttr ".wl[1017].w[2]" 0.5112798443179557;
	setAttr ".wl[1017].w[3]" 0.052658912387946767;
	setAttr ".wl[1017].w[5]" 0.0090950014323235556;
	setAttr -s 5 ".wl[1018].w";
	setAttr ".wl[1018].w[0]" 0.040221592229425895;
	setAttr ".wl[1018].w[1]" 0.38674465370238892;
	setAttr ".wl[1018].w[2]" 0.51127983477780203;
	setAttr ".wl[1018].w[3]" 0.052658916831705753;
	setAttr ".wl[1018].w[5]" 0.0090950024586773648;
	setAttr -s 5 ".wl[1019].w";
	setAttr ".wl[1019].w[0]" 0.040221592324966547;
	setAttr ".wl[1019].w[1]" 0.38674465371364469;
	setAttr ".wl[1019].w[2]" 0.51127983452747172;
	setAttr ".wl[1019].w[3]" 0.05265891694830848;
	setAttr ".wl[1019].w[5]" 0.0090950024856085391;
	setAttr -s 5 ".wl[1020].w";
	setAttr ".wl[1020].w[0]" 0.058595352614682981;
	setAttr ".wl[1020].w[1]" 0.56204517548358535;
	setAttr ".wl[1020].w[2]" 0.33686232682910822;
	setAttr ".wl[1020].w[3]" 0.035621763354629528;
	setAttr ".wl[1020].w[5]" 0.0068753817179939697;
	setAttr -s 5 ".wl[1021].w";
	setAttr ".wl[1021].w[0]" 0.058595355193274301;
	setAttr ".wl[1021].w[1]" 0.56204516853437259;
	setAttr ".wl[1021].w[2]" 0.33686232899711466;
	setAttr ".wl[1021].w[3]" 0.035621765133174381;
	setAttr ".wl[1021].w[5]" 0.0068753821420641072;
	setAttr -s 5 ".wl[1022].w";
	setAttr ".wl[1022].w[0]" 0.058595356395690204;
	setAttr ".wl[1022].w[1]" 0.56204516529390425;
	setAttr ".wl[1022].w[2]" 0.33686233000807164;
	setAttr ".wl[1022].w[3]" 0.035621765962522769;
	setAttr ".wl[1022].w[5]" 0.0068753823398111057;
	setAttr -s 5 ".wl[1023].w";
	setAttr ".wl[1023].w[0]" 0.058595357750763577;
	setAttr ".wl[1023].w[1]" 0.56204516164202944;
	setAttr ".wl[1023].w[2]" 0.33686233114737874;
	setAttr ".wl[1023].w[3]" 0.035621766897164404;
	setAttr ".wl[1023].w[5]" 0.0068753825626638636;
	setAttr -s 5 ".wl[1024].w";
	setAttr ".wl[1024].w[0]" 0.058595360072235189;
	setAttr ".wl[1024].w[1]" 0.56204515538574562;
	setAttr ".wl[1024].w[2]" 0.33686233309920571;
	setAttr ".wl[1024].w[3]" 0.035621768498364799;
	setAttr ".wl[1024].w[5]" 0.0068753829444486185;
	setAttr -s 5 ".wl[1025].w";
	setAttr ".wl[1025].w[0]" 0.058595364864944627;
	setAttr ".wl[1025].w[1]" 0.56204514246956461;
	setAttr ".wl[1025].w[2]" 0.33686233712877772;
	setAttr ".wl[1025].w[3]" 0.035621771804064672;
	setAttr ".wl[1025].w[5]" 0.006875383732648426;
	setAttr -s 5 ".wl[1026].w";
	setAttr ".wl[1026].w[0]" 0.058595368736735126;
	setAttr ".wl[1026].w[1]" 0.56204513203522721;
	setAttr ".wl[1026].w[2]" 0.33686234038406748;
	setAttr ".wl[1026].w[3]" 0.035621774474574458;
	setAttr ".wl[1026].w[5]" 0.0068753843693957024;
	setAttr -s 5 ".wl[1027].w";
	setAttr ".wl[1027].w[0]" 0.058595369906621703;
	setAttr ".wl[1027].w[1]" 0.56204512888242497;
	setAttr ".wl[1027].w[2]" 0.33686234136767396;
	setAttr ".wl[1027].w[3]" 0.035621775281486322;
	setAttr ".wl[1027].w[5]" 0.0068753845617930227;
	setAttr -s 5 ".wl[1028].w";
	setAttr ".wl[1028].w[0]" 0.058595374861956893;
	setAttr ".wl[1028].w[1]" 0.56204511552797465;
	setAttr ".wl[1028].w[2]" 0.33686234553397548;
	setAttr ".wl[1028].w[3]" 0.035621778699354976;
	setAttr ".wl[1028].w[5]" 0.0068753853767380396;
	setAttr -s 5 ".wl[1029].w";
	setAttr ".wl[1029].w[0]" 0.058595380387426899;
	setAttr ".wl[1029].w[1]" 0.56204510063703295;
	setAttr ".wl[1029].w[2]" 0.33686235017962812;
	setAttr ".wl[1029].w[3]" 0.035621782510465716;
	setAttr ".wl[1029].w[5]" 0.0068753862854464033;
	setAttr -s 5 ".wl[1030].w";
	setAttr ".wl[1030].w[0]" 0.05859537711520673;
	setAttr ".wl[1030].w[1]" 0.56204510945554775;
	setAttr ".wl[1030].w[2]" 0.33686234742844179;
	setAttr ".wl[1030].w[3]" 0.035621780253500532;
	setAttr ".wl[1030].w[5]" 0.0068753857473032474;
	setAttr -s 5 ".wl[1031].w";
	setAttr ".wl[1031].w[0]" 0.058595380387426899;
	setAttr ".wl[1031].w[1]" 0.56204510063703295;
	setAttr ".wl[1031].w[2]" 0.33686235017962812;
	setAttr ".wl[1031].w[3]" 0.035621782510465716;
	setAttr ".wl[1031].w[5]" 0.0068753862854464033;
	setAttr -s 5 ".wl[1032].w";
	setAttr ".wl[1032].w[0]" 0.058595383417553971;
	setAttr ".wl[1032].w[1]" 0.56204509247095014;
	setAttr ".wl[1032].w[2]" 0.33686235272726972;
	setAttr ".wl[1032].w[3]" 0.035621784600450838;
	setAttr ".wl[1032].w[5]" 0.0068753867837754012;
	setAttr -s 5 ".wl[1033].w";
	setAttr ".wl[1033].w[0]" 0.058595391973151306;
	setAttr ".wl[1033].w[1]" 0.56204506941392729;
	setAttr ".wl[1033].w[2]" 0.33686235992056124;
	setAttr ".wl[1033].w[3]" 0.035621790501547082;
	setAttr ".wl[1033].w[5]" 0.0068753881908129458;
	setAttr -s 5 ".wl[1034].w";
	setAttr ".wl[1034].w[0]" 0.058595400702620155;
	setAttr ".wl[1034].w[1]" 0.56204504588832993;
	setAttr ".wl[1034].w[2]" 0.33686236726003593;
	setAttr ".wl[1034].w[3]" 0.035621796522568826;
	setAttr ".wl[1034].w[5]" 0.0068753896264452212;
	setAttr -s 5 ".wl[1035].w";
	setAttr ".wl[1035].w[0]" 0.058595401615732609;
	setAttr ".wl[1035].w[1]" 0.5620450434275257;
	setAttr ".wl[1035].w[2]" 0.3368623680277531;
	setAttr ".wl[1035].w[3]" 0.035621797152374596;
	setAttr ".wl[1035].w[5]" 0.0068753897766140109;
	setAttr -s 5 ".wl[1036].w";
	setAttr ".wl[1036].w[0]" 0.058595406527966604;
	setAttr ".wl[1036].w[1]" 0.56204503018923702;
	setAttr ".wl[1036].w[2]" 0.33686237215781012;
	setAttr ".wl[1036].w[3]" 0.035621800540515315;
	setAttr ".wl[1036].w[5]" 0.0068753905844709841;
	setAttr -s 5 ".wl[1037].w";
	setAttr ".wl[1037].w[0]" 0.05859541403968261;
	setAttr ".wl[1037].w[1]" 0.56204500994544226;
	setAttr ".wl[1037].w[2]" 0.33686237847343076;
	setAttr ".wl[1037].w[3]" 0.035621805721610347;
	setAttr ".wl[1037].w[5]" 0.0068753918198340746;
	setAttr -s 5 ".wl[1038].w";
	setAttr ".wl[1038].w[0]" 0.058595418995018585;
	setAttr ".wl[1038].w[1]" 0.56204499659099749;
	setAttr ".wl[1038].w[2]" 0.33686238263972407;
	setAttr ".wl[1038].w[3]" 0.035621809139480189;
	setAttr ".wl[1038].w[5]" 0.0068753926347796404;
	setAttr -s 5 ".wl[1039].w";
	setAttr ".wl[1039].w[0]" 0.058595419125044908;
	setAttr ".wl[1039].w[1]" 0.56204499624058157;
	setAttr ".wl[1039].w[2]" 0.33686238274904601;
	setAttr ".wl[1039].w[3]" 0.0356218092291639;
	setAttr ".wl[1039].w[5]" 0.0068753926561635351;
	setAttr -s 5 ".wl[1040].w";
	setAttr ".wl[1040].w[0]" 0.082481841321304608;
	setAttr ".wl[1040].w[1]" 0.68814646515017963;
	setAttr ".wl[1040].w[2]" 0.20112517618400799;
	setAttr ".wl[1040].w[3]" 0.023273745789068927;
	setAttr ".wl[1040].w[5]" 0.0049727715554387332;
	setAttr -s 5 ".wl[1041].w";
	setAttr ".wl[1041].w[0]" 0.082481845130310052;
	setAttr ".wl[1041].w[1]" 0.68814645399568919;
	setAttr ".wl[1041].w[2]" 0.2011251817406508;
	setAttr ".wl[1041].w[3]" 0.023273747224319023;
	setAttr ".wl[1041].w[5]" 0.004972771909030887;
	setAttr -s 5 ".wl[1042].w";
	setAttr ".wl[1042].w[0]" 0.082481846906477044;
	setAttr ".wl[1042].w[1]" 0.68814644879426889;
	setAttr ".wl[1042].w[2]" 0.2011251843317538;
	setAttr ".wl[1042].w[3]" 0.023273747893586588;
	setAttr ".wl[1042].w[5]" 0.0049727720739134885;
	setAttr -s 5 ".wl[1043].w";
	setAttr ".wl[1043].w[0]" 0.082481848908144348;
	setAttr ".wl[1043].w[1]" 0.68814644293248195;
	setAttr ".wl[1043].w[2]" 0.20112518725182049;
	setAttr ".wl[1043].w[3]" 0.023273748647823708;
	setAttr ".wl[1043].w[5]" 0.0049727722597294206;
	setAttr -s 5 ".wl[1044].w";
	setAttr ".wl[1044].w[0]" 0.082481852337341524;
	setAttr ".wl[1044].w[1]" 0.68814643289024213;
	setAttr ".wl[1044].w[2]" 0.2011251922543921;
	setAttr ".wl[1044].w[3]" 0.023273749939960422;
	setAttr ".wl[1044].w[5]" 0.004972772578063782;
	setAttr -s 5 ".wl[1045].w";
	setAttr ".wl[1045].w[0]" 0.082481859416965175;
	setAttr ".wl[1045].w[1]" 0.68814641215790351;
	setAttr ".wl[1045].w[2]" 0.20112520258226785;
	setAttr ".wl[1045].w[3]" 0.02327375260759414;
	setAttr ".wl[1045].w[5]" 0.0049727732352693853;
	setAttr -s 5 ".wl[1046].w";
	setAttr ".wl[1046].w[0]" 0.082481865136239146;
	setAttr ".wl[1046].w[1]" 0.68814639540928413;
	setAttr ".wl[1046].w[2]" 0.20112521092564156;
	setAttr ".wl[1046].w[3]" 0.023273754762642148;
	setAttr ".wl[1046].w[5]" 0.0049727737661929743;
	setAttr -s 5 ".wl[1047].w";
	setAttr ".wl[1047].w[0]" 0.08248186686435488;
	setAttr ".wl[1047].w[1]" 0.68814639034858016;
	setAttr ".wl[1047].w[2]" 0.20112521344664605;
	setAttr ".wl[1047].w[3]" 0.023273755413803898;
	setAttr ".wl[1047].w[5]" 0.0049727739266149876;
	setAttr -s 5 ".wl[1048].w";
	setAttr ".wl[1048].w[0]" 0.082481874184203205;
	setAttr ".wl[1048].w[1]" 0.68814636891275627;
	setAttr ".wl[1048].w[2]" 0.20112522412496395;
	setAttr ".wl[1048].w[3]" 0.023273758171955636;
	setAttr ".wl[1048].w[5]" 0.0049727746061209036;
	setAttr -s 5 ".wl[1049].w";
	setAttr ".wl[1049].w[0]" 0.082481882346234464;
	setAttr ".wl[1049].w[1]" 0.68814634501064098;
	setAttr ".wl[1049].w[2]" 0.20112523603187152;
	setAttr ".wl[1049].w[3]" 0.023273761247445891;
	setAttr ".wl[1049].w[5]" 0.0049727753638072452;
	setAttr -s 5 ".wl[1050].w";
	setAttr ".wl[1050].w[0]" 0.082481877512625201;
	setAttr ".wl[1050].w[1]" 0.68814635916563283;
	setAttr ".wl[1050].w[2]" 0.20112522898052171;
	setAttr ".wl[1050].w[3]" 0.023273759426120075;
	setAttr ".wl[1050].w[5]" 0.0049727749151003411;
	setAttr -s 5 ".wl[1051].w";
	setAttr ".wl[1051].w[0]" 0.082481882346234464;
	setAttr ".wl[1051].w[1]" 0.68814634501064098;
	setAttr ".wl[1051].w[2]" 0.20112523603187152;
	setAttr ".wl[1051].w[3]" 0.023273761247445891;
	setAttr ".wl[1051].w[5]" 0.0049727753638072452;
	setAttr -s 5 ".wl[1052].w";
	setAttr ".wl[1052].w[0]" 0.082481886822232217;
	setAttr ".wl[1052].w[1]" 0.68814633190289742;
	setAttr ".wl[1052].w[2]" 0.20112524256153128;
	setAttr ".wl[1052].w[3]" 0.02327376293402213;
	setAttr ".wl[1052].w[5]" 0.0049727757793168771;
	setAttr -s 5 ".wl[1053].w";
	setAttr ".wl[1053].w[0]" 0.082481899460261174;
	setAttr ".wl[1053].w[1]" 0.68814629489304091;
	setAttr ".wl[1053].w[2]" 0.20112526099809591;
	setAttr ".wl[1053].w[3]" 0.023273767696089045;
	setAttr ".wl[1053].w[5]" 0.004972776952513005;
	setAttr -s 5 ".wl[1054].w";
	setAttr ".wl[1054].w[0]" 0.082481912355126363;
	setAttr ".wl[1054].w[1]" 0.6881462571310536;
	setAttr ".wl[1054].w[2]" 0.20112527980933501;
	setAttr ".wl[1054].w[3]" 0.02327377255493349;
	setAttr ".wl[1054].w[5]" 0.0049727781495515887;
	setAttr -s 5 ".wl[1055].w";
	setAttr ".wl[1055].w[0]" 0.082481913703944074;
	setAttr ".wl[1055].w[1]" 0.68814625318110645;
	setAttr ".wl[1055].w[2]" 0.20112528177701208;
	setAttr ".wl[1055].w[3]" 0.02327377306317421;
	setAttr ".wl[1055].w[5]" 0.0049727782747632085;
	setAttr -s 5 ".wl[1056].w";
	setAttr ".wl[1056].w[0]" 0.082481920960123536;
	setAttr ".wl[1056].w[1]" 0.68814623193173785;
	setAttr ".wl[1056].w[2]" 0.20112529236244334;
	setAttr ".wl[1056].w[3]" 0.023273775797336197;
	setAttr ".wl[1056].w[5]" 0.004972778948359075;
	setAttr -s 5 ".wl[1057].w";
	setAttr ".wl[1057].w[0]" 0.082481932056166038;
	setAttr ".wl[1057].w[1]" 0.6881461994375182;
	setAttr ".wl[1057].w[2]" 0.20112530854952709;
	setAttr ".wl[1057].w[3]" 0.023273779978376628;
	setAttr ".wl[1057].w[5]" 0.0049727799784120459;
	setAttr -s 5 ".wl[1058].w";
	setAttr ".wl[1058].w[0]" 0.082481939376013794;
	setAttr ".wl[1058].w[1]" 0.68814617800170197;
	setAttr ".wl[1058].w[2]" 0.20112531922783644;
	setAttr ".wl[1058].w[3]" 0.023273782736529493;
	setAttr ".wl[1058].w[5]" 0.0049727806579184285;
	setAttr -s 5 ".wl[1059].w";
	setAttr ".wl[1059].w[0]" 0.082481939568084042;
	setAttr ".wl[1059].w[1]" 0.68814617743923345;
	setAttr ".wl[1059].w[2]" 0.20112531950803153;
	setAttr ".wl[1059].w[3]" 0.023273782808902466;
	setAttr ".wl[1059].w[5]" 0.004972780675748442;
	setAttr -s 5 ".wl[1060].w";
	setAttr ".wl[1060].w[0]" 0.12280971945772834;
	setAttr ".wl[1060].w[1]" 0.73366861936783134;
	setAttr ".wl[1060].w[2]" 0.12365538451582982;
	setAttr ".wl[1060].w[3]" 0.016094783515953327;
	setAttr ".wl[1060].w[5]" 0.003771493142657319;
	setAttr -s 5 ".wl[1061].w";
	setAttr ".wl[1061].w[0]" 0.12280972473591491;
	setAttr ".wl[1061].w[1]" 0.73366860738934037;
	setAttr ".wl[1061].w[2]" 0.12365538981290869;
	setAttr ".wl[1061].w[3]" 0.016094784629349761;
	setAttr ".wl[1061].w[5]" 0.0037714934324862594;
	setAttr -s 5 ".wl[1062].w";
	setAttr ".wl[1062].w[0]" 0.1228097271971717;
	setAttr ".wl[1062].w[1]" 0.7336686018036831;
	setAttr ".wl[1062].w[2]" 0.12365539228297508;
	setAttr ".wl[1062].w[3]" 0.016094785148534626;
	setAttr ".wl[1062].w[5]" 0.0037714935676356094;
	setAttr -s 5 ".wl[1063].w";
	setAttr ".wl[1063].w[0]" 0.12280972997090706;
	setAttr ".wl[1063].w[1]" 0.73366859550887642;
	setAttr ".wl[1063].w[2]" 0.12365539506663854;
	setAttr ".wl[1063].w[3]" 0.016094785733634685;
	setAttr ".wl[1063].w[5]" 0.003771493719943383;
	setAttr -s 5 ".wl[1064].w";
	setAttr ".wl[1064].w[0]" 0.12280973472278839;
	setAttr ".wl[1064].w[1]" 0.73366858472480001;
	setAttr ".wl[1064].w[2]" 0.1236553998355283;
	setAttr ".wl[1064].w[3]" 0.016094786736010808;
	setAttr ".wl[1064].w[5]" 0.0037714939808725602;
	setAttr -s 5 ".wl[1065].w";
	setAttr ".wl[1065].w[0]" 0.122809744533111;
	setAttr ".wl[1065].w[1]" 0.73366856246092949;
	setAttr ".wl[1065].w[2]" 0.12365540968096513;
	setAttr ".wl[1065].w[3]" 0.016094788805429871;
	setAttr ".wl[1065].w[5]" 0.0037714945195643917;
	setAttr -s 5 ".wl[1066].w";
	setAttr ".wl[1066].w[0]" 0.1228097524583799;
	setAttr ".wl[1066].w[1]" 0.73366854447506236;
	setAttr ".wl[1066].w[2]" 0.12365541763460092;
	setAttr ".wl[1066].w[3]" 0.016094790477210148;
	setAttr ".wl[1066].w[5]" 0.0037714949547466231;
	setAttr -s 5 ".wl[1067].w";
	setAttr ".wl[1067].w[0]" 0.1228097548530513;
	setAttr ".wl[1067].w[1]" 0.73366853904051565;
	setAttr ".wl[1067].w[2]" 0.12365542003784366;
	setAttr ".wl[1067].w[3]" 0.016094790982349432;
	setAttr ".wl[1067].w[5]" 0.0037714950862397607;
	setAttr -s 5 ".wl[1068].w";
	setAttr ".wl[1068].w[0]" 0.12280976499625559;
	setAttr ".wl[1068].w[1]" 0.73366851602119254;
	setAttr ".wl[1068].w[2]" 0.12365543021735352;
	setAttr ".wl[1068].w[3]" 0.016094793121987954;
	setAttr ".wl[1068].w[5]" 0.0037714956432104946;
	setAttr -s 5 ".wl[1069].w";
	setAttr ".wl[1069].w[0]" 0.12280977630648292;
	setAttr ".wl[1069].w[1]" 0.73366849035338777;
	setAttr ".wl[1069].w[2]" 0.1236554415680637;
	setAttr ".wl[1069].w[3]" 0.016094795507802136;
	setAttr ".wl[1069].w[5]" 0.0037714962642633938;
	setAttr -s 5 ".wl[1070].w";
	setAttr ".wl[1070].w[0]" 0.12280976960849109;
	setAttr ".wl[1070].w[1]" 0.73366850555403229;
	setAttr ".wl[1070].w[2]" 0.1236554348460977;
	setAttr ".wl[1070].w[3]" 0.016094794094907085;
	setAttr ".wl[1070].w[5]" 0.0037714958964717251;
	setAttr -s 5 ".wl[1071].w";
	setAttr ".wl[1071].w[0]" 0.12280977630648292;
	setAttr ".wl[1071].w[1]" 0.73366849035338777;
	setAttr ".wl[1071].w[2]" 0.1236554415680637;
	setAttr ".wl[1071].w[3]" 0.016094795507802136;
	setAttr ".wl[1071].w[5]" 0.0037714962642633938;
	setAttr -s 5 ".wl[1072].w";
	setAttr ".wl[1072].w[0]" 0.12280978250892799;
	setAttr ".wl[1072].w[1]" 0.73366847627735332;
	setAttr ".wl[1072].w[2]" 0.12365544779270932;
	setAttr ".wl[1072].w[3]" 0.016094796816165116;
	setAttr ".wl[1072].w[5]" 0.0037714966048442516;
	setAttr -s 5 ".wl[1073].w";
	setAttr ".wl[1073].w[0]" 0.12280980002159941;
	setAttr ".wl[1073].w[1]" 0.73366843653351599;
	setAttr ".wl[1073].w[2]" 0.12365546536806384;
	setAttr ".wl[1073].w[3]" 0.016094800510342643;
	setAttr ".wl[1073].w[5]" 0.003771497566478146;
	setAttr -s 5 ".wl[1074].w";
	setAttr ".wl[1074].w[0]" 0.12280981789017102;
	setAttr ".wl[1074].w[1]" 0.73366839598198585;
	setAttr ".wl[1074].w[2]" 0.12365548330059256;
	setAttr ".wl[1074].w[3]" 0.016094804279595518;
	setAttr ".wl[1074].w[5]" 0.003771498547654995;
	setAttr -s 5 ".wl[1075].w";
	setAttr ".wl[1075].w[0]" 0.12280981975924408;
	setAttr ".wl[1075].w[1]" 0.73366839174024945;
	setAttr ".wl[1075].w[2]" 0.12365548517635551;
	setAttr ".wl[1075].w[3]" 0.016094804673863702;
	setAttr ".wl[1075].w[5]" 0.003771498650287228;
	setAttr -s 5 ".wl[1076].w";
	setAttr ".wl[1076].w[0]" 0.12280982981421966;
	setAttr ".wl[1076].w[1]" 0.73366836892115339;
	setAttr ".wl[1076].w[2]" 0.12365549526732096;
	setAttr ".wl[1076].w[3]" 0.016094806794892308;
	setAttr ".wl[1076].w[5]" 0.003771499202413685;
	setAttr -s 5 ".wl[1077].w";
	setAttr ".wl[1077].w[0]" 0.12280984519013957;
	setAttr ".wl[1077].w[1]" 0.73366833402652887;
	setAttr ".wl[1077].w[2]" 0.123655510698276;
	setAttr ".wl[1077].w[3]" 0.016094810038338216;
	setAttr ".wl[1077].w[5]" 0.0037715000467174182;
	setAttr -s 5 ".wl[1078].w";
	setAttr ".wl[1078].w[0]" 0.12280985533334032;
	setAttr ".wl[1078].w[1]" 0.73366831100721097;
	setAttr ".wl[1078].w[2]" 0.1236555208777823;
	setAttr ".wl[1078].w[3]" 0.01609481217797781;
	setAttr ".wl[1078].w[5]" 0.0037715006036885546;
	setAttr -s 5 ".wl[1079].w";
	setAttr ".wl[1079].w[0]" 0.12280985559949444;
	setAttr ".wl[1079].w[1]" 0.73366831040319191;
	setAttr ".wl[1079].w[2]" 0.12365552114488906;
	setAttr ".wl[1079].w[3]" 0.016094812234121215;
	setAttr ".wl[1079].w[5]" 0.0037715006183032854;
	setAttr -s 5 ".wl[1080].w";
	setAttr ".wl[1080].w[0]" 0.20208634453869267;
	setAttr ".wl[1080].w[1]" 0.6983665164188505;
	setAttr ".wl[1080].w[2]" 0.084005398762533073;
	setAttr ".wl[1080].w[3]" 0.012386201649532979;
	setAttr ".wl[1080].w[5]" 0.0031555386303907347;
	setAttr -s 5 ".wl[1081].w";
	setAttr ".wl[1081].w[0]" 0.20208635033545364;
	setAttr ".wl[1081].w[1]" 0.69836650561126268;
	setAttr ".wl[1081].w[2]" 0.084005402706465934;
	setAttr ".wl[1081].w[3]" 0.012386202483956228;
	setAttr ".wl[1081].w[5]" 0.0031555388628614631;
	setAttr -s 5 ".wl[1082].w";
	setAttr ".wl[1082].w[0]" 0.20208635303852529;
	setAttr ".wl[1082].w[1]" 0.69836650057160599;
	setAttr ".wl[1082].w[2]" 0.084005404545550499;
	setAttr ".wl[1082].w[3]" 0.012386202873053868;
	setAttr ".wl[1082].w[5]" 0.0031555389712642577;
	setAttr -s 5 ".wl[1083].w";
	setAttr ".wl[1083].w[0]" 0.20208635608477621;
	setAttr ".wl[1083].w[1]" 0.69836649489211966;
	setAttr ".wl[1083].w[2]" 0.084005406618123488;
	setAttr ".wl[1083].w[3]" 0.012386203311550966;
	setAttr ".wl[1083].w[5]" 0.0031555390934297663;
	setAttr -s 5 ".wl[1084].w";
	setAttr ".wl[1084].w[0]" 0.20208636130352281;
	setAttr ".wl[1084].w[1]" 0.69836648516219191;
	setAttr ".wl[1084].w[2]" 0.084005410168793954;
	setAttr ".wl[1084].w[3]" 0.01238620406277121;
	setAttr ".wl[1084].w[5]" 0.0031555393027201022;
	setAttr -s 5 ".wl[1085].w";
	setAttr ".wl[1085].w[0]" 0.20208637207769475;
	setAttr ".wl[1085].w[1]" 0.69836646507462585;
	setAttr ".wl[1085].w[2]" 0.084005417499200971;
	setAttr ".wl[1085].w[3]" 0.012386205613675587;
	setAttr ".wl[1085].w[5]" 0.003155539734802842;
	setAttr -s 5 ".wl[1086].w";
	setAttr ".wl[1086].w[0]" 0.20208638078160907;
	setAttr ".wl[1086].w[1]" 0.69836644884688592;
	setAttr ".wl[1086].w[2]" 0.084005423421070285;
	setAttr ".wl[1086].w[3]" 0.012386206866573778;
	setAttr ".wl[1086].w[5]" 0.0031555400838609148;
	setAttr -s 5 ".wl[1087].w";
	setAttr ".wl[1087].w[0]" 0.20208638341155305;
	setAttr ".wl[1087].w[1]" 0.69836644394356928;
	setAttr ".wl[1087].w[2]" 0.084005425210401538;
	setAttr ".wl[1087].w[3]" 0.012386207245145102;
	setAttr ".wl[1087].w[5]" 0.0031555401893310769;
	setAttr -s 5 ".wl[1088].w";
	setAttr ".wl[1088].w[0]" 0.20208639455131083;
	setAttr ".wl[1088].w[1]" 0.69836642317439646;
	setAttr ".wl[1088].w[2]" 0.084005432789542728;
	setAttr ".wl[1088].w[3]" 0.012386208848674746;
	setAttr ".wl[1088].w[5]" 0.0031555406360752616;
	setAttr -s 5 ".wl[1089].w";
	setAttr ".wl[1089].w[0]" 0.20208640697274943;
	setAttr ".wl[1089].w[1]" 0.69836640001563288;
	setAttr ".wl[1089].w[2]" 0.084005441240699905;
	setAttr ".wl[1089].w[3]" 0.012386210636698184;
	setAttr ".wl[1089].w[5]" 0.0031555411342195209;
	setAttr -s 5 ".wl[1090].w";
	setAttr ".wl[1090].w[0]" 0.20208639961669095;
	setAttr ".wl[1090].w[1]" 0.69836641373040675;
	setAttr ".wl[1090].w[2]" 0.084005436235868397;
	setAttr ".wl[1090].w[3]" 0.012386209577818783;
	setAttr ".wl[1090].w[5]" 0.0031555408392151684;
	setAttr -s 5 ".wl[1091].w";
	setAttr ".wl[1091].w[0]" 0.20208640697274943;
	setAttr ".wl[1091].w[1]" 0.69836640001563288;
	setAttr ".wl[1091].w[2]" 0.084005441240699905;
	setAttr ".wl[1091].w[3]" 0.012386210636698184;
	setAttr ".wl[1091].w[5]" 0.0031555411342195209;
	setAttr -s 5 ".wl[1092].w";
	setAttr ".wl[1092].w[0]" 0.2020864137845742;
	setAttr ".wl[1092].w[1]" 0.69836638731553846;
	setAttr ".wl[1092].w[2]" 0.084005445875252174;
	setAttr ".wl[1092].w[3]" 0.012386211617237106;
	setAttr ".wl[1092].w[5]" 0.0031555414073981794;
	setAttr -s 5 ".wl[1093].w";
	setAttr ".wl[1093].w[0]" 0.20208643301783472;
	setAttr ".wl[1093].w[1]" 0.6983663514566828;
	setAttr ".wl[1093].w[2]" 0.08400545896096151;
	setAttr ".wl[1093].w[3]" 0.012386214385799761;
	setAttr ".wl[1093].w[5]" 0.0031555421787212087;
	setAttr -s 5 ".wl[1094].w";
	setAttr ".wl[1094].w[0]" 0.20208645264196079;
	setAttr ".wl[1094].w[1]" 0.69836631486908762;
	setAttr ".wl[1094].w[2]" 0.084005472312605189;
	setAttr ".wl[1094].w[3]" 0.012386217210626877;
	setAttr ".wl[1094].w[5]" 0.003155542965719575;
	setAttr -s 5 ".wl[1095].w";
	setAttr ".wl[1095].w[0]" 0.20208645469466677;
	setAttr ".wl[1095].w[1]" 0.69836631104198332;
	setAttr ".wl[1095].w[2]" 0.084005473709202444;
	setAttr ".wl[1095].w[3]" 0.012386217506107069;
	setAttr ".wl[1095].w[5]" 0.0031555430480405149;
	setAttr -s 5 ".wl[1096].w";
	setAttr ".wl[1096].w[0]" 0.20208646573752459;
	setAttr ".wl[1096].w[1]" 0.69836629045346688;
	setAttr ".wl[1096].w[2]" 0.084005481222419617;
	setAttr ".wl[1096].w[3]" 0.012386219095689785;
	setAttr ".wl[1096].w[5]" 0.0031555434908991358;
	setAttr -s 5 ".wl[1097].w";
	setAttr ".wl[1097].w[0]" 0.20208648262409831;
	setAttr ".wl[1097].w[1]" 0.69836625896981264;
	setAttr ".wl[1097].w[2]" 0.084005492711520524;
	setAttr ".wl[1097].w[3]" 0.01238622152645643;
	setAttr ".wl[1097].w[5]" 0.0031555441681120787;
	setAttr -s 5 ".wl[1098].w";
	setAttr ".wl[1098].w[0]" 0.20208649376384816;
	setAttr ".wl[1098].w[1]" 0.69836623820064669;
	setAttr ".wl[1098].w[2]" 0.084005500290661436;
	setAttr ".wl[1098].w[3]" 0.012386223129987002;
	setAttr ".wl[1098].w[5]" 0.0031555446148566024;
	setAttr -s 5 ".wl[1099].w";
	setAttr ".wl[1099].w[0]" 0.2020864940561512;
	setAttr ".wl[1099].w[1]" 0.69836623765567118;
	setAttr ".wl[1099].w[2]" 0.084005500489535451;
	setAttr ".wl[1099].w[3]" 0.012386223172063089;
	setAttr ".wl[1099].w[5]" 0.0031555446265790245;
	setAttr -s 5 ".wl[1100].w";
	setAttr ".wl[1100].w[0]" 0.34457847847704359;
	setAttr ".wl[1100].w[1]" 0.58181975038168265;
	setAttr ".wl[1100].w[2]" 0.06071431527980678;
	setAttr ".wl[1100].w[3]" 0.010109469404061246;
	setAttr ".wl[1100].w[5]" 0.0027779864574058099;
	setAttr -s 5 ".wl[1101].w";
	setAttr ".wl[1101].w[0]" 0.34457848131188451;
	setAttr ".wl[1101].w[1]" 0.58181974397777447;
	setAttr ".wl[1101].w[2]" 0.060714318042263897;
	setAttr ".wl[1101].w[3]" 0.010109470025392546;
	setAttr ".wl[1101].w[5]" 0.0027779866426846057;
	setAttr -s 5 ".wl[1102].w";
	setAttr ".wl[1102].w[0]" 0.34457848263379121;
	setAttr ".wl[1102].w[1]" 0.58181974099158584;
	setAttr ".wl[1102].w[2]" 0.060714319330417738;
	setAttr ".wl[1102].w[3]" 0.010109470315123862;
	setAttr ".wl[1102].w[5]" 0.002777986729081455;
	setAttr -s 5 ".wl[1103].w";
	setAttr ".wl[1103].w[0]" 0.34457848412352587;
	setAttr ".wl[1103].w[1]" 0.58181973762627348;
	setAttr ".wl[1103].w[2]" 0.060714320782114313;
	setAttr ".wl[1103].w[3]" 0.010109470641639164;
	setAttr ".wl[1103].w[5]" 0.002777986826447166;
	setAttr -s 5 ".wl[1104].w";
	setAttr ".wl[1104].w[0]" 0.34457848667569513;
	setAttr ".wl[1104].w[1]" 0.58181973186092018;
	setAttr ".wl[1104].w[2]" 0.060714323269117909;
	setAttr ".wl[1104].w[3]" 0.010109471201015541;
	setAttr ".wl[1104].w[5]" 0.0027779869932512253;
	setAttr -s 5 ".wl[1105].w";
	setAttr ".wl[1105].w[0]" 0.3445784919446826;
	setAttr ".wl[1105].w[1]" 0.58181971995827086;
	setAttr ".wl[1105].w[2]" 0.060714328403570397;
	setAttr ".wl[1105].w[3]" 0.010109472355855666;
	setAttr ".wl[1105].w[5]" 0.0027779873376204715;
	setAttr -s 5 ".wl[1106].w";
	setAttr ".wl[1106].w[0]" 0.34457849620123321;
	setAttr ".wl[1106].w[1]" 0.58181971034271629;
	setAttr ".wl[1106].w[2]" 0.060714332551437974;
	setAttr ".wl[1106].w[3]" 0.010109473288793329;
	setAttr ".wl[1106].w[5]" 0.0027779876158191938;
	setAttr -s 5 ".wl[1107].w";
	setAttr ".wl[1107].w[0]" 0.34457849748737746;
	setAttr ".wl[1107].w[1]" 0.58181970743731437;
	setAttr ".wl[1107].w[2]" 0.060714333804743052;
	setAttr ".wl[1107].w[3]" 0.010109473570686494;
	setAttr ".wl[1107].w[5]" 0.0027779876998787435;
	setAttr -s 5 ".wl[1108].w";
	setAttr ".wl[1108].w[0]" 0.3445785029351493;
	setAttr ".wl[1108].w[1]" 0.58181969513078768;
	setAttr ".wl[1108].w[2]" 0.060714339113417247;
	setAttr ".wl[1108].w[3]" 0.010109474764712658;
	setAttr ".wl[1108].w[5]" 0.0027779880559331404;
	setAttr -s 5 ".wl[1109].w";
	setAttr ".wl[1109].w[0]" 0.34457850900971226;
	setAttr ".wl[1109].w[1]" 0.58181968140833751;
	setAttr ".wl[1109].w[2]" 0.060714345032879695;
	setAttr ".wl[1109].w[3]" 0.010109476096117282;
	setAttr ".wl[1109].w[5]" 0.0027779884529533171;
	setAttr -s 5 ".wl[1110].w";
	setAttr ".wl[1110].w[0]" 0.34457850541231588;
	setAttr ".wl[1110].w[1]" 0.58181968953486374;
	setAttr ".wl[1110].w[2]" 0.060714341527334605;
	setAttr ".wl[1110].w[3]" 0.010109475307650589;
	setAttr ".wl[1110].w[5]" 0.00277798821783532;
	setAttr -s 5 ".wl[1111].w";
	setAttr ".wl[1111].w[0]" 0.34457850900971226;
	setAttr ".wl[1111].w[1]" 0.58181968140833751;
	setAttr ".wl[1111].w[2]" 0.060714345032879695;
	setAttr ".wl[1111].w[3]" 0.010109476096117282;
	setAttr ".wl[1111].w[5]" 0.0027779884529533171;
	setAttr -s 5 ".wl[1112].w";
	setAttr ".wl[1112].w[0]" 0.34457851234095727;
	setAttr ".wl[1112].w[1]" 0.58181967388304734;
	setAttr ".wl[1112].w[2]" 0.060714348279069311;
	setAttr ".wl[1112].w[3]" 0.010109476826249802;
	setAttr ".wl[1112].w[5]" 0.002777988670676274;
	setAttr -s 5 ".wl[1113].w";
	setAttr ".wl[1113].w[0]" 0.34457852174676246;
	setAttr ".wl[1113].w[1]" 0.58181965263530899;
	setAttr ".wl[1113].w[2]" 0.060714357444721756;
	setAttr ".wl[1113].w[3]" 0.01010947888778721;
	setAttr ".wl[1113].w[5]" 0.002777989285419499;
	setAttr -s 5 ".wl[1114].w";
	setAttr ".wl[1114].w[0]" 0.34457853134371469;
	setAttr ".wl[1114].w[1]" 0.58181963095576517;
	setAttr ".wl[1114].w[2]" 0.06071436679664366;
	setAttr ".wl[1114].w[3]" 0.010109480991220521;
	setAttr ".wl[1114].w[5]" 0.0027779899126559532;
	setAttr -s 5 ".wl[1115].w";
	setAttr ".wl[1115].w[0]" 0.34457853234756669;
	setAttr ".wl[1115].w[1]" 0.58181962868806025;
	setAttr ".wl[1115].w[2]" 0.060714367774865441;
	setAttr ".wl[1115].w[3]" 0.010109481211242069;
	setAttr ".wl[1115].w[5]" 0.002777989978265612;
	setAttr -s 5 ".wl[1116].w";
	setAttr ".wl[1116].w[0]" 0.34457853774794811;
	setAttr ".wl[1116].w[1]" 0.58181961648858016;
	setAttr ".wl[1116].w[2]" 0.060714373037365363;
	setAttr ".wl[1116].w[3]" 0.010109482394883096;
	setAttr ".wl[1116].w[5]" 0.0027779903312232361;
	setAttr -s 5 ".wl[1117].w";
	setAttr ".wl[1117].w[0]" 0.34457854600613003;
	setAttr ".wl[1117].w[1]" 0.5818195978333166;
	setAttr ".wl[1117].w[2]" 0.060714381084702888;
	setAttr ".wl[1117].w[3]" 0.010109484204889671;
	setAttr ".wl[1117].w[5]" 0.0027779908709608895;
	setAttr -s 5 ".wl[1118].w";
	setAttr ".wl[1118].w[0]" 0.34457855145389427;
	setAttr ".wl[1118].w[1]" 0.58181958552679525;
	setAttr ".wl[1118].w[2]" 0.060714386393378249;
	setAttr ".wl[1118].w[3]" 0.01010948539891663;
	setAttr ".wl[1118].w[5]" 0.0027779912270155744;
	setAttr -s 5 ".wl[1119].w";
	setAttr ".wl[1119].w[0]" 0.34457855159684148;
	setAttr ".wl[1119].w[1]" 0.58181958520387667;
	setAttr ".wl[1119].w[2]" 0.060714386532676058;
	setAttr ".wl[1119].w[3]" 0.010109485430247485;
	setAttr ".wl[1119].w[5]" 0.0027779912363583279;
	setAttr -s 5 ".wl[1120].w";
	setAttr ".wl[1120].w[0]" 0.53633244963650983;
	setAttr ".wl[1120].w[1]" 0.41067824803699182;
	setAttr ".wl[1120].w[2]" 0.042681093775904025;
	setAttr ".wl[1120].w[3]" 0.0079643173523617876;
	setAttr ".wl[1120].w[5]" 0.0023438911982325977;
	setAttr -s 5 ".wl[1121].w";
	setAttr ".wl[1121].w[0]" 0.53633244578781136;
	setAttr ".wl[1121].w[1]" 0.41067824913030759;
	setAttr ".wl[1121].w[2]" 0.042681095882226627;
	setAttr ".wl[1121].w[3]" 0.0079643178458883041;
	setAttr ".wl[1121].w[5]" 0.0023438913537660849;
	setAttr -s 5 ".wl[1122].w";
	setAttr ".wl[1122].w[0]" 0.53633244399313562;
	setAttr ".wl[1122].w[1]" 0.41067824964012839;
	setAttr ".wl[1122].w[2]" 0.042681096864420183;
	setAttr ".wl[1122].w[3]" 0.0079643180760233211;
	setAttr ".wl[1122].w[5]" 0.0023438914262924855;
	setAttr -s 5 ".wl[1123].w";
	setAttr ".wl[1123].w[0]" 0.53633244197060959;
	setAttr ".wl[1123].w[1]" 0.41067825021467569;
	setAttr ".wl[1123].w[2]" 0.042681097971312039;
	setAttr ".wl[1123].w[3]" 0.0079643183353760461;
	setAttr ".wl[1123].w[5]" 0.0023438915080267642;
	setAttr -s 5 ".wl[1124].w";
	setAttr ".wl[1124].w[0]" 0.53633243850567758;
	setAttr ".wl[1124].w[1]" 0.410678251198973;
	setAttr ".wl[1124].w[2]" 0.042681099867606431;
	setAttr ".wl[1124].w[3]" 0.0079643187796914674;
	setAttr ".wl[1124].w[5]" 0.0023438916480515173;
	setAttr -s 5 ".wl[1125].w";
	setAttr ".wl[1125].w[0]" 0.53633243135227937;
	setAttr ".wl[1125].w[1]" 0.41067825323106766;
	setAttr ".wl[1125].w[2]" 0.042681103782531843;
	setAttr ".wl[1125].w[3]" 0.0079643196969866846;
	setAttr ".wl[1125].w[5]" 0.00234389193713452;
	setAttr -s 5 ".wl[1126].w";
	setAttr ".wl[1126].w[0]" 0.53633242557340677;
	setAttr ".wl[1126].w[1]" 0.41067825487269483;
	setAttr ".wl[1126].w[2]" 0.042681106945204488;
	setAttr ".wl[1126].w[3]" 0.0079643204380236976;
	setAttr ".wl[1126].w[5]" 0.0023438921706702468;
	setAttr -s 5 ".wl[1127].w";
	setAttr ".wl[1127].w[0]" 0.53633242382728286;
	setAttr ".wl[1127].w[1]" 0.41067825536872316;
	setAttr ".wl[1127].w[2]" 0.042681107900826562;
	setAttr ".wl[1127].w[3]" 0.007964320661932844;
	setAttr ".wl[1127].w[5]" 0.0023438922412345859;
	setAttr -s 5 ".wl[1128].w";
	setAttr ".wl[1128].w[0]" 0.53633241643115714;
	setAttr ".wl[1128].w[1]" 0.41067825746976949;
	setAttr ".wl[1128].w[2]" 0.042681111948592948;
	setAttr ".wl[1128].w[3]" 0.0079643216103537518;
	setAttr ".wl[1128].w[5]" 0.0023438925401267682;
	setAttr -s 5 ".wl[1129].w";
	setAttr ".wl[1129].w[0]" 0.53633240818407246;
	setAttr ".wl[1129].w[1]" 0.41067825981255029;
	setAttr ".wl[1129].w[2]" 0.042681116462074287;
	setAttr ".wl[1129].w[3]" 0.0079643226678950563;
	setAttr ".wl[1129].w[5]" 0.0023438928734079438;
	setAttr -s 5 ".wl[1130].w";
	setAttr ".wl[1130].w[0]" 0.53633241306805068;
	setAttr ".wl[1130].w[1]" 0.41067825842514016;
	setAttr ".wl[1130].w[2]" 0.042681113789160591;
	setAttr ".wl[1130].w[3]" 0.007964322041612043;
	setAttr ".wl[1130].w[5]" 0.0023438926760366088;
	setAttr -s 5 ".wl[1131].w";
	setAttr ".wl[1131].w[0]" 0.53633240818407246;
	setAttr ".wl[1131].w[1]" 0.41067825981255029;
	setAttr ".wl[1131].w[2]" 0.042681116462074287;
	setAttr ".wl[1131].w[3]" 0.0079643226678950563;
	setAttr ".wl[1131].w[5]" 0.0023438928734079438;
	setAttr -s 5 ".wl[1132].w";
	setAttr ".wl[1132].w[0]" 0.53633240366143198;
	setAttr ".wl[1132].w[1]" 0.41067826109731392;
	setAttr ".wl[1132].w[2]" 0.042681118937234266;
	setAttr ".wl[1132].w[3]" 0.0079643232478429533;
	setAttr ".wl[1132].w[5]" 0.0023438930561768992;
	setAttr -s 5 ".wl[1133].w";
	setAttr ".wl[1133].w[0]" 0.53633239089170781;
	setAttr ".wl[1133].w[1]" 0.41067826472485663;
	setAttr ".wl[1133].w[2]" 0.042681125925876022;
	setAttr ".wl[1133].w[3]" 0.0079643248853323838;
	setAttr ".wl[1133].w[5]" 0.002343893572227113;
	setAttr -s 5 ".wl[1134].w";
	setAttr ".wl[1134].w[0]" 0.53633237786247179;
	setAttr ".wl[1134].w[1]" 0.41067826842611826;
	setAttr ".wl[1134].w[2]" 0.042681133056545154;
	setAttr ".wl[1134].w[3]" 0.0079643265560999568;
	setAttr ".wl[1134].w[5]" 0.0023438940987648518;
	setAttr -s 5 ".wl[1135].w";
	setAttr ".wl[1135].w[0]" 0.53633237649959886;
	setAttr ".wl[1135].w[1]" 0.41067826881327424;
	setAttr ".wl[1135].w[2]" 0.04268113380242132;
	setAttr ".wl[1135].w[3]" 0.0079643267308641737;
	setAttr ".wl[1135].w[5]" 0.0023438941538413069;
	setAttr -s 5 ".wl[1136].w";
	setAttr ".wl[1136].w[0]" 0.53633236916780636;
	setAttr ".wl[1136].w[1]" 0.41067827089604231;
	setAttr ".wl[1136].w[2]" 0.042681137814981236;
	setAttr ".wl[1136].w[3]" 0.0079643276710361609;
	setAttr ".wl[1136].w[5]" 0.0023438944501338933;
	setAttr -s 5 ".wl[1137].w";
	setAttr ".wl[1137].w[0]" 0.53633235795613876;
	setAttr ".wl[1137].w[1]" 0.41067827408097862;
	setAttr ".wl[1137].w[2]" 0.042681143950929;
	setAttr ".wl[1137].w[3]" 0.0079643291087334572;
	setAttr ".wl[1137].w[5]" 0.0023438949032202022;
	setAttr -s 5 ".wl[1138].w";
	setAttr ".wl[1138].w[0]" 0.53633235056001538;
	setAttr ".wl[1138].w[1]" 0.41067827618201996;
	setAttr ".wl[1138].w[2]" 0.042681147998697003;
	setAttr ".wl[1138].w[3]" 0.0079643300571550588;
	setAttr ".wl[1138].w[5]" 0.0023438952021126382;
	setAttr -s 5 ".wl[1139].w";
	setAttr ".wl[1139].w[0]" 0.53633235036594373;
	setAttr ".wl[1139].w[1]" 0.41067827623715047;
	setAttr ".wl[1139].w[2]" 0.042681148104909056;
	setAttr ".wl[1139].w[3]" 0.007964330082041322;
	setAttr ".wl[1139].w[5]" 0.0023438952099554752;
	setAttr -s 5 ".wl[1140].w";
	setAttr ".wl[1140].w[0]" 0.70813516846279401;
	setAttr ".wl[1140].w[1]" 0.25546271272684007;
	setAttr ".wl[1140].w[2]" 0.028616259086756468;
	setAttr ".wl[1140].w[3]" 0.0059288601835112654;
	setAttr ".wl[1140].w[5]" 0.0018569995400981266;
	setAttr -s 5 ".wl[1141].w";
	setAttr ".wl[1141].w[0]" 0.70813515984497144;
	setAttr ".wl[1141].w[1]" 0.25546271902147993;
	setAttr ".wl[1141].w[2]" 0.028616260845839073;
	setAttr ".wl[1141].w[3]" 0.0059288606078166765;
	setAttr ".wl[1141].w[5]" 0.0018569996798927012;
	setAttr -s 5 ".wl[1142].w";
	setAttr ".wl[1142].w[0]" 0.70813515582641839;
	setAttr ".wl[1142].w[1]" 0.25546272195671627;
	setAttr ".wl[1142].w[2]" 0.028616261666112097;
	setAttr ".wl[1142].w[3]" 0.0059288608056733859;
	setAttr ".wl[1142].w[5]" 0.0018569997450799311;
	setAttr -s 5 ".wl[1143].w";
	setAttr ".wl[1143].w[0]" 0.70813515129767357;
	setAttr ".wl[1143].w[1]" 0.25546272526460723;
	setAttr ".wl[1143].w[2]" 0.028616262590526177;
	setAttr ".wl[1143].w[3]" 0.0059288610286497827;
	setAttr ".wl[1143].w[5]" 0.0018569998185432664;
	setAttr -s 5 ".wl[1144].w";
	setAttr ".wl[1144].w[0]" 0.70813514353916263;
	setAttr ".wl[1144].w[1]" 0.25546273093158756;
	setAttr ".wl[1144].w[2]" 0.028616264174205014;
	setAttr ".wl[1144].w[3]" 0.0059288614106463569;
	setAttr ".wl[1144].w[5]" 0.0018569999443984817;
	setAttr -s 5 ".wl[1145].w";
	setAttr ".wl[1145].w[0]" 0.70813512752161278;
	setAttr ".wl[1145].w[1]" 0.25546274263114416;
	setAttr ".wl[1145].w[2]" 0.028616267443731386;
	setAttr ".wl[1145].w[3]" 0.0059288621992834708;
	setAttr ".wl[1145].w[5]" 0.001857000204228284;
	setAttr -s 5 ".wl[1146].w";
	setAttr ".wl[1146].w[0]" 0.7081351145818352;
	setAttr ".wl[1146].w[1]" 0.25546275208263047;
	setAttr ".wl[1146].w[2]" 0.028616270085018457;
	setAttr ".wl[1146].w[3]" 0.0059288628363840228;
	setAttr ".wl[1146].w[5]" 0.0018570004141318128;
	setAttr -s 5 ".wl[1147].w";
	setAttr ".wl[1147].w[0]" 0.70813511067199764;
	setAttr ".wl[1147].w[1]" 0.25546275493845833;
	setAttr ".wl[1147].w[2]" 0.028616270883100502;
	setAttr ".wl[1147].w[3]" 0.0059288630288880945;
	setAttr ".wl[1147].w[5]" 0.0018570004775555278;
	setAttr -s 5 ".wl[1148].w";
	setAttr ".wl[1148].w[0]" 0.70813509411094377;
	setAttr ".wl[1148].w[1]" 0.25546276703500059;
	setAttr ".wl[1148].w[2]" 0.028616274263568345;
	setAttr ".wl[1148].w[3]" 0.0059288638442852697;
	setAttr ".wl[1148].w[5]" 0.0018570007462018904;
	setAttr -s 5 ".wl[1149].w";
	setAttr ".wl[1149].w[0]" 0.70813507564446354;
	setAttr ".wl[1149].w[1]" 0.25546278052330607;
	setAttr ".wl[1149].w[2]" 0.028616278032975194;
	setAttr ".wl[1149].w[3]" 0.0059288647534978187;
	setAttr ".wl[1149].w[5]" 0.0018570010457573168;
	setAttr -s 5 ".wl[1150].w";
	setAttr ".wl[1150].w[0]" 0.70813508658043622;
	setAttr ".wl[1150].w[1]" 0.25546277253544181;
	setAttr ".wl[1150].w[2]" 0.028616275800707344;
	setAttr ".wl[1150].w[3]" 0.0059288642150560822;
	setAttr ".wl[1150].w[5]" 0.0018570008683585942;
	setAttr -s 5 ".wl[1151].w";
	setAttr ".wl[1151].w[0]" 0.70813507564446354;
	setAttr ".wl[1151].w[1]" 0.25546278052330607;
	setAttr ".wl[1151].w[2]" 0.028616278032975194;
	setAttr ".wl[1151].w[3]" 0.0059288647534978187;
	setAttr ".wl[1151].w[5]" 0.0018570010457573168;
	setAttr -s 5 ".wl[1152].w";
	setAttr ".wl[1152].w[0]" 0.70813506551758232;
	setAttr ".wl[1152].w[1]" 0.25546278792019284;
	setAttr ".wl[1152].w[2]" 0.028616280100090236;
	setAttr ".wl[1152].w[3]" 0.0059288652521033193;
	setAttr ".wl[1152].w[5]" 0.0018570012100313181;
	setAttr -s 5 ".wl[1153].w";
	setAttr ".wl[1153].w[0]" 0.70813503692422275;
	setAttr ".wl[1153].w[1]" 0.25546280880538225;
	setAttr ".wl[1153].w[2]" 0.028616285936612678;
	setAttr ".wl[1153].w[3]" 0.0059288666599215814;
	setAttr ".wl[1153].w[5]" 0.0018570016738608231;
	setAttr -s 5 ".wl[1154].w";
	setAttr ".wl[1154].w[0]" 0.70813500774977622;
	setAttr ".wl[1154].w[1]" 0.25546283011500825;
	setAttr ".wl[1154].w[2]" 0.028616291891748469;
	setAttr ".wl[1154].w[3]" 0.0059288680963504575;
	setAttr ".wl[1154].w[5]" 0.0018570021471165904;
	setAttr -s 5 ".wl[1155].w";
	setAttr ".wl[1155].w[0]" 0.70813500469809587;
	setAttr ".wl[1155].w[1]" 0.25546283234401929;
	setAttr ".wl[1155].w[2]" 0.028616292514662543;
	setAttr ".wl[1155].w[3]" 0.0059288682466025816;
	setAttr ".wl[1155].w[5]" 0.0018570021966196914;
	setAttr -s 5 ".wl[1156].w";
	setAttr ".wl[1156].w[0]" 0.70813498828109545;
	setAttr ".wl[1156].w[1]" 0.25546284433533917;
	setAttr ".wl[1156].w[2]" 0.028616295865728069;
	setAttr ".wl[1156].w[3]" 0.0059288690549078359;
	setAttr ".wl[1156].w[5]" 0.0018570024629295215;
	setAttr -s 5 ".wl[1157].w";
	setAttr ".wl[1157].w[0]" 0.70813496317646196;
	setAttr ".wl[1157].w[1]" 0.25546286267228663;
	setAttr ".wl[1157].w[2]" 0.028616300990128383;
	setAttr ".wl[1157].w[3]" 0.0059288702909564336;
	setAttr ".wl[1157].w[5]" 0.0018570028701666316;
	setAttr -s 5 ".wl[1158].w";
	setAttr ".wl[1158].w[0]" 0.70813494661541454;
	setAttr ".wl[1158].w[1]" 0.25546287476882024;
	setAttr ".wl[1158].w[2]" 0.028616304370597867;
	setAttr ".wl[1158].w[3]" 0.0059288711063542332;
	setAttr ".wl[1158].w[5]" 0.0018570031388132277;
	setAttr -s 5 ".wl[1159].w";
	setAttr ".wl[1159].w[0]" 0.70813494618085804;
	setAttr ".wl[1159].w[1]" 0.25546287508622934;
	setAttr ".wl[1159].w[2]" 0.028616304459300253;
	setAttr ".wl[1159].w[3]" 0.0059288711277499968;
	setAttr ".wl[1159].w[5]" 0.0018570031458624231;
	setAttr -s 5 ".wl[1160].w";
	setAttr ".wl[1160].w[0]" 0.81443464406763055;
	setAttr ".wl[1160].w[1]" 0.15951916007826641;
	setAttr ".wl[1160].w[2]" 0.019983018461612913;
	setAttr ".wl[1160].w[3]" 0.0045536801708625429;
	setAttr ".wl[1160].w[5]" 0.0015094972216275902;
	setAttr -s 5 ".wl[1161].w";
	setAttr ".wl[1161].w[0]" 0.81443463500612245;
	setAttr ".wl[1161].w[1]" 0.15951916718195705;
	setAttr ".wl[1161].w[2]" 0.01998301992198703;
	setAttr ".wl[1161].w[3]" 0.0045536805408707831;
	setAttr ".wl[1161].w[5]" 0.0015094973490626833;
	setAttr -s 5 ".wl[1162].w";
	setAttr ".wl[1162].w[0]" 0.81443463078067524;
	setAttr ".wl[1162].w[1]" 0.15951917049445971;
	setAttr ".wl[1162].w[2]" 0.019983020602970126;
	setAttr ".wl[1162].w[3]" 0.0045536807134083247;
	setAttr ".wl[1162].w[5]" 0.0015094974084865964;
	setAttr -s 5 ".wl[1163].w";
	setAttr ".wl[1163].w[0]" 0.81443462601876981;
	setAttr ".wl[1163].w[1]" 0.1595191742275141;
	setAttr ".wl[1163].w[2]" 0.019983021370410144;
	setAttr ".wl[1163].w[3]" 0.00455368090785106;
	setAttr ".wl[1163].w[5]" 0.001509497475454911;
	setAttr -s 5 ".wl[1164].w";
	setAttr ".wl[1164].w[0]" 0.81443461786081417;
	setAttr ".wl[1164].w[1]" 0.15951918062287251;
	setAttr ".wl[1164].w[2]" 0.019983022685165712;
	setAttr ".wl[1164].w[3]" 0.0045536812409646098;
	setAttr ".wl[1164].w[5]" 0.0015094975901830494;
	setAttr -s 5 ".wl[1165].w";
	setAttr ".wl[1165].w[0]" 0.81443460101860521;
	setAttr ".wl[1165].w[1]" 0.15951919382617555;
	setAttr ".wl[1165].w[2]" 0.019983025399496375;
	setAttr ".wl[1165].w[3]" 0.0045536819286820596;
	setAttr ".wl[1165].w[5]" 0.0015094978270408501;
	setAttr -s 5 ".wl[1166].w";
	setAttr ".wl[1166].w[0]" 0.81443458741262631;
	setAttr ".wl[1166].w[1]" 0.15951920449246393;
	setAttr ".wl[1166].w[2]" 0.019983027592268592;
	setAttr ".wl[1166].w[3]" 0.0045536824842546553;
	setAttr ".wl[1166].w[5]" 0.0015094980183864447;
	setAttr -s 5 ".wl[1167].w";
	setAttr ".wl[1167].w[0]" 0.81443458330149188;
	setAttr ".wl[1167].w[1]" 0.15951920771535197;
	setAttr ".wl[1167].w[2]" 0.019983028254828939;
	setAttr ".wl[1167].w[3]" 0.0045536826521245253;
	setAttr ".wl[1167].w[5]" 0.0015094980762027606;
	setAttr -s 5 ".wl[1168].w";
	setAttr ".wl[1168].w[0]" 0.81443456588779561;
	setAttr ".wl[1168].w[1]" 0.15951922136666685;
	setAttr ".wl[1168].w[2]" 0.019983031061262264;
	setAttr ".wl[1168].w[3]" 0.0045536833631776349;
	setAttr ".wl[1168].w[5]" 0.0015094983210976363;
	setAttr -s 5 ".wl[1169].w";
	setAttr ".wl[1169].w[0]" 0.81443454647057156;
	setAttr ".wl[1169].w[1]" 0.15951923658862954;
	setAttr ".wl[1169].w[2]" 0.019983034190589239;
	setAttr ".wl[1169].w[3]" 0.0045536841560408483;
	setAttr ".wl[1169].w[5]" 0.0015094985941688554;
	setAttr -s 5 ".wl[1170].w";
	setAttr ".wl[1170].w[0]" 0.81443455796958086;
	setAttr ".wl[1170].w[1]" 0.15951922757408196;
	setAttr ".wl[1170].w[2]" 0.01998303233738094;
	setAttr ".wl[1170].w[3]" 0.0045536836865019631;
	setAttr ".wl[1170].w[5]" 0.0015094984324542573;
	setAttr -s 5 ".wl[1171].w";
	setAttr ".wl[1171].w[0]" 0.81443454647057156;
	setAttr ".wl[1171].w[1]" 0.15951923658862954;
	setAttr ".wl[1171].w[2]" 0.019983034190589239;
	setAttr ".wl[1171].w[3]" 0.0045536841560408483;
	setAttr ".wl[1171].w[5]" 0.0015094985941688554;
	setAttr -s 5 ".wl[1172].w";
	setAttr ".wl[1172].w[0]" 0.81443453582230896;
	setAttr ".wl[1172].w[1]" 0.15951924493624145;
	setAttr ".wl[1172].w[2]" 0.019983035906689168;
	setAttr ".wl[1172].w[3]" 0.0045536845908412194;
	setAttr ".wl[1172].w[5]" 0.0015094987439191118;
	setAttr -s 5 ".wl[1173].w";
	setAttr ".wl[1173].w[0]" 0.81443450575682286;
	setAttr ".wl[1173].w[1]" 0.15951926850581483;
	setAttr ".wl[1173].w[2]" 0.019983040752116633;
	setAttr ".wl[1173].w[3]" 0.0045536858185049999;
	setAttr ".wl[1173].w[5]" 0.0015094991667406619;
	setAttr -s 5 ".wl[1174].w";
	setAttr ".wl[1174].w[0]" 0.81443447508033084;
	setAttr ".wl[1174].w[1]" 0.15951929255437988;
	setAttr ".wl[1174].w[2]" 0.019983045696015916;
	setAttr ".wl[1174].w[3]" 0.0045536870711181928;
	setAttr ".wl[1174].w[5]" 0.0015094995981550848;
	setAttr -s 5 ".wl[1175].w";
	setAttr ".wl[1175].w[0]" 0.81443447187153462;
	setAttr ".wl[1175].w[1]" 0.15951929506988732;
	setAttr ".wl[1175].w[2]" 0.019983046213153485;
	setAttr ".wl[1175].w[3]" 0.0045536872021429819;
	setAttr ".wl[1175].w[5]" 0.0015094996432815323;
	setAttr -s 5 ".wl[1176].w";
	setAttr ".wl[1176].w[0]" 0.81443445460930453;
	setAttr ".wl[1176].w[1]" 0.15951930860245978;
	setAttr ".wl[1176].w[2]" 0.01998304899517752;
	setAttr ".wl[1176].w[3]" 0.004553687907011739;
	setAttr ".wl[1176].w[5]" 0.001509499886046462;
	setAttr -s 5 ".wl[1177].w";
	setAttr ".wl[1177].w[0]" 0.81443442821215695;
	setAttr ".wl[1177].w[1]" 0.15951932929626933;
	setAttr ".wl[1177].w[2]" 0.019983053249407978;
	setAttr ".wl[1177].w[3]" 0.0045536889848867678;
	setAttr ".wl[1177].w[5]" 0.0015095002572790576;
	setAttr -s 5 ".wl[1178].w";
	setAttr ".wl[1178].w[0]" 0.81443441079846157;
	setAttr ".wl[1178].w[1]" 0.15951934294758077;
	setAttr ".wl[1178].w[2]" 0.019983056055843013;
	setAttr ".wl[1178].w[3]" 0.0045536896959404742;
	setAttr ".wl[1178].w[5]" 0.0015095005021741592;
	setAttr -s 5 ".wl[1179].w";
	setAttr ".wl[1179].w[0]" 0.8144344103415323;
	setAttr ".wl[1179].w[1]" 0.1595193433057864;
	setAttr ".wl[1179].w[2]" 0.019983056129482889;
	setAttr ".wl[1179].w[3]" 0.004553689714598276;
	setAttr ".wl[1179].w[5]" 0.0015095005086001216;
	setAttr -s 5 ".wl[1180].w";
	setAttr ".wl[1180].w[0]" 0.86551633666030847;
	setAttr ".wl[1180].w[1]" 0.11307591215788051;
	setAttr ".wl[1180].w[2]" 0.016034287769405003;
	setAttr ".wl[1180].w[3]" 0.0039829859023318981;
	setAttr ".wl[1180].w[5]" 0.0013904775100741179;
	setAttr -s 5 ".wl[1181].w";
	setAttr ".wl[1181].w[0]" 0.8655163289278851;
	setAttr ".wl[1181].w[1]" 0.11307591822823714;
	setAttr ".wl[1181].w[2]" 0.016034288984504212;
	setAttr ".wl[1181].w[3]" 0.0039829862308335406;
	setAttr ".wl[1181].w[5]" 0.0013904776285400139;
	setAttr -s 5 ".wl[1182].w";
	setAttr ".wl[1182].w[0]" 0.8655163253221998;
	setAttr ".wl[1182].w[1]" 0.11307592105888851;
	setAttr ".wl[1182].w[2]" 0.016034289551113811;
	setAttr ".wl[1182].w[3]" 0.0039829863840162502;
	setAttr ".wl[1182].w[5]" 0.0013904776837815229;
	setAttr -s 5 ".wl[1183].w";
	setAttr ".wl[1183].w[0]" 0.86551632125874045;
	setAttr ".wl[1183].w[1]" 0.11307592424891666;
	setAttr ".wl[1183].w[2]" 0.016034290189659624;
	setAttr ".wl[1183].w[3]" 0.0039829865566468892;
	setAttr ".wl[1183].w[5]" 0.001390477746036442;
	setAttr -s 5 ".wl[1184].w";
	setAttr ".wl[1184].w[0]" 0.86551631429734177;
	setAttr ".wl[1184].w[1]" 0.11307592971397842;
	setAttr ".wl[1184].w[2]" 0.016034291283597433;
	setAttr ".wl[1184].w[3]" 0.0039829868523925992;
	setAttr ".wl[1184].w[5]" 0.0013904778526897309;
	setAttr -s 5 ".wl[1185].w";
	setAttr ".wl[1185].w[0]" 0.86551629992544066;
	setAttr ".wl[1185].w[1]" 0.11307594099667187;
	setAttr ".wl[1185].w[2]" 0.016034293542046871;
	setAttr ".wl[1185].w[3]" 0.0039829874629636365;
	setAttr ".wl[1185].w[5]" 0.0013904780728768939;
	setAttr -s 5 ".wl[1186].w";
	setAttr ".wl[1186].w[0]" 0.86551628831509986;
	setAttr ".wl[1186].w[1]" 0.11307595011139601;
	setAttr ".wl[1186].w[2]" 0.016034295366535389;
	setAttr ".wl[1186].w[3]" 0.0039829879562134976;
	setAttr ".wl[1186].w[5]" 0.0013904782507551136;
	setAttr -s 5 ".wl[1187].w";
	setAttr ".wl[1187].w[0]" 0.86551628480696041;
	setAttr ".wl[1187].w[1]" 0.11307595286546886;
	setAttr ".wl[1187].w[2]" 0.016034295917816434;
	setAttr ".wl[1187].w[3]" 0.0039829881052521427;
	setAttr ".wl[1187].w[5]" 0.0013904783045021719;
	setAttr -s 5 ".wl[1188].w";
	setAttr ".wl[1188].w[0]" 0.86551626994739339;
	setAttr ".wl[1188].w[1]" 0.11307596453100519;
	setAttr ".wl[1188].w[2]" 0.01603429825289961;
	setAttr ".wl[1188].w[3]" 0.0039829887365411109;
	setAttr ".wl[1188].w[5]" 0.0013904785321607429;
	setAttr -s 5 ".wl[1189].w";
	setAttr ".wl[1189].w[0]" 0.8655162533781624;
	setAttr ".wl[1189].w[1]" 0.11307597753871668;
	setAttr ".wl[1189].w[2]" 0.01603430085664535;
	setAttr ".wl[1189].w[3]" 0.003982989440462931;
	setAttr ".wl[1189].w[5]" 0.0013904787860125369;
	setAttr -s 5 ".wl[1190].w";
	setAttr ".wl[1190].w[0]" 0.86551626319057129;
	setAttr ".wl[1190].w[1]" 0.11307596983546339;
	setAttr ".wl[1190].w[2]" 0.016034299314689766;
	setAttr ".wl[1190].w[3]" 0.0039829890235957375;
	setAttr ".wl[1190].w[5]" 0.0013904786356798123;
	setAttr -s 5 ".wl[1191].w";
	setAttr ".wl[1191].w[0]" 0.8655162533781624;
	setAttr ".wl[1191].w[1]" 0.11307597753871668;
	setAttr ".wl[1191].w[2]" 0.01603430085664535;
	setAttr ".wl[1191].w[3]" 0.003982989440462931;
	setAttr ".wl[1191].w[5]" 0.0013904787860125369;
	setAttr -s 5 ".wl[1192].w";
	setAttr ".wl[1192].w[0]" 0.86551624429171847;
	setAttr ".wl[1192].w[1]" 0.11307598467204964;
	setAttr ".wl[1192].w[2]" 0.016034302284520397;
	setAttr ".wl[1192].w[3]" 0.003982989826488495;
	setAttr ".wl[1192].w[5]" 0.001390478925223001;
	setAttr -s 5 ".wl[1193].w";
	setAttr ".wl[1193].w[0]" 0.86551621863604244;
	setAttr ".wl[1193].w[1]" 0.11307600481309436;
	setAttr ".wl[1193].w[2]" 0.016034306316141722;
	setAttr ".wl[1193].w[3]" 0.003982990916436069;
	setAttr ".wl[1193].w[5]" 0.0013904793182853311;
	setAttr -s 5 ".wl[1194].w";
	setAttr ".wl[1194].w[0]" 0.86551619245897804;
	setAttr ".wl[1194].w[1]" 0.11307602536345575;
	setAttr ".wl[1194].w[2]" 0.016034310429696264;
	setAttr ".wl[1194].w[3]" 0.0039829920285342968;
	setAttr ".wl[1194].w[5]" 0.0013904797193357488;
	setAttr -s 5 ".wl[1195].w";
	setAttr ".wl[1195].w[0]" 0.86551618972082689;
	setAttr ".wl[1195].w[1]" 0.11307602751304717;
	setAttr ".wl[1195].w[2]" 0.016034310859978827;
	setAttr ".wl[1195].w[3]" 0.0039829921448610601;
	setAttr ".wl[1195].w[5]" 0.0013904797612860874;
	setAttr -s 5 ".wl[1196].w";
	setAttr ".wl[1196].w[0]" 0.86551617499050704;
	setAttr ".wl[1196].w[1]" 0.11307603907711646;
	setAttr ".wl[1196].w[2]" 0.016034313174752464;
	setAttr ".wl[1196].w[3]" 0.003982992770659435;
	setAttr ".wl[1196].w[5]" 0.0013904799869646264;
	setAttr -s 5 ".wl[1197].w";
	setAttr ".wl[1197].w[0]" 0.86551615246511859;
	setAttr ".wl[1197].w[1]" 0.11307605676072065;
	setAttr ".wl[1197].w[2]" 0.016034316714470507;
	setAttr ".wl[1197].w[3]" 0.0039829937276211983;
	setAttr ".wl[1197].w[5]" 0.0013904803320689641;
	setAttr -s 5 ".wl[1198].w";
	setAttr ".wl[1198].w[0]" 0.86551613760554902;
	setAttr ".wl[1198].w[1]" 0.11307606842625735;
	setAttr ".wl[1198].w[2]" 0.016034319049555261;
	setAttr ".wl[1198].w[3]" 0.0039829943589107112;
	setAttr ".wl[1198].w[5]" 0.0013904805597277487;
	setAttr -s 5 ".wl[1199].w";
	setAttr ".wl[1199].w[0]" 0.86551613721563891;
	setAttr ".wl[1199].w[1]" 0.11307606873235702;
	setAttr ".wl[1199].w[2]" 0.016034319110827089;
	setAttr ".wl[1199].w[3]" 0.0039829943754755327;
	setAttr ".wl[1199].w[5]" 0.0013904805657014374;
	setAttr -s 6 ".pm";
	setAttr ".pm[0]" -type "matrix" -1.1920926112907436e-007 0.99999988079071045 1.2246465071688647e-016 0
		 0.99999988079071045 1.1920926135111894e-007 1.4598922293909973e-023 0 -1.5525010974635449e-033 1.224646653158087e-016 -0.99999976158147774 0
		 -8.999998927116394 -1.0728833521600705e-006 -1.3139030064518971e-022 1;
	setAttr ".pm[1]" -type "matrix" -1.1920926112907436e-007 0.99999988079071045 1.2246465071688647e-016 0
		 0.99999988079071045 1.1920926135111894e-007 1.4598922293909973e-023 0 -1.5525010974635449e-033 1.224646653158087e-016 -0.99999976158147774 0
		 -10.199998593330406 -1.215934443044051e-006 -1.4890900461335822e-022 1;
	setAttr ".pm[2]" -type "matrix" -1.1920926112907436e-007 0.99999988079071045 1.2246465071688647e-016 0
		 0.99999988079071045 1.1920926135111894e-007 1.4598922293909973e-023 0 -1.5525010974635449e-033 1.224646653158087e-016 -0.99999976158147774 0
		 -11.399999213218621 -1.3589856476148425e-006 -1.6642772250414395e-022 1;
	setAttr ".pm[3]" -type "matrix" -1.1920926112907436e-007 0.99999988079071045 1.2246465071688647e-016 0
		 0.99999988079071045 1.1920926135111894e-007 1.4598922293909973e-023 0 -1.5525010974635449e-033 1.224646653158087e-016 -0.99999976158147774 0
		 -12.599998879432633 -1.5020367384988228e-006 -1.8394642647231246e-022 1;
	setAttr ".pm[4]" -type "matrix" -1.1920926112907436e-007 0.99999988079071045 1.2246465071688647e-016 0
		 0.99999988079071045 1.1920926135111894e-007 1.4598922293909973e-023 0 -1.5525010974635449e-033 1.224646653158087e-016 -0.99999976158147774 0
		 -14.999998211860657 -1.7881389202667843e-006 -2.1898383440864949e-022 1;
	setAttr ".pm[5]" -type "matrix" -1.1920926112907436e-007 0.99999988079071045 1.2246465071688647e-016 0
		 0.99999988079071045 1.1920926135111894e-007 1.4598922293909973e-023 0 -1.5525010974635449e-033 1.224646653158087e-016 -0.99999976158147774 0
		 -13.799998545646645 -1.6450878293828036e-006 -2.0146513044048101e-022 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 12.121572174091401 0 1;
	setAttr -s 6 ".ma";
	setAttr -s 6 ".dpf[0:5]"  4 4 4 4 4 4;
	setAttr -s 6 ".lw";
	setAttr -s 6 ".lw";
	setAttr ".mmi" yes;
	setAttr ".mi" 5;
	setAttr ".ucm" yes;
	setAttr -s 6 ".ifcl";
	setAttr -s 6 ".ifcl";
createNode tweak -n "tweak1";
	rename -uid "CED25F7E-4B1E-D21D-C305-039DE0080E64";
createNode objectSet -n "skinCluster1Set";
	rename -uid "7B82B534-4F28-031F-02C2-87A0FA2887E7";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster1GroupId";
	rename -uid "837E67F8-4FBA-5403-0DFD-3095374D54B2";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster1GroupParts";
	rename -uid "5A3CF2E7-4ED0-2A34-64AB-28A57A1A763F";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[0:599]";
	setAttr ".irc" -type "componentList" 1 "vtx[600:1199]";
createNode objectSet -n "tweakSet1";
	rename -uid "56AF7D03-4A75-8F0A-62FE-159CC417A504";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId2";
	rename -uid "E970BEA0-4DF8-24D0-209D-F9AE7273B659";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts2";
	rename -uid "A7A52F43-4338-5130-FDF4-5B9A16888FF9";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode dagPose -n "bindPose2";
	rename -uid "A2D149F0-42D1-9912-CCA8-F5B1AF4F25F9";
	setAttr -s 9 ".wm";
	setAttr ".wm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".wm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".wm[2]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr -s 9 ".xm";
	setAttr ".xm[0]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[1]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[2]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[3]" -type "matrix" "xform" 1.0000001192092967 1.0000001192092967 1.0000002384185791 3.1415926535897931
		 0 1.5707964460041719 0 0 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[4]" -type "matrix" "xform" 1.0000001192092967 1.0000001192092967 1.0000002384185791 3.1415926535897931
		 0 1.5707964460041719 0 0 10.199999809265137 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[5]" -type "matrix" "xform" 1.0000001192092967 1.0000001192092967 1.0000002384185791 3.1415926535897931
		 0 1.5707964460041719 0 0 11.40000057220459 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[6]" -type "matrix" "xform" 1.0000001192092967 1.0000001192092967 1.0000002384185791 3.1415926535897931
		 0 1.5707964460041719 0 0 12.600000381469727 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[7]" -type "matrix" "xform" 1.0000001192092967 1.0000001192092967 1.0000002384185791 3.1415926535897931
		 0 1.5707964460041719 0 0 15 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[8]" -type "matrix" "xform" 1.0000001192092967 1.0000001192092967 1.0000002384185791 3.1415926535897931
		 0 1.5707964460041719 0 0 13.800000190734863 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr -s 9 ".m";
	setAttr -s 9 ".p";
	setAttr -s 9 ".g[0:8]" yes yes yes no no no no no no;
	setAttr ".bp" yes;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "0171723A-4D33-1C5D-6AE3-559D26D8F147";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -480.35712376946583 -856.54758501147626 ;
	setAttr ".tgi[0].vh" -type "double2" 1207.7380472468974 2.9761903579272291 ;
	setAttr -s 34 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" 2161.428466796875;
	setAttr ".tgi[0].ni[0].y" -1190;
	setAttr ".tgi[0].ni[0].nvs" 18304;
	setAttr ".tgi[0].ni[1].x" 1157.142822265625;
	setAttr ".tgi[0].ni[1].y" -717.14288330078125;
	setAttr ".tgi[0].ni[1].nvs" 18304;
	setAttr ".tgi[0].ni[2].x" -265.21804809570312;
	setAttr ".tgi[0].ni[2].y" -384.38900756835937;
	setAttr ".tgi[0].ni[2].nvs" 18305;
	setAttr ".tgi[0].ni[3].x" 1151.4285888671875;
	setAttr ".tgi[0].ni[3].y" -327.14285278320312;
	setAttr ".tgi[0].ni[3].nvs" 18304;
	setAttr ".tgi[0].ni[4].x" 2517.142822265625;
	setAttr ".tgi[0].ni[4].y" -1038.5714111328125;
	setAttr ".tgi[0].ni[4].nvs" 18304;
	setAttr ".tgi[0].ni[5].x" 888.5714111328125;
	setAttr ".tgi[0].ni[5].y" -651.4285888671875;
	setAttr ".tgi[0].ni[5].nvs" 18304;
	setAttr ".tgi[0].ni[6].x" 889.66229248046875;
	setAttr ".tgi[0].ni[6].y" -261.42855834960937;
	setAttr ".tgi[0].ni[6].nvs" 18304;
	setAttr ".tgi[0].ni[7].x" 627.14288330078125;
	setAttr ".tgi[0].ni[7].y" -1.4285714626312256;
	setAttr ".tgi[0].ni[7].nvs" 18304;
	setAttr ".tgi[0].ni[8].x" 1444.2857666015625;
	setAttr ".tgi[0].ni[8].y" -391.42855834960937;
	setAttr ".tgi[0].ni[8].nvs" 18304;
	setAttr ".tgi[0].ni[9].x" 627.14288330078125;
	setAttr ".tgi[0].ni[9].y" -261.42855834960937;
	setAttr ".tgi[0].ni[9].nvs" 18304;
	setAttr ".tgi[0].ni[10].x" 1356.2723388671875;
	setAttr ".tgi[0].ni[10].y" -58.864009857177734;
	setAttr ".tgi[0].ni[10].nvs" 18304;
	setAttr ".tgi[0].ni[11].x" 3040;
	setAttr ".tgi[0].ni[11].y" -1038.5714111328125;
	setAttr ".tgi[0].ni[11].nvs" 18304;
	setAttr ".tgi[0].ni[12].x" 888.5714111328125;
	setAttr ".tgi[0].ni[12].y" -391.42855834960937;
	setAttr ".tgi[0].ni[12].nvs" 18304;
	setAttr ".tgi[0].ni[13].x" 627.14288330078125;
	setAttr ".tgi[0].ni[13].y" -391.42855834960937;
	setAttr ".tgi[0].ni[13].nvs" 18304;
	setAttr ".tgi[0].ni[14].x" -256.775146484375;
	setAttr ".tgi[0].ni[14].y" -568.6851806640625;
	setAttr ".tgi[0].ni[14].nvs" 18305;
	setAttr ".tgi[0].ni[15].x" 1444.2857666015625;
	setAttr ".tgi[0].ni[15].y" -651.4285888671875;
	setAttr ".tgi[0].ni[15].nvs" 18304;
	setAttr ".tgi[0].ni[16].x" -255.54222106933594;
	setAttr ".tgi[0].ni[16].y" -331.72366333007812;
	setAttr ".tgi[0].ni[16].nvs" 18304;
	setAttr ".tgi[0].ni[17].x" 1.4285714626312256;
	setAttr ".tgi[0].ni[17].y" -1.4285714626312256;
	setAttr ".tgi[0].ni[17].nvs" 18304;
	setAttr ".tgi[0].ni[18].x" 296.82095336914062;
	setAttr ".tgi[0].ni[18].y" -57.858455657958984;
	setAttr ".tgi[0].ni[18].nvs" 18306;
	setAttr ".tgi[0].ni[19].x" 888.5714111328125;
	setAttr ".tgi[0].ni[19].y" -521.4285888671875;
	setAttr ".tgi[0].ni[19].nvs" 18304;
	setAttr ".tgi[0].ni[20].x" 2517.142822265625;
	setAttr ".tgi[0].ni[20].y" -1168.5714111328125;
	setAttr ".tgi[0].ni[20].nvs" 18304;
	setAttr ".tgi[0].ni[21].x" 1602.857177734375;
	setAttr ".tgi[0].ni[21].y" -1190;
	setAttr ".tgi[0].ni[21].nvs" 18304;
	setAttr ".tgi[0].ni[22].x" 627.14288330078125;
	setAttr ".tgi[0].ni[22].y" -651.4285888671875;
	setAttr ".tgi[0].ni[22].nvs" 18304;
	setAttr ".tgi[0].ni[23].x" -242.59378051757812;
	setAttr ".tgi[0].ni[23].y" -190.66999816894531;
	setAttr ".tgi[0].ni[23].nvs" 18304;
	setAttr ".tgi[0].ni[24].x" 901.66192626953125;
	setAttr ".tgi[0].ni[24].y" -163.06396484375;
	setAttr ".tgi[0].ni[24].nvs" 18304;
	setAttr ".tgi[0].ni[25].x" -238.61994934082031;
	setAttr ".tgi[0].ni[25].y" -69.672004699707031;
	setAttr ".tgi[0].ni[25].nvs" 18304;
	setAttr ".tgi[0].ni[26].x" 1154.2857666015625;
	setAttr ".tgi[0].ni[26].y" -587.14288330078125;
	setAttr ".tgi[0].ni[26].nvs" 18304;
	setAttr ".tgi[0].ni[27].x" 627.14288330078125;
	setAttr ".tgi[0].ni[27].y" -521.4285888671875;
	setAttr ".tgi[0].ni[27].nvs" 18304;
	setAttr ".tgi[0].ni[28].x" 1148.5714111328125;
	setAttr ".tgi[0].ni[28].y" -457.14285278320312;
	setAttr ".tgi[0].ni[28].nvs" 18304;
	setAttr ".tgi[0].ni[29].x" 630.41546630859375;
	setAttr ".tgi[0].ni[29].y" -163.06396484375;
	setAttr ".tgi[0].ni[29].nvs" 18304;
	setAttr ".tgi[0].ni[30].x" 3040;
	setAttr ".tgi[0].ni[30].y" -1168.5714111328125;
	setAttr ".tgi[0].ni[30].nvs" 18304;
	setAttr ".tgi[0].ni[31].x" 888.5714111328125;
	setAttr ".tgi[0].ni[31].y" -1.4285714626312256;
	setAttr ".tgi[0].ni[31].nvs" 18304;
	setAttr ".tgi[0].ni[32].x" 1660;
	setAttr ".tgi[0].ni[32].y" -1010;
	setAttr ".tgi[0].ni[32].nvs" 18304;
	setAttr ".tgi[0].ni[33].x" 1882.857177734375;
	setAttr ".tgi[0].ni[33].y" -1075.7142333984375;
	setAttr ".tgi[0].ni[33].nvs" 18304;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 1;
	setAttr -av ".unw" 1;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr -k on ".mbsof";
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".st";
	setAttr -cb on ".an";
	setAttr -cb on ".pt";
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 4 ".s";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
select -ne :initialParticleSE;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
select -ne :defaultResolution;
	setAttr -av -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av ".w";
	setAttr -av ".h";
	setAttr -av -k on ".pa" 1;
	setAttr -av -k on ".al";
	setAttr -av ".dar";
	setAttr -av -k on ".ldar";
	setAttr -k on ".dpi";
	setAttr -av -k on ".off";
	setAttr -av -k on ".fld";
	setAttr -av -k on ".zsl";
	setAttr -k on ".isu";
	setAttr -k on ".pdu";
select -ne :hardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr ".ctrs" 256;
	setAttr -av ".btrs" 512;
	setAttr -k off ".fbfm";
	setAttr -k off -cb on ".ehql";
	setAttr -k off -cb on ".eams";
	setAttr -k off -cb on ".eeaa";
	setAttr -k off -cb on ".engm";
	setAttr -k off -cb on ".mes";
	setAttr -k off -cb on ".emb";
	setAttr -av -k off -cb on ".mbbf";
	setAttr -k off -cb on ".mbs";
	setAttr -k off -cb on ".trm";
	setAttr -k off -cb on ".tshc";
	setAttr -k off ".enpt";
	setAttr -k off -cb on ".clmt";
	setAttr -k off -cb on ".tcov";
	setAttr -k off -cb on ".lith";
	setAttr -k off -cb on ".sobc";
	setAttr -k off -cb on ".cuth";
	setAttr -k off -cb on ".hgcd";
	setAttr -k off -cb on ".hgci";
	setAttr -k off -cb on ".mgcs";
	setAttr -k off -cb on ".twa";
	setAttr -k off -cb on ".twz";
	setAttr -cb on ".hwcc";
	setAttr -cb on ".hwdp";
	setAttr -cb on ".hwql";
	setAttr -k on ".hwfr";
	setAttr -k on ".soll";
	setAttr -k on ".sosl";
	setAttr -k on ".bswa";
	setAttr -k on ".shml";
	setAttr -k on ".hwel";
connectAttr "cog_To_cog_par_cns.ctx" "M_cog_cmpOut.tx";
connectAttr "cog_To_cog_par_cns.cty" "M_cog_cmpOut.ty";
connectAttr "cog_To_cog_par_cns.ctz" "M_cog_cmpOut.tz";
connectAttr "cog_To_cog_par_cns.crx" "M_cog_cmpOut.rx";
connectAttr "cog_To_cog_par_cns.cry" "M_cog_cmpOut.ry";
connectAttr "cog_To_cog_par_cns.crz" "M_cog_cmpOut.rz";
connectAttr "cog_To_cog_scl_cns.csx" "M_cog_cmpOut.sx";
connectAttr "cog_To_cog_scl_cns.csy" "M_cog_cmpOut.sy";
connectAttr "cog_To_cog_scl_cns.csz" "M_cog_cmpOut.sz";
connectAttr "M_cog_cmpOut.ro" "cog_To_cog_par_cns.cro";
connectAttr "M_cog_cmpOut.pim" "cog_To_cog_par_cns.cpim";
connectAttr "M_cog_cmpOut.rp" "cog_To_cog_par_cns.crp";
connectAttr "M_cog_cmpOut.rpt" "cog_To_cog_par_cns.crt";
connectAttr "M_cog_ctrl.t" "cog_To_cog_par_cns.tg[0].tt";
connectAttr "M_cog_ctrl.rp" "cog_To_cog_par_cns.tg[0].trp";
connectAttr "M_cog_ctrl.rpt" "cog_To_cog_par_cns.tg[0].trt";
connectAttr "M_cog_ctrl.r" "cog_To_cog_par_cns.tg[0].tr";
connectAttr "M_cog_ctrl.ro" "cog_To_cog_par_cns.tg[0].tro";
connectAttr "M_cog_ctrl.s" "cog_To_cog_par_cns.tg[0].ts";
connectAttr "M_cog_ctrl.pm" "cog_To_cog_par_cns.tg[0].tpm";
connectAttr "cog_To_cog_par_cns.w0" "cog_To_cog_par_cns.tg[0].tw";
connectAttr "M_cog_cmpOut.pim" "cog_To_cog_scl_cns.cpim";
connectAttr "M_cog_ctrl.s" "cog_To_cog_scl_cns.tg[0].ts";
connectAttr "M_cog_ctrl.pm" "cog_To_cog_scl_cns.tg[0].tpm";
connectAttr "cog_To_cog_scl_cns.w0" "cog_To_cog_scl_cns.tg[0].tw";
connectAttr "spineBase_To_spineBase_par_cns.ctx" "M_spineBase_cmpOut.tx";
connectAttr "spineBase_To_spineBase_par_cns.cty" "M_spineBase_cmpOut.ty";
connectAttr "spineBase_To_spineBase_par_cns.ctz" "M_spineBase_cmpOut.tz";
connectAttr "spineBase_To_spineBase_par_cns.crx" "M_spineBase_cmpOut.rx";
connectAttr "spineBase_To_spineBase_par_cns.cry" "M_spineBase_cmpOut.ry";
connectAttr "spineBase_To_spineBase_par_cns.crz" "M_spineBase_cmpOut.rz";
connectAttr "spineBase_To_spineBase_scl_cns.csx" "M_spineBase_cmpOut.sx";
connectAttr "spineBase_To_spineBase_scl_cns.csy" "M_spineBase_cmpOut.sy";
connectAttr "spineBase_To_spineBase_scl_cns.csz" "M_spineBase_cmpOut.sz";
connectAttr "M_spineBase_cmpOut.ro" "spineBase_To_spineBase_par_cns.cro";
connectAttr "M_spineBase_cmpOut.pim" "spineBase_To_spineBase_par_cns.cpim";
connectAttr "M_spineBase_cmpOut.rp" "spineBase_To_spineBase_par_cns.crp";
connectAttr "M_spineBase_cmpOut.rpt" "spineBase_To_spineBase_par_cns.crt";
connectAttr "M_spine01_cmpOut.t" "spineBase_To_spineBase_par_cns.tg[0].tt";
connectAttr "M_spine01_cmpOut.rp" "spineBase_To_spineBase_par_cns.tg[0].trp";
connectAttr "M_spine01_cmpOut.rpt" "spineBase_To_spineBase_par_cns.tg[0].trt";
connectAttr "M_spine01_cmpOut.r" "spineBase_To_spineBase_par_cns.tg[0].tr";
connectAttr "M_spine01_cmpOut.ro" "spineBase_To_spineBase_par_cns.tg[0].tro";
connectAttr "M_spine01_cmpOut.s" "spineBase_To_spineBase_par_cns.tg[0].ts";
connectAttr "M_spine01_cmpOut.pm" "spineBase_To_spineBase_par_cns.tg[0].tpm";
connectAttr "spineBase_To_spineBase_par_cns.w0" "spineBase_To_spineBase_par_cns.tg[0].tw"
		;
connectAttr "M_spineBase_cmpOut.pim" "spineBase_To_spineBase_scl_cns.cpim";
connectAttr "M_spine01_cmpOut.s" "spineBase_To_spineBase_scl_cns.tg[0].ts";
connectAttr "M_spine01_cmpOut.pm" "spineBase_To_spineBase_scl_cns.tg[0].tpm";
connectAttr "spineBase_To_spineBase_scl_cns.w0" "spineBase_To_spineBase_scl_cns.tg[0].tw"
		;
connectAttr "pelvis_To_pelvis_par_cns.ctx" "M_pelvis_cmpOut.tx";
connectAttr "pelvis_To_pelvis_par_cns.cty" "M_pelvis_cmpOut.ty";
connectAttr "pelvis_To_pelvis_par_cns.ctz" "M_pelvis_cmpOut.tz";
connectAttr "pelvis_To_pelvis_par_cns.crx" "M_pelvis_cmpOut.rx";
connectAttr "pelvis_To_pelvis_par_cns.cry" "M_pelvis_cmpOut.ry";
connectAttr "pelvis_To_pelvis_par_cns.crz" "M_pelvis_cmpOut.rz";
connectAttr "pelvis_To_pelvis_scl_cns.csx" "M_pelvis_cmpOut.sx";
connectAttr "pelvis_To_pelvis_scl_cns.csy" "M_pelvis_cmpOut.sy";
connectAttr "pelvis_To_pelvis_scl_cns.csz" "M_pelvis_cmpOut.sz";
connectAttr "M_pelvis_cmpOut.ro" "pelvis_To_pelvis_par_cns.cro";
connectAttr "M_pelvis_cmpOut.pim" "pelvis_To_pelvis_par_cns.cpim";
connectAttr "M_pelvis_cmpOut.rp" "pelvis_To_pelvis_par_cns.crp";
connectAttr "M_pelvis_cmpOut.rpt" "pelvis_To_pelvis_par_cns.crt";
connectAttr "M_pelvis_ctrlSpace.t" "pelvis_To_pelvis_par_cns.tg[0].tt";
connectAttr "M_pelvis_ctrlSpace.rp" "pelvis_To_pelvis_par_cns.tg[0].trp";
connectAttr "M_pelvis_ctrlSpace.rpt" "pelvis_To_pelvis_par_cns.tg[0].trt";
connectAttr "M_pelvis_ctrlSpace.r" "pelvis_To_pelvis_par_cns.tg[0].tr";
connectAttr "M_pelvis_ctrlSpace.ro" "pelvis_To_pelvis_par_cns.tg[0].tro";
connectAttr "M_pelvis_ctrlSpace.s" "pelvis_To_pelvis_par_cns.tg[0].ts";
connectAttr "M_pelvis_ctrlSpace.pm" "pelvis_To_pelvis_par_cns.tg[0].tpm";
connectAttr "pelvis_To_pelvis_par_cns.w0" "pelvis_To_pelvis_par_cns.tg[0].tw";
connectAttr "M_pelvis_cmpOut.pim" "pelvis_To_pelvis_scl_cns.cpim";
connectAttr "M_pelvis_ctrlSpace.s" "pelvis_To_pelvis_scl_cns.tg[0].ts";
connectAttr "M_pelvis_ctrlSpace.pm" "pelvis_To_pelvis_scl_cns.tg[0].tpm";
connectAttr "pelvis_To_pelvis_scl_cns.w0" "pelvis_To_pelvis_scl_cns.tg[0].tw";
connectAttr "spineEnd_To_spineEnd_par_cns.ctx" "M_spineEnd_cmpOut.tx";
connectAttr "spineEnd_To_spineEnd_par_cns.cty" "M_spineEnd_cmpOut.ty";
connectAttr "spineEnd_To_spineEnd_par_cns.ctz" "M_spineEnd_cmpOut.tz";
connectAttr "spineEnd_To_spineEnd_par_cns.crx" "M_spineEnd_cmpOut.rx";
connectAttr "spineEnd_To_spineEnd_par_cns.cry" "M_spineEnd_cmpOut.ry";
connectAttr "spineEnd_To_spineEnd_par_cns.crz" "M_spineEnd_cmpOut.rz";
connectAttr "spineEnd_To_spineEnd_scl_cns.csx" "M_spineEnd_cmpOut.sx";
connectAttr "spineEnd_To_spineEnd_scl_cns.csy" "M_spineEnd_cmpOut.sy";
connectAttr "spineEnd_To_spineEnd_scl_cns.csz" "M_spineEnd_cmpOut.sz";
connectAttr "M_spineEnd_cmpOut.ro" "spineEnd_To_spineEnd_par_cns.cro";
connectAttr "M_spineEnd_cmpOut.pim" "spineEnd_To_spineEnd_par_cns.cpim";
connectAttr "M_spineEnd_cmpOut.rp" "spineEnd_To_spineEnd_par_cns.crp";
connectAttr "M_spineEnd_cmpOut.rpt" "spineEnd_To_spineEnd_par_cns.crt";
connectAttr "M_spine06_cmpOut.t" "spineEnd_To_spineEnd_par_cns.tg[0].tt";
connectAttr "M_spine06_cmpOut.rp" "spineEnd_To_spineEnd_par_cns.tg[0].trp";
connectAttr "M_spine06_cmpOut.rpt" "spineEnd_To_spineEnd_par_cns.tg[0].trt";
connectAttr "M_spine06_cmpOut.r" "spineEnd_To_spineEnd_par_cns.tg[0].tr";
connectAttr "M_spine06_cmpOut.ro" "spineEnd_To_spineEnd_par_cns.tg[0].tro";
connectAttr "M_spine06_cmpOut.s" "spineEnd_To_spineEnd_par_cns.tg[0].ts";
connectAttr "M_spine06_cmpOut.pm" "spineEnd_To_spineEnd_par_cns.tg[0].tpm";
connectAttr "spineEnd_To_spineEnd_par_cns.w0" "spineEnd_To_spineEnd_par_cns.tg[0].tw"
		;
connectAttr "M_spineEnd_cmpOut.pim" "spineEnd_To_spineEnd_scl_cns.cpim";
connectAttr "M_spine06_cmpOut.s" "spineEnd_To_spineEnd_scl_cns.tg[0].ts";
connectAttr "M_spine06_cmpOut.pm" "spineEnd_To_spineEnd_scl_cns.tg[0].tpm";
connectAttr "spineEnd_To_spineEnd_scl_cns.w0" "spineEnd_To_spineEnd_scl_cns.tg[0].tw"
		;
connectAttr "decomposeMatrix1.ot" "M_spine01_cmpOut.t";
connectAttr "decomposeMatrix1.or" "M_spine01_cmpOut.r";
connectAttr "decomposeMatrix1.os" "M_spine01_cmpOut.s";
connectAttr "decomposeMatrix2.or" "M_spine02_cmpOut.r";
connectAttr "decomposeMatrix2.os" "M_spine02_cmpOut.s";
connectAttr "decomposeMatrix2.ot" "M_spine02_cmpOut.t";
connectAttr "decomposeMatrix3.or" "M_spine03_cmpOut.r";
connectAttr "decomposeMatrix3.os" "M_spine03_cmpOut.s";
connectAttr "decomposeMatrix3.ot" "M_spine03_cmpOut.t";
connectAttr "decomposeMatrix4.or" "M_spine04_cmpOut.r";
connectAttr "decomposeMatrix4.os" "M_spine04_cmpOut.s";
connectAttr "decomposeMatrix4.ot" "M_spine04_cmpOut.t";
connectAttr "decomposeMatrix5.or" "M_spine05_cmpOut.r";
connectAttr "decomposeMatrix5.os" "M_spine05_cmpOut.s";
connectAttr "decomposeMatrix5.ot" "M_spine05_cmpOut.t";
connectAttr "decomposeMatrix6.ot" "M_spine06_cmpOut.t";
connectAttr "decomposeMatrix6.or" "M_spine06_cmpOut.r";
connectAttr "decomposeMatrix6.os" "M_spine06_cmpOut.s";
connectAttr "cog_To_mainSrt_par_cns.ctx" "M_cog_ctrlSpace.tx";
connectAttr "cog_To_mainSrt_par_cns.cty" "M_cog_ctrlSpace.ty";
connectAttr "cog_To_mainSrt_par_cns.ctz" "M_cog_ctrlSpace.tz";
connectAttr "cog_To_mainSrt_par_cns.crx" "M_cog_ctrlSpace.rx";
connectAttr "cog_To_mainSrt_par_cns.cry" "M_cog_ctrlSpace.ry";
connectAttr "cog_To_mainSrt_par_cns.crz" "M_cog_ctrlSpace.rz";
connectAttr "cog_To_mainSrt_scl_cns.csx" "M_cog_ctrlSpace.sx";
connectAttr "cog_To_mainSrt_scl_cns.csy" "M_cog_ctrlSpace.sy";
connectAttr "cog_To_mainSrt_scl_cns.csz" "M_cog_ctrlSpace.sz";
connectAttr "M_cog_ctrlSpace.ro" "cog_To_mainSrt_par_cns.cro";
connectAttr "M_cog_ctrlSpace.pim" "cog_To_mainSrt_par_cns.cpim";
connectAttr "M_cog_ctrlSpace.rp" "cog_To_mainSrt_par_cns.crp";
connectAttr "M_cog_ctrlSpace.rpt" "cog_To_mainSrt_par_cns.crt";
connectAttr "M_mainSrt_cmpIn.t" "cog_To_mainSrt_par_cns.tg[0].tt";
connectAttr "M_mainSrt_cmpIn.rp" "cog_To_mainSrt_par_cns.tg[0].trp";
connectAttr "M_mainSrt_cmpIn.rpt" "cog_To_mainSrt_par_cns.tg[0].trt";
connectAttr "M_mainSrt_cmpIn.r" "cog_To_mainSrt_par_cns.tg[0].tr";
connectAttr "M_mainSrt_cmpIn.ro" "cog_To_mainSrt_par_cns.tg[0].tro";
connectAttr "M_mainSrt_cmpIn.s" "cog_To_mainSrt_par_cns.tg[0].ts";
connectAttr "M_mainSrt_cmpIn.pm" "cog_To_mainSrt_par_cns.tg[0].tpm";
connectAttr "cog_To_mainSrt_par_cns.w0" "cog_To_mainSrt_par_cns.tg[0].tw";
connectAttr "M_cog_ctrlSpace.pim" "cog_To_mainSrt_scl_cns.cpim";
connectAttr "M_mainSrt_cmpIn.s" "cog_To_mainSrt_scl_cns.tg[0].ts";
connectAttr "M_mainSrt_cmpIn.pm" "cog_To_mainSrt_scl_cns.tg[0].tpm";
connectAttr "cog_To_mainSrt_scl_cns.w0" "cog_To_mainSrt_scl_cns.tg[0].tw";
connectAttr "decomposeMatrix7.or" "M_spine01_def.r";
connectAttr "decomposeMatrix7.os" "M_spine01_def.s";
connectAttr "decomposeMatrix7.ot" "M_spine01_def.t";
connectAttr "decomposeMatrix8.or" "M_spine02_def.r";
connectAttr "decomposeMatrix8.os" "M_spine02_def.s";
connectAttr "decomposeMatrix8.ot" "M_spine02_def.t";
connectAttr "decomposeMatrix9.or" "M_spine03_def.r";
connectAttr "decomposeMatrix9.os" "M_spine03_def.s";
connectAttr "decomposeMatrix9.ot" "M_spine03_def.t";
connectAttr "decomposeMatrix10.or" "M_spine04_def.r";
connectAttr "decomposeMatrix10.os" "M_spine04_def.s";
connectAttr "decomposeMatrix10.ot" "M_spine04_def.t";
connectAttr "decomposeMatrix11.or" "M_spine05_def.r";
connectAttr "decomposeMatrix11.os" "M_spine05_def.s";
connectAttr "decomposeMatrix11.ot" "M_spine05_def.t";
connectAttr "decomposeMatrix12.or" "M_spine06_def.r";
connectAttr "decomposeMatrix12.os" "M_spine06_def.s";
connectAttr "decomposeMatrix12.ot" "M_spine06_def.t";
connectAttr "ZSplineSpineCanvasOp.dummyResult" "transform1.t";
connectAttr "skinCluster1GroupId.id" "pPipeShape1.iog.og[2].gid";
connectAttr "skinCluster1Set.mwc" "pPipeShape1.iog.og[2].gco";
connectAttr "groupId2.id" "pPipeShape1.iog.og[3].gid";
connectAttr "tweakSet1.mwc" "pPipeShape1.iog.og[3].gco";
connectAttr "skinCluster1.og[0]" "pPipeShape1.i";
connectAttr "tweak1.vl[0].vt[1]" "pPipeShape1.twl";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "M_pelvis_ctrlSpace.wm" "ZSplineSpineCanvasOp.pelvis";
connectAttr "M_torso_ctrl.wm" "ZSplineSpineCanvasOp.torso";
connectAttr "M_chest_ctrl.wm" "ZSplineSpineCanvasOp.chest";
connectAttr "M_upChest_ctrl.wm" "ZSplineSpineCanvasOp.upChest";
connectAttr "M_neck_ctrlSpace.wm" "ZSplineSpineCanvasOp.neck";
connectAttr "M_inputs_hrc.rigScale" "ZSplineSpineCanvasOp.rigScale";
connectAttr "M_inputs_hrc.drawDebug" "ZSplineSpineCanvasOp.drawDebug";
connectAttr "M_inputs_hrc.numDeformers" "ZSplineSpineCanvasOp.numDeformers";
connectAttr "ZSplineSpineCanvasOp.outputs[0]" "decomposeMatrix1.imat";
connectAttr "ZSplineSpineCanvasOp.outputs[1]" "decomposeMatrix2.imat";
connectAttr "ZSplineSpineCanvasOp.outputs[2]" "decomposeMatrix3.imat";
connectAttr "ZSplineSpineCanvasOp.outputs[3]" "decomposeMatrix4.imat";
connectAttr "ZSplineSpineCanvasOp.outputs[4]" "decomposeMatrix5.imat";
connectAttr "ZSplineSpineCanvasOp.outputs[5]" "decomposeMatrix6.imat";
connectAttr "M_inputs_hrc.drawDebug" "spineDeformerKLOp.drawDebug";
connectAttr "M_inputs_hrc.rigScale" "spineDeformerKLOp.rigScale";
connectAttr "M_spine01_cmpOut.wm" "spineDeformerKLOp.constrainers[0]";
connectAttr "M_spine02_cmpOut.wm" "spineDeformerKLOp.constrainers[1]";
connectAttr "M_spine03_cmpOut.wm" "spineDeformerKLOp.constrainers[2]";
connectAttr "M_spine04_cmpOut.wm" "spineDeformerKLOp.constrainers[3]";
connectAttr "M_spine05_cmpOut.wm" "spineDeformerKLOp.constrainers[4]";
connectAttr "M_spine06_cmpOut.wm" "spineDeformerKLOp.constrainers[5]";
connectAttr "spineDeformerKLOp.constrainees[0]" "decomposeMatrix7.imat";
connectAttr "spineDeformerKLOp.constrainees[1]" "decomposeMatrix8.imat";
connectAttr "spineDeformerKLOp.constrainees[2]" "decomposeMatrix9.imat";
connectAttr "spineDeformerKLOp.constrainees[3]" "decomposeMatrix10.imat";
connectAttr "spineDeformerKLOp.constrainees[4]" "decomposeMatrix11.imat";
connectAttr "spineDeformerKLOp.constrainees[5]" "decomposeMatrix12.imat";
connectAttr ":TurtleDefaultBakeLayer.idx" ":TurtleBakeLayerManager.bli[0]";
connectAttr ":TurtleRenderOptions.msg" ":TurtleDefaultBakeLayer.rset";
connectAttr "skinCluster1GroupParts.og" "skinCluster1.ip[0].ig";
connectAttr "skinCluster1GroupId.id" "skinCluster1.ip[0].gi";
connectAttr "bindPose2.msg" "skinCluster1.bp";
connectAttr "M_spine01_def.wm" "skinCluster1.ma[0]";
connectAttr "M_spine02_def.wm" "skinCluster1.ma[1]";
connectAttr "M_spine03_def.wm" "skinCluster1.ma[2]";
connectAttr "M_spine04_def.wm" "skinCluster1.ma[3]";
connectAttr "M_spine06_def.wm" "skinCluster1.ma[4]";
connectAttr "M_spine05_def.wm" "skinCluster1.ma[5]";
connectAttr "M_spine01_def.liw" "skinCluster1.lw[0]";
connectAttr "M_spine02_def.liw" "skinCluster1.lw[1]";
connectAttr "M_spine03_def.liw" "skinCluster1.lw[2]";
connectAttr "M_spine04_def.liw" "skinCluster1.lw[3]";
connectAttr "M_spine06_def.liw" "skinCluster1.lw[4]";
connectAttr "M_spine05_def.liw" "skinCluster1.lw[5]";
connectAttr "M_spine01_def.obcc" "skinCluster1.ifcl[0]";
connectAttr "M_spine02_def.obcc" "skinCluster1.ifcl[1]";
connectAttr "M_spine03_def.obcc" "skinCluster1.ifcl[2]";
connectAttr "M_spine04_def.obcc" "skinCluster1.ifcl[3]";
connectAttr "M_spine06_def.obcc" "skinCluster1.ifcl[4]";
connectAttr "M_spine05_def.obcc" "skinCluster1.ifcl[5]";
connectAttr "groupParts2.og" "tweak1.ip[0].ig";
connectAttr "groupId2.id" "tweak1.ip[0].gi";
connectAttr "skinCluster1GroupId.msg" "skinCluster1Set.gn" -na;
connectAttr "pPipeShape1.iog.og[2]" "skinCluster1Set.dsm" -na;
connectAttr "skinCluster1.msg" "skinCluster1Set.ub[0]";
connectAttr "tweak1.og[0]" "skinCluster1GroupParts.ig";
connectAttr "skinCluster1GroupId.id" "skinCluster1GroupParts.gi";
connectAttr "groupId2.msg" "tweakSet1.gn" -na;
connectAttr "pPipeShape1.iog.og[3]" "tweakSet1.dsm" -na;
connectAttr "tweak1.msg" "tweakSet1.ub[0]";
connectAttr "pPipeShape1Orig.w" "groupParts2.ig";
connectAttr "groupId2.id" "groupParts2.gi";
connectAttr "MyRig.msg" "bindPose2.m[0]";
connectAttr "MyRig_deformers.msg" "bindPose2.m[1]";
connectAttr "|MyRig|MyRig_deformers|spine_M_cmp.msg" "bindPose2.m[2]";
connectAttr "M_spine01_def.msg" "bindPose2.m[3]";
connectAttr "M_spine02_def.msg" "bindPose2.m[4]";
connectAttr "M_spine03_def.msg" "bindPose2.m[5]";
connectAttr "M_spine04_def.msg" "bindPose2.m[6]";
connectAttr "M_spine06_def.msg" "bindPose2.m[7]";
connectAttr "M_spine05_def.msg" "bindPose2.m[8]";
connectAttr "bindPose2.w" "bindPose2.p[0]";
connectAttr "bindPose2.m[0]" "bindPose2.p[1]";
connectAttr "bindPose2.m[1]" "bindPose2.p[2]";
connectAttr "bindPose2.m[2]" "bindPose2.p[3]";
connectAttr "bindPose2.m[2]" "bindPose2.p[4]";
connectAttr "bindPose2.m[2]" "bindPose2.p[5]";
connectAttr "bindPose2.m[2]" "bindPose2.p[6]";
connectAttr "bindPose2.m[2]" "bindPose2.p[7]";
connectAttr "bindPose2.m[2]" "bindPose2.p[8]";
connectAttr "M_spine01_def.bps" "bindPose2.wm[3]";
connectAttr "M_spine02_def.bps" "bindPose2.wm[4]";
connectAttr "M_spine03_def.bps" "bindPose2.wm[5]";
connectAttr "M_spine04_def.bps" "bindPose2.wm[6]";
connectAttr "M_spine06_def.bps" "bindPose2.wm[7]";
connectAttr "M_spine05_def.bps" "bindPose2.wm[8]";
connectAttr "pPipeShape1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[0].dn";
connectAttr "spineEnd_To_spineEnd_scl_cns.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[1].dn"
		;
connectAttr "M_torso_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[2].dn";
connectAttr "spineBase_To_spineBase_scl_cns.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[3].dn"
		;
connectAttr "skinCluster1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[4].dn";
connectAttr "M_spine06_cmpOut.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[5].dn"
		;
connectAttr "M_spine03_cmpOut.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[6].dn"
		;
connectAttr "decomposeMatrix5.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[7].dn"
		;
connectAttr "M_spineBase_cmpOut.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[8].dn"
		;
connectAttr "decomposeMatrix3.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[9].dn"
		;
connectAttr "transform1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[10].dn";
connectAttr "skinCluster1Set.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[11].dn"
		;
connectAttr "M_spine01_cmpOut.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[12].dn"
		;
connectAttr "decomposeMatrix1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[13].dn"
		;
connectAttr "M_upChest_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[14].dn";
connectAttr "M_spineEnd_cmpOut.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[15].dn"
		;
connectAttr "M_pelvis_ctrlSpace.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[16].dn"
		;
connectAttr "M_inputs_hrc.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[17].dn";
connectAttr "ZSplineSpineCanvasOp.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[18].dn"
		;
connectAttr "M_spine04_cmpOut.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[19].dn"
		;
connectAttr "tweak1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[20].dn";
connectAttr "pPipe1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[21].dn";
connectAttr "decomposeMatrix6.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[22].dn"
		;
connectAttr "M_neck_ctrlSpace.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[23].dn"
		;
connectAttr "M_spine02_cmpOut.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[24].dn"
		;
connectAttr "M_chest_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[25].dn";
connectAttr "spineEnd_To_spineEnd_par_cns.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[26].dn"
		;
connectAttr "decomposeMatrix4.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[27].dn"
		;
connectAttr "spineBase_To_spineBase_par_cns.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[28].dn"
		;
connectAttr "decomposeMatrix2.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[29].dn"
		;
connectAttr "tweakSet1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[30].dn";
connectAttr "M_spine05_cmpOut.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[31].dn"
		;
connectAttr "bindPose2.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[32].dn";
connectAttr "pPipeShape1Orig.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[33].dn"
		;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "pPipeShape1.iog" ":initialShadingGroup.dsm" -na;
// End of ZSplineSpineComponent_compression.ma
