//Maya ASCII 2016 scene
//Name: ZSplineSpineComponent.ma
//Last modified: Thu, Feb 18, 2016 11:28:23 AM
//Codeset: 1252
requires maya "2016";
requires -nodeType "decomposeMatrix" "matrixNodes" "1.0";
requires -nodeType "ilrOptionsNode" -nodeType "ilrUIOptionsNode" -nodeType "ilrBakeLayerManager"
		 -nodeType "ilrBakeLayer" "Turtle" "2016.0.0";
requires "stereoCamera" "10.0";
requires -nodeType "dfgMayaNode" -dataType "FabricSpliceMayaData" "FabricMaya" "2.0.1";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2016";
fileInfo "version" "2016";
fileInfo "cutIdentifier" "201508242200-969261";
fileInfo "osv" "Microsoft Windows 7 Enterprise Edition, 64-bit Windows 7 Service Pack 1 (Build 7601)\n";
createNode transform -s -n "persp";
	rename -uid "8942B32E-4850-22CF-1407-C5ADC6896DB7";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -32.894375979008977 21.588784236297293 26.608870875892208 ;
	setAttr ".r" -type "double3" -17.138352729602861 -44.999999999999986 1.1244958915987363e-015 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "151FDC0E-4F62-590A-ACF7-A39F8E0651C3";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 44.82186966202994;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
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
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "3DE259C4-410E-556A-7242-04964318CCB9";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 100.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "22335FCB-48F6-E5CD-AACE-7797420D7D2E";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 30;
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
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "M_spine02_def" -p "|MyRig|MyRig_deformers|spine_M_cmp";
	rename -uid "2CFA71C4-4FDD-A9C9-4089-F88F92FF071D";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "M_spine03_def" -p "|MyRig|MyRig_deformers|spine_M_cmp";
	rename -uid "BCB0EA5A-4B57-B8C3-642C-EB8ED9FA685A";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "M_spine04_def" -p "|MyRig|MyRig_deformers|spine_M_cmp";
	rename -uid "4E04BA29-4F4C-5FDB-8494-ADA5469857B9";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "M_spine05_def" -p "|MyRig|MyRig_deformers|spine_M_cmp";
	rename -uid "7FA18320-46D7-81D8-EC8C-37B2095672F4";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "M_spine06_def" -p "|MyRig|MyRig_deformers|spine_M_cmp";
	rename -uid "21387B16-496C-14B3-257D-648D22CDFCCF";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "94382988-4786-ACA7-ED94-D2A1709ADBCE";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode displayLayerManager -n "layerManager";
	rename -uid "615D1165-4C3B-D628-7DCE-C1816A21013E";
createNode displayLayer -n "defaultLayer";
	rename -uid "5B9B1C58-4371-D446-6B4D-C18BAFD5AD91";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "2C31B515-4A6F-600D-5B48-48BD2C7D3A94";
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
	setAttr ".cch" no;
	setAttr ".ihi" 2;
	setAttr ".nds" 0;
	setAttr ".fzn" no;
	setAttr ".svd" -type "string" (
		"{\n  \"objectType\" : \"Graph\",\n  \"metadata\" : {\n    \"maya_id\" : \"155\"\n    },\n  \"title\" : \"\",\n  \"ports\" : [\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"pelvis\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Mat44\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"torso\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Mat44\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"chest\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Mat44\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"upChest\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Mat44\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n"
		+ "        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"neck\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Mat44\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"rigScale\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Scalar\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"drawDebug\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Boolean\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"nodePortType\" : \"In\",\n      \"name\" : \"outputs\",\n      \"execPortType\" : \"Out\",\n      \"typeSpec\" : \"Mat44[]\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"numDeformers\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Integer\"\n      }\n    ],\n  \"extDeps\" : {\n    \"Kraken\" : \"*\"\n"
		+ "    },\n  \"nodes\" : [\n    {\n      \"objectType\" : \"Inst\",\n      \"metadata\" : {\n        \"uiGraphPos\" : \"{\\\"x\\\":203.0,\\\"y\\\":62.0}\"\n        },\n      \"name\" : \"ZSplineSpineSolver_1\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"torso\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"chest\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"upChest\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"neck\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"rigScale\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"drawDebug\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"outputs\"\n"
		+ "          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"numDeformers\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"torsoRest\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"chestRest\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"upchestRest\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"neckRest\"\n          }\n        ],\n      \"executable\" : \"OSS.Solvers.ZSplineSpineSolver\",\n      \"presetGUID\" : \"4C4F38C120424D847A26B6AED8C11BF7\"\n      }\n    ],\n  \"connections\" : {\n    \"torso\" : [\n      \"ZSplineSpineSolver_1.torso\"\n      ],\n    \"chest\" : [\n      \"ZSplineSpineSolver_1.chest\"\n      ],\n    \"upChest\" : [\n      \"ZSplineSpineSolver_1.upChest\"\n      ],\n    \"neck\" : [\n      \"ZSplineSpineSolver_1.neck\"\n"
		+ "      ],\n    \"rigScale\" : [\n      \"ZSplineSpineSolver_1.rigScale\"\n      ],\n    \"drawDebug\" : [\n      \"ZSplineSpineSolver_1.drawDebug\"\n      ],\n    \"numDeformers\" : [\n      \"ZSplineSpineSolver_1.numDeformers\"\n      ],\n    \"ZSplineSpineSolver_1.outputs\" : [\n      \"outputs\"\n      ]\n    },\n  \"metadata\" : {\n    \"maya_id\" : \"155\"\n    },\n  \"requiredPresets\" : {\n    \"OSS.Solvers.ZSplineSpineSolver\" : {\n      \"objectType\" : \"Graph\",\n      \"metadata\" : {\n        \"maya_id\" : \"2\",\n        \"uiGraphZoom\" : \"{\\n  \\\"value\\\" : 0.9141361713409424\\n  }\",\n        \"uiGraphPan\" : \"{\\n  \\\"x\\\" : 30.85516357421875,\\n  \\\"y\\\" : -188.3853759765625\\n  }\"\n        },\n      \"title\" : \"ZSplineSpineSolver\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {\n            \"uiPersistValue\" : \"true\"\n            },\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"torso\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Mat44\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {\n"
		+ "            \"uiPersistValue\" : \"true\"\n            },\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"chest\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Mat44\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {\n            \"uiPersistValue\" : \"true\"\n            },\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"upChest\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Mat44\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {\n            \"uiPersistValue\" : \"true\"\n            },\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"neck\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Mat44\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {\n            \"uiPersistValue\" : \"true\"\n            },\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"rigScale\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Scalar\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {\n"
		+ "            \"uiPersistValue\" : \"true\"\n            },\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"drawDebug\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Boolean\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"outputs\",\n          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"Mat44[]\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {\n            \"uiPersistValue\" : \"true\"\n            },\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"numDeformers\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Integer\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {},\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"torsoRest\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Xfo\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {},\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"chestRest\",\n          \"execPortType\" : \"In\",\n"
		+ "          \"typeSpec\" : \"Xfo\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {},\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"upchestRest\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Xfo\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {},\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"neckRest\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Xfo\"\n          }\n        ],\n      \"extDeps\" : {\n        \"Curves\" : \"*\"\n        },\n      \"presetGUID\" : \"4C4F38C120424D847A26B6AED8C11BF7\",\n      \"nodes\" : [\n        {\n          \"objectType\" : \"Inst\",\n          \"metadata\" : {\n            \"uiGraphPos\" : \"{\\\"x\\\":79.61830000000001,\\\"y\\\":365.897}\"\n            },\n          \"name\" : \"assemble\",\n          \"ports\" : [\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"In\",\n              \"name\" : \"pelvis\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"In\",\n"
		+ "              \"name\" : \"torso\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"In\",\n              \"name\" : \"chest\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"In\",\n              \"name\" : \"upchest\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"In\",\n              \"name\" : \"neck\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"Out\",\n              \"name\" : \"result\"\n              }\n            ],\n          \"definition\" : {\n            \"objectType\" : \"Func\",\n            \"metadata\" : {\n              \"uiTextColor\" : \"{\\n  \\\"r\\\" : 20,\\n  \\\"g\\\" : 20,\\n  \\\"b\\\" : 20\\n  }\",\n              \"uiNodeColor\" : \"{\\n  \\\"r\\\" : 121,\\n  \\\"g\\\" : 134,\\n  \\\"b\\\" : 143\\n  }\"\n              },\n            \"title\" : \"asseble\",\n            \"ports\" : [\n              {\n                \"objectType\" : \"Port\",\n                \"nodePortType\" : \"Out\",\n"
		+ "                \"name\" : \"pelvis\",\n                \"execPortType\" : \"In\",\n                \"typeSpec\" : \"Mat44\"\n                },\n              {\n                \"objectType\" : \"Port\",\n                \"nodePortType\" : \"Out\",\n                \"name\" : \"torso\",\n                \"execPortType\" : \"In\",\n                \"typeSpec\" : \"Mat44\"\n                },\n              {\n                \"objectType\" : \"Port\",\n                \"nodePortType\" : \"Out\",\n                \"name\" : \"chest\",\n                \"execPortType\" : \"In\",\n                \"typeSpec\" : \"Mat44\"\n                },\n              {\n                \"objectType\" : \"Port\",\n                \"nodePortType\" : \"Out\",\n                \"name\" : \"upchest\",\n                \"execPortType\" : \"In\",\n                \"typeSpec\" : \"Mat44\"\n                },\n              {\n                \"objectType\" : \"Port\",\n                \"nodePortType\" : \"Out\",\n                \"name\" : \"neck\",\n                \"execPortType\" : \"In\",\n                \"typeSpec\" : \"Mat44\"\n                },\n"
		+ "              {\n                \"objectType\" : \"Port\",\n                \"nodePortType\" : \"In\",\n                \"name\" : \"result\",\n                \"execPortType\" : \"Out\",\n                \"typeSpec\" : \"Mat44[]\"\n                }\n              ],\n            \"extDeps\" : {},\n            \"code\" : \"dfgEntry {\n  result.push(pelvis);\n  result.push(torso);\n  result.push(chest);\n  result.push(upchest);\n  result.push(neck);\n}\n\"\n            }\n          },\n        {\n          \"objectType\" : \"Inst\",\n          \"metadata\" : {\n            \"uiGraphPos\" : \"{\\\"x\\\":776.528,\\\"y\\\":244.274}\"\n            },\n          \"name\" : \"GetEmptyDebugShape2\",\n          \"ports\" : [\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"IO\",\n              \"name\" : \"exec\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"IO\",\n              \"name\" : \"this\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"In\",\n              \"name\" : \"name\"\n"
		+ "              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"Out\",\n              \"name\" : \"result\"\n              }\n            ],\n          \"executable\" : \"Fabric.Exts.InlineDrawing.DrawingHandle.GetEmptyDebugShape\",\n          \"presetGUID\" : \"DB3916AA2CE58EEAFAEDB9E2653EF4D6\"\n          },\n        {\n          \"objectType\" : \"User\",\n          \"metadata\" : {\n            \"uiTitle\" : \"Drawing\",\n            \"uiGraphPos\" : \"{\\\"x\\\":753.448,\\\"y\\\":80.90900000000001}\",\n            \"uiNodeColor\" : \"{\\n  \\\"r\\\" : 121,\\n  \\\"g\\\" : 134,\\n  \\\"b\\\" : 143\\n  }\",\n            \"uiTextColor\" : \"{\\n  \\\"r\\\" : 20,\\n  \\\"g\\\" : 20,\\n  \\\"b\\\" : 20\\n  }\",\n            \"uiGraphSize\" : \"{\\\"w\\\":611.199,\\\"h\\\":420.479}\"\n            },\n          \"name\" : \"uiBackDropTheDrivenRig22\",\n          \"ports\" : []\n          },\n        {\n          \"objectType\" : \"Inst\",\n          \"metadata\" : {\n            \"uiGraphPos\" : \"{\\\"x\\\":776.883,\\\"y\\\":405.326}\"\n            },\n          \"name\" : \"EmptyDrawingHandle\",\n          \"ports\" : [\n"
		+ "            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"Out\",\n              \"name\" : \"handle\"\n              }\n            ],\n          \"executable\" : \"Fabric.Exts.InlineDrawing.DrawingHandle.EmptyDrawingHandle\",\n          \"presetGUID\" : \"2440020BA6A1CAB1CEB690A198F99C70\"\n          },\n        {\n          \"objectType\" : \"Inst\",\n          \"metadata\" : {\n            \"uiGraphPos\" : \"{\\\"x\\\":776.9160000000001,\\\"y\\\":136.871}\",\n            \"uiCollapsedState\" : \"0\"\n            },\n          \"name\" : \"CreateSegs\",\n          \"ports\" : [\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"Out\",\n              \"name\" : \"result\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"In\",\n              \"name\" : \"this\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"Out\",\n              \"name\" : \"color\"\n              }\n            ],\n          \"executable\" : \"OSS.Exts.Curves.ZSpline.createSegsOnZSpline\",\n"
		+ "          \"presetGUID\" : \"D8E844DE0169A7D9BB304C9F8DDF30A2\"\n          },\n        {\n          \"objectType\" : \"Inst\",\n          \"metadata\" : {\n            \"uiGraphPos\" : \"{\\\"x\\\":1052.66,\\\"y\\\":161.581}\",\n            \"uiNodeColor\" : \"{\\n  \\\"r\\\" : 121,\\n  \\\"g\\\" : 134,\\n  \\\"b\\\" : 143\\n  }\",\n            \"uiTextColor\" : \"{\\n  \\\"r\\\" : 20,\\n  \\\"g\\\" : 20,\\n  \\\"b\\\" : 20\\n  }\",\n            \"uiCollapsedState\" : \"0\"\n            },\n          \"name\" : \"DrawCurve\",\n          \"ports\" : [\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"In\",\n              \"name\" : \"points\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"In\",\n              \"name\" : \"color\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"Out\",\n              \"name\" : \"result\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"IO\",\n              \"name\" : \"this\"\n              },\n"
		+ "            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"Out\",\n              \"name\" : \"dummyResult\"\n              }\n            ],\n          \"executable\" : \"OSS.Exts.Curves.ZSpline.drawCurve\",\n          \"presetGUID\" : \"B3D1DFFCE15CC7040DCD73D99F2C3098\"\n          },\n        {\n          \"objectType\" : \"Inst\",\n          \"metadata\" : {\n            \"uiGraphPos\" : \"{\\\"x\\\":351.2,\\\"y\\\":436.814}\"\n            },\n          \"name\" : \"buildZSpline\",\n          \"ports\" : [\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"In\",\n              \"name\" : \"mat44s\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"Out\",\n              \"name\" : \"result\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"IO\",\n              \"name\" : \"isSegmentStart\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"IO\",\n              \"name\" : \"clamped\"\n"
		+ "              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"IO\",\n              \"name\" : \"weights\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"IO\",\n              \"name\" : \"resolution\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"IO\",\n              \"name\" : \"order\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"IO\",\n              \"name\" : \"closed\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"IO\",\n              \"name\" : \"defSegs\"\n              }\n            ],\n          \"executable\" : \"OSS.Exts.Curves.ZSpline.ZSpline\",\n          \"presetGUID\" : \"1A4FC39528C5CC9C3EF2B16480BD4E7B\"\n          },\n        {\n          \"objectType\" : \"Inst\",\n          \"metadata\" : {\n            \"uiGraphPos\" : \"{\\\"x\\\":1034.15,\\\"y\\\":321.474}\"\n            },\n          \"name\" : \"DrawAxesInstances\",\n"
		+ "          \"ports\" : [\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"IO\",\n              \"name\" : \"exec\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"IO\",\n              \"name\" : \"this\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"In\",\n              \"defaultValues\" : {\n                \"String\" : \"a\"\n                },\n              \"name\" : \"name\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"In\",\n              \"name\" : \"transforms\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"Out\",\n              \"name\" : \"dummyResult\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"Out\",\n              \"name\" : \"instance\"\n              }\n            ],\n          \"executable\" : \"Fabric.Exts.InlineDrawing.DrawingHandle.DrawAxesInstances\",\n"
		+ "          \"presetGUID\" : \"A2DAC55CB1CE7426981A13F213257B7A\"\n          },\n        {\n          \"objectType\" : \"Inst\",\n          \"metadata\" : {\n            \"uiGraphPos\" : \"{\\\"x\\\":480.688,\\\"y\\\":494.188}\",\n            \"uiNodeColor\" : \"{\\n  \\\"r\\\" : 121,\\n  \\\"g\\\" : 134,\\n  \\\"b\\\" : 143\\n  }\",\n            \"uiTextColor\" : \"{\\n  \\\"r\\\" : 20,\\n  \\\"g\\\" : 20,\\n  \\\"b\\\" : 20\\n  }\",\n            \"uiCollapsedState\" : \"0\"\n            },\n          \"name\" : \"createXfosOnZSpline\",\n          \"ports\" : [\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"In\",\n              \"name\" : \"this\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"Out\",\n              \"name\" : \"result\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"In\",\n              \"defaultValues\" : {\n                \"Float32\" : 0\n                },\n              \"name\" : \"keepCurveLen\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n"
		+ "              \"nodePortType\" : \"In\",\n              \"defaultValues\" : {\n                \"Float32\" : 1\n                },\n              \"name\" : \"keepArcLen\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"Out\",\n              \"name\" : \"medianXfos\"\n              }\n            ],\n          \"executable\" : \"OSS.Exts.Curves.ZSpline.createXfosOnZSplineSegments\",\n          \"presetGUID\" : \"9A8AFEEBF71811F541C71B0877BDF45B\"\n          },\n        {\n          \"objectType\" : \"Inst\",\n          \"metadata\" : {\n            \"uiGraphPos\" : \"{\\\"x\\\":1234.3,\\\"y\\\":324.887}\"\n            },\n          \"name\" : \"Add_1\",\n          \"ports\" : [\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"In\",\n              \"name\" : \"lhs\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"In\",\n              \"name\" : \"rhs\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"Out\",\n"
		+ "              \"name\" : \"result\"\n              }\n            ],\n          \"executable\" : \"Fabric.Core.Math.Add\",\n          \"presetGUID\" : \"8146B3E77857E24CAE33F8B5284585E7\"\n          },\n        {\n          \"objectType\" : \"Inst\",\n          \"metadata\" : {\n            \"uiGraphPos\" : \"{\\\"x\\\":848.804,\\\"y\\\":663.986}\"\n            },\n          \"name\" : \"convertXfoToMat44\",\n          \"ports\" : [\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"In\",\n              \"name\" : \"xfoArray\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"Out\",\n              \"name\" : \"mat44Array\"\n              }\n            ],\n          \"definition\" : {\n            \"objectType\" : \"Func\",\n            \"title\" : \"convertXfoToMat44\",\n            \"ports\" : [\n              {\n                \"objectType\" : \"Port\",\n                \"nodePortType\" : \"Out\",\n                \"name\" : \"xfoArray\",\n                \"execPortType\" : \"In\",\n                \"typeSpec\" : \"Xfo[]\"\n"
		+ "                },\n              {\n                \"objectType\" : \"Port\",\n                \"nodePortType\" : \"In\",\n                \"name\" : \"mat44Array\",\n                \"execPortType\" : \"Out\",\n                \"typeSpec\" : \"Mat44[]\"\n                }\n              ],\n            \"extDeps\" : {},\n            \"code\" : \"dfgEntry {\n  for(UInt32 i=0;i<xfoArray.size();i++)\n  {\n    mat44Array.push(xfoArray[i].toMat44());\n  }\n}\n\"\n            }\n          },\n        {\n          \"objectType\" : \"Inst\",\n          \"metadata\" : {\n            \"uiGraphPos\" : \"{\\\"x\\\":847.92,\\\"y\\\":576.005}\"\n            },\n          \"name\" : \"convertXfoToMat44_2\",\n          \"ports\" : [\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"In\",\n              \"name\" : \"xfoArray\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"Out\",\n              \"name\" : \"mat44Array\"\n              }\n            ],\n          \"definition\" : {\n            \"objectType\" : \"Func\",\n            \"title\" : \"convertXfoToMat44\",\n"
		+ "            \"ports\" : [\n              {\n                \"objectType\" : \"Port\",\n                \"nodePortType\" : \"Out\",\n                \"name\" : \"xfoArray\",\n                \"execPortType\" : \"In\",\n                \"typeSpec\" : \"Xfo[]\"\n                },\n              {\n                \"objectType\" : \"Port\",\n                \"nodePortType\" : \"In\",\n                \"name\" : \"mat44Array\",\n                \"execPortType\" : \"Out\",\n                \"typeSpec\" : \"Mat44[]\"\n                }\n              ],\n            \"extDeps\" : {},\n            \"code\" : \"dfgEntry {\n  for(UInt32 i=0;i<xfoArray.size();i++)\n  {\n    mat44Array.push(xfoArray[i].toMat44());\n  }\n}\n\"\n            }\n          },\n        {\n          \"objectType\" : \"Inst\",\n          \"metadata\" : {\n            \"uiGraphPos\" : \"{\\\"x\\\":172.536,\\\"y\\\":627.624}\"\n            },\n          \"name\" : \"Convert_2\",\n          \"ports\" : [\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"Out\",\n              \"name\" : \"result\"\n              },\n            {\n"
		+ "              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"In\",\n              \"name\" : \"size\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"In\",\n              \"name\" : \"defaultVal\"\n              }\n            ],\n          \"definition\" : {\n            \"objectType\" : \"Func\",\n            \"title\" : \"Convert[]\",\n            \"ports\" : [\n              {\n                \"objectType\" : \"Port\",\n                \"nodePortType\" : \"In\",\n                \"name\" : \"result\",\n                \"execPortType\" : \"Out\",\n                \"typeSpec\" : \"$TYPEOUT$[]\"\n                },\n              {\n                \"objectType\" : \"Port\",\n                \"nodePortType\" : \"Out\",\n                \"name\" : \"size\",\n                \"execPortType\" : \"In\",\n                \"typeSpec\" : \"UInt32\"\n                },\n              {\n                \"objectType\" : \"Port\",\n                \"nodePortType\" : \"Out\",\n                \"name\" : \"defaultVal\",\n                \"execPortType\" : \"In\",\n"
		+ "                \"typeSpec\" : \"$TYPE$\"\n                }\n              ],\n            \"extDeps\" : {},\n            \"code\" : \"dfgEntry {\n  result.resize(size);\n  for(UInt32 i=0;i<size;i++){\n     result[i]=defaultVal;\n}\n}\n\"\n            }\n          },\n        {\n          \"objectType\" : \"Inst\",\n          \"metadata\" : {\n            \"uiGraphPos\" : \"{\\\"x\\\":197.978,\\\"y\\\":538.0}\"\n            },\n          \"name\" : \"Size_1\",\n          \"ports\" : [\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"In\",\n              \"name\" : \"this\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"Out\",\n              \"name\" : \"result\"\n              }\n            ],\n          \"executable\" : \"Fabric.Exts.Geometry.Func.Size\",\n          \"presetGUID\" : \"3426735D9D96DD0F52A2A961A393053A\"\n          },\n        {\n          \"objectType\" : \"Inst\",\n          \"metadata\" : {\n            \"uiGraphPos\" : \"{\\\"x\\\":900.679,\\\"y\\\":751.204}\"\n            },\n          \"name\" : \"Set_1\",\n"
		+ "          \"ports\" : [\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"IO\",\n              \"name\" : \"this\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"In\",\n              \"name\" : \"index\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"In\",\n              \"name\" : \"value\"\n              }\n            ],\n          \"definition\" : {\n            \"objectType\" : \"Func\",\n            \"metadata\" : {\n              \"uiDocUrl\" : \"http://docs.fabric-engine.com/FabricEngine/2.0.1/HTML/KLExtensionsGuide/Containers/LocalL4UInt8Array.html\",\n              \"uiTooltip\" : \"sets the value stored at an index\\n\\n Supported by LocalL4UInt8Array,LocalL8UInt8Array,LocalL16UInt8Array,LocalL32UInt8Array,LocalL64UInt8Array\"\n              },\n            \"title\" : \"Set\",\n            \"ports\" : [\n              {\n                \"objectType\" : \"Port\",\n                \"nodePortType\" : \"IO\",\n                \"name\" : \"this\",\n"
		+ "                \"execPortType\" : \"IO\",\n                \"typeSpec\" : \"$TYPE$[]\"\n                },\n              {\n                \"objectType\" : \"Port\",\n                \"nodePortType\" : \"Out\",\n                \"name\" : \"index\",\n                \"execPortType\" : \"In\",\n                \"typeSpec\" : \"UInt32\"\n                },\n              {\n                \"objectType\" : \"Port\",\n                \"nodePortType\" : \"Out\",\n                \"name\" : \"value\",\n                \"execPortType\" : \"In\",\n                \"typeSpec\" : \"$TYPE$\"\n                }\n              ],\n            \"extDeps\" : {\n              \"Containers\" : \"*\"\n              },\n            \"origPresetGUID\" : \"BD62AB731FA3A3205CD0C73932780A71\",\n            \"code\" : \"require Containers;\n\ndfgEntry {\n  this[index] =  value;\n}\n\"\n            }\n          },\n        {\n          \"objectType\" : \"Inst\",\n          \"metadata\" : {\n            \"uiGraphPos\" : \"{\\\"x\\\":540.6660000000001,\\\"y\\\":692.199}\"\n            },\n          \"name\" : \"Sub_1\",\n          \"ports\" : [\n            {\n"
		+ "              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"In\",\n              \"name\" : \"lhs\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"In\",\n              \"name\" : \"rhs\"\n              },\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"Out\",\n              \"name\" : \"result\"\n              }\n            ],\n          \"executable\" : \"Fabric.Core.Math.Sub\",\n          \"presetGUID\" : \"F9754B19F43BC017056B8BA291E7B8B4\"\n          },\n        {\n          \"objectType\" : \"Inst\",\n          \"metadata\" : {\n            \"uiGraphPos\" : \"{\\\"x\\\":327.569,\\\"y\\\":755.505}\"\n            },\n          \"name\" : \"UInt32_1\",\n          \"ports\" : [\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"In\",\n              \"defaultValues\" : {\n                \"UInt32\" : 1\n                },\n              \"name\" : \"value\"\n              }\n            ],\n          \"executable\" : \"Fabric.Core.Constants.UInt32\",\n"
		+ "          \"presetGUID\" : \"522214488375FF199C3D64A3DBF3C762\"\n          }\n        ],\n      \"connections\" : {\n        \"torso\" : [\n          \"assemble.torso\"\n          ],\n        \"chest\" : [\n          \"assemble.chest\"\n          ],\n        \"upChest\" : [\n          \"assemble.upchest\"\n          ],\n        \"neck\" : [\n          \"assemble.neck\"\n          ],\n        \"numDeformers\" : [\n          \"Convert_2.defaultVal\",\n          \"Sub_1.lhs\"\n          ],\n        \"neckRest\" : [\n          \"Set_1.value\"\n          ],\n        \"assemble.result\" : [\n          \"buildZSpline.mat44s\",\n          \"Size_1.this\"\n          ],\n        \"GetEmptyDebugShape2.result\" : [\n          \"DrawCurve.this\"\n          ],\n        \"EmptyDrawingHandle.handle\" : [\n          \"GetEmptyDebugShape2.this\",\n          \"DrawAxesInstances.this\"\n          ],\n        \"CreateSegs.result\" : [\n          \"DrawCurve.points\"\n          ],\n        \"CreateSegs.color\" : [\n          \"DrawCurve.color\"\n          ],\n        \"DrawCurve.dummyResult\" : [\n          \"Add_1.lhs\"\n          ],\n"
		+ "        \"buildZSpline.result\" : [\n          \"createXfosOnZSpline.this\",\n          \"CreateSegs.this\"\n          ],\n        \"DrawAxesInstances.dummyResult\" : [\n          \"Add_1.rhs\"\n          ],\n        \"createXfosOnZSpline.result\" : [\n          \"convertXfoToMat44_2.xfoArray\",\n          \"DrawAxesInstances.transforms\",\n          \"Set_1.this\"\n          ],\n        \"createXfosOnZSpline.medianXfos\" : [\n          \"convertXfoToMat44.xfoArray\"\n          ],\n        \"convertXfoToMat44_2.mat44Array\" : [\n          \"outputs\"\n          ],\n        \"Convert_2.result\" : [\n          \"buildZSpline.defSegs\"\n          ],\n        \"Size_1.result\" : [\n          \"Convert_2.size\"\n          ],\n        \"Sub_1.result\" : [\n          \"Set_1.index\"\n          ],\n        \"UInt32_1.value\" : [\n          \"Sub_1.rhs\"\n          ]\n        }\n      },\n    \"Fabric.Exts.InlineDrawing.DrawingHandle.GetEmptyDebugShape\" : {\n      \"objectType\" : \"Func\",\n      \"metadata\" : {\n        \"uiDocUrl\" : \"http://docs.fabric-engine.com/FabricEngine/2.0.1/HTML/KLExtensionsGuide/InlineDrawing/DrawingHandle.html\",\n"
		+ "        \"uiTooltip\" : \"helper function to clear a debug drawing shape\\n\\n Supported by DrawingHandle\"\n        },\n      \"title\" : \"GetEmptyDebugShape\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"exec\",\n          \"execPortType\" : \"IO\",\n          \"typeSpec\" : \"Execute\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"this\",\n          \"execPortType\" : \"IO\",\n          \"typeSpec\" : \"DrawingHandle\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"Out\",\n          \"defaultValues\" : {\n            \"String\" : \"debug\"\n            },\n          \"name\" : \"name\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"String\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"result\",\n          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"InlineDebugShape\"\n          }\n        ],\n      \"extDeps\" : {\n        \"InlineDrawing\" : \"*\",\n"
		+ "        \"FabricInterfaces\" : \"*\"\n        },\n      \"presetGUID\" : \"DB3916AA2CE58EEAFAEDB9E2653EF4D6\",\n      \"code\" : \"require InlineDrawing;\n\ndfgEntry {\n  result = this.getEmptyDebugShape(name);\n}\n\"\n      },\n    \"Fabric.Exts.InlineDrawing.DrawingHandle.EmptyDrawingHandle\" : {\n      \"objectType\" : \"Graph\",\n      \"title\" : \"EmptyDrawingHandle\",\n      \"cacheRule\" : \"never\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"handle\",\n          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"DrawingHandle\"\n          }\n        ],\n      \"extDeps\" : {},\n      \"presetGUID\" : \"2440020BA6A1CAB1CEB690A198F99C70\",\n      \"nodes\" : [\n        {\n          \"objectType\" : \"Inst\",\n          \"metadata\" : {\n            \"uiGraphPos\" : \"{\\\"x\\\": 894, \\\"y\\\": 100}\"\n            },\n          \"name\" : \"Clear\",\n          \"ports\" : [\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"IO\",\n              \"name\" : \"this\"\n              }\n            ],\n"
		+ "          \"executable\" : \"Fabric.Exts.InlineDrawing.DrawingHandle.Clear\",\n          \"cacheRule\" : \"never\"\n          },\n        {\n          \"objectType\" : \"Var\",\n          \"metadata\" : {\n            \"uiGraphPos\" : \"{\\\"x\\\":567.0,\\\"y\\\":56.0}\",\n            \"uiCollapsedState\" : \"0\"\n            },\n          \"name\" : \"handleVar\",\n          \"ports\" : [\n            {\n              \"objectType\" : \"VarPort\",\n              \"nodePortType\" : \"IO\",\n              \"name\" : \"value\"\n              }\n            ],\n          \"dataType\" : \"DrawingHandle\",\n          \"extDep\" : \"InlineDrawing:*\"\n          },\n        {\n          \"objectType\" : \"Inst\",\n          \"metadata\" : {\n            \"uiGraphPos\" : \"{\\\"x\\\":287.0,\\\"y\\\":56.0}\"\n            },\n          \"name\" : \"CreateDrawingHandle\",\n          \"ports\" : [\n            {\n              \"objectType\" : \"InstPort\",\n              \"nodePortType\" : \"Out\",\n              \"name\" : \"handle\"\n              }\n            ],\n          \"definition\" : {\n            \"objectType\" : \"Func\",\n            \"title\" : \"Create DrawingHandle\",\n"
		+ "            \"ports\" : [\n              {\n                \"objectType\" : \"Port\",\n                \"nodePortType\" : \"In\",\n                \"name\" : \"handle\",\n                \"execPortType\" : \"Out\",\n                \"typeSpec\" : \"DrawingHandle\"\n                }\n              ],\n            \"extDeps\" : {\n              \"InlineDrawing\" : \"*\"\n              },\n            \"code\" : \"dfgEntry {\n  handle = DrawingHandle();\n}\n\"\n            }\n          }\n        ],\n      \"connections\" : {\n        \"Clear.this\" : [\n          \"handle\"\n          ],\n        \"handleVar.value\" : [\n          \"Clear.this\"\n          ],\n        \"CreateDrawingHandle.handle\" : [\n          \"handleVar.value\"\n          ]\n        }\n      },\n    \"Fabric.Exts.InlineDrawing.DrawingHandle.Clear\" : {\n      \"objectType\" : \"Func\",\n      \"metadata\" : {\n        \"uiDocUrl\" : \"http://docs.fabric-engine.com/FabricEngine/2.0.0-beta/HTML/KLExtensionsGuide/InlineDrawing/DrawingHandle.html\",\n        \"uiTooltip\" : \"removes all contents from the DrawingHandle\\n\\n Supported by DrawingHandle\"\n"
		+ "        },\n      \"title\" : \"Clear\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"this\",\n          \"execPortType\" : \"IO\",\n          \"typeSpec\" : \"DrawingHandle\"\n          }\n        ],\n      \"extDeps\" : {\n        \"InlineDrawing\" : \"*\"\n        },\n      \"code\" : \"require InlineDrawing;\n\ndfgEntry {\n  this.clear();\n}\n\"\n      },\n    \"OSS.Exts.Curves.ZSpline.createSegsOnZSpline\" : {\n      \"objectType\" : \"Func\",\n      \"title\" : \"createSegsOnZSpline\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"result\",\n          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"Vec3[]\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"this\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"ZSpline\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"color\",\n          \"execPortType\" : \"Out\",\n"
		+ "          \"typeSpec\" : \"Color[]\"\n          }\n        ],\n      \"extDeps\" : {\n        \"Math\" : \"*\"\n        },\n      \"presetGUID\" : \"D8E844DE0169A7D9BB304C9F8DDF30A2\",\n      \"code\" : \"dfgEntry {\n  result.resize(0);\n  color.resize(0);\n  for(UInt32 n=0;n<this.BSplines.size();n++){\n    BSpline b = this.BSplines[n];\n    UInt32 resolution = b.resolution;\n    \n    // Color Settings\n    Scalar hue = mathRandomScalar(n,1);\n    Scalar saturation = 2;\n    \n    for(UInt32 k=0; k<=resolution; k++) {\n      Scalar t =  Scalar(k)/(resolution);\n      t = (t+n)/(this.BSplines.size());\n      Color c = randomColor(hue*180,saturation,this.normalizeT(t));\n      result.push(this.evalPosition(t));\n      color.push(c);\n    }\n  }\n}\n\"\n      },\n    \"OSS.Exts.Curves.ZSpline.drawCurve\" : {\n      \"objectType\" : \"Func\",\n      \"metadata\" : {\n        \"uiTextColor\" : \"{\\n  \\\"r\\\" : 20,\\n  \\\"g\\\" : 20,\\n  \\\"b\\\" : 20\\n  }\",\n        \"uiNodeColor\" : \"{\\n  \\\"r\\\" : 121,\\n  \\\"g\\\" : 134,\\n  \\\"b\\\" : 143\\n  }\"\n        },\n      \"title\" : \"drawCurve\",\n      \"ports\" : [\n"
		+ "        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"points\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Vec3[]\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"color\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Color[]\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"result\",\n          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"InlineDebugShape\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"this\",\n          \"execPortType\" : \"IO\",\n          \"typeSpec\" : \"InlineDebugShape\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"dummyResult\",\n          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"Vec3\"\n          }\n        ],\n      \"extDeps\" : {},\n      \"presetGUID\" : \"B3D1DFFCE15CC7040DCD73D99F2C3098\",\n"
		+ "      \"code\" : \"dfgEntry {\n  Index firstIndex = this.allocateLines(points.size(), points.size()-1);\n  Index colorIndex = firstIndex;\n  Vec3Attribute positionsAttr = this.attributes.getOrCreateAttribute('positions', Vec3Attribute);\n  Vec3Attribute normalsAttr = this.attributes.getOrCreateAttribute('normals', Vec3Attribute);\n  ColorAttribute vertexColorsAttr = this.attributes.getOrCreateColorAttribute('vertexColors');\n  \n\n  for( Integer i=0; i<points.size(); i++){\n    vertexColorsAttr.values[firstIndex] = color[i];\n    positionsAttr.values[firstIndex] = points[i];\n    normalsAttr.values[firstIndex++] = this.defaultNormal;\n    if(i > 0){\n      this.linesIndices[this.linesIndicesOffset++] = firstIndex - 2;\n      this.linesIndices[this.linesIndicesOffset++] = firstIndex - 1;\n    }\n  }\n\n  positionsAttr.incrementVersion();\n  normalsAttr.incrementVersion();\n  vertexColorsAttr.incrementVersion();\n\n  result = this;\n}\n\"\n      },\n    \"OSS.Exts.Curves.ZSpline.ZSpline\" : {\n      \"objectType\" : \"Func\",\n      \"metadata\" : {\n        \"uiTextColor\" : \"{\\n  \\\"r\\\" : 20,\\n  \\\"g\\\" : 20,\\n  \\\"b\\\" : 20\\n  }\",\n"
		+ "        \"uiNodeColor\" : \"{\\n  \\\"r\\\" : 121,\\n  \\\"g\\\" : 134,\\n  \\\"b\\\" : 143\\n  }\"\n        },\n      \"title\" : \"ZSpline\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"mat44s\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Mat44[]\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"result\",\n          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"ZSpline\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"isSegmentStart\",\n          \"execPortType\" : \"IO\",\n          \"typeSpec\" : \"Boolean[]\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"clamped\",\n          \"execPortType\" : \"IO\",\n          \"typeSpec\" : \"Boolean[]\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"weights\",\n          \"execPortType\" : \"IO\",\n"
		+ "          \"typeSpec\" : \"Scalar[]\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"resolution\",\n          \"execPortType\" : \"IO\",\n          \"typeSpec\" : \"UInt32[]\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"order\",\n          \"execPortType\" : \"IO\",\n          \"typeSpec\" : \"UInt32[]\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"closed\",\n          \"execPortType\" : \"IO\",\n          \"typeSpec\" : \"Boolean\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"defSegs\",\n          \"execPortType\" : \"IO\",\n          \"typeSpec\" : \"UInt32[]\"\n          }\n        ],\n      \"extDeps\" : {\n        \"Curves\" : \"*\",\n        \"Math\" : \"*\"\n        },\n      \"presetGUID\" : \"1A4FC39528C5CC9C3EF2B16480BD4E7B\",\n      \"code\" : \"dfgEntry { \n  result.buildZSpline(mat44s, isSegmentStart, weights, order, resolution, defSegs, clamped, closed);\n"
		+ "}\"\n      },\n    \"Fabric.Exts.InlineDrawing.DrawingHandle.DrawAxesInstances\" : {\n      \"objectType\" : \"Func\",\n      \"metadata\" : {\n        \"uiDocUrl\" : \"http://docs.fabric-engine.com/FabricEngine/2.0.1/HTML/KLExtensionsGuide/InlineDrawing/DrawingHandle.html\",\n        \"uiTooltip\" : \"helper function to draw axes at given transforms\\n\\n Supported by DrawingHandle\"\n        },\n      \"title\" : \"DrawAxesInstances\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"exec\",\n          \"execPortType\" : \"IO\",\n          \"typeSpec\" : \"Execute\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"this\",\n          \"execPortType\" : \"IO\",\n          \"typeSpec\" : \"DrawingHandle\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"name\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"String\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {\n"
		+ "            \"uiColor\" : \"{\\n  \\\"r\\\" : 249,\\n  \\\"g\\\" : 157,\\n  \\\"b\\\" : 28\\n  }\"\n            },\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"transforms\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Xfo[]\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {\n            \"uiColor\" : \"{\\n  \\\"r\\\" : 255,\\n  \\\"g\\\" : 242,\\n  \\\"b\\\" : 0\\n  }\"\n            },\n          \"nodePortType\" : \"In\",\n          \"name\" : \"dummyResult\",\n          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"Vec3\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"instance\",\n          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"InlineInstance\"\n          }\n        ],\n      \"extDeps\" : {\n        \"InlineDrawing\" : \"*\",\n        \"FabricInterfaces\" : \"*\"\n        },\n      \"presetGUID\" : \"A2DAC55CB1CE7426981A13F213257B7A\",\n      \"code\" : \"require InlineDrawing;\n\ndfgEntry {\n  this.drawAxesInstances(name, transforms, dummyResult, instance);\n}\n\"\n      },\n"
		+ "    \"OSS.Exts.Curves.ZSpline.createXfosOnZSplineSegments\" : {\n      \"objectType\" : \"Func\",\n      \"metadata\" : {\n        \"uiTextColor\" : \"{\\n  \\\"r\\\" : 20,\\n  \\\"g\\\" : 20,\\n  \\\"b\\\" : 20\\n  }\",\n        \"uiNodeColor\" : \"{\\n  \\\"r\\\" : 121,\\n  \\\"g\\\" : 134,\\n  \\\"b\\\" : 143\\n  }\"\n        },\n      \"title\" : \"createXfosOnZSplineSegments\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"this\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"ZSpline\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"result\",\n          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"Xfo[]\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"Out\",\n          \"defaultValues\" : {\n            \"Float32\" : 0\n            },\n          \"name\" : \"keepCurveLen\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Scalar\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"Out\",\n"
		+ "          \"defaultValues\" : {\n            \"Float32\" : 1\n            },\n          \"name\" : \"keepArcLen\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Scalar\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"medianXfos\",\n          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"Xfo[]\"\n          }\n        ],\n      \"extDeps\" : {\n        \"Math\" : \"*\"\n        },\n      \"presetGUID\" : \"9A8AFEEBF71811F541C71B0877BDF45B\",\n      \"code\" : \"dfgEntry {\n  result.resize(0);\n  for(UInt32 n=0;n<this.BSplines.size();n++){\n    for(UInt32 k=0; k<this.BSplines[n].defSegs; k++) {\n        Scalar t =  Scalar(k)/ Scalar(Math_max(1,(this.BSplines[n].defSegs-1)));\n        Xfo outXfo = Xfo(\n                this.BSplines[n].evalPosition(t,keepArcLen,keepCurveLen),\n                this.BSplines[n].evalOri(t,keepArcLen,keepCurveLen),\n                this.BSplines[n].evalScale(t,keepArcLen,keepCurveLen));\n        result.push(outXfo);\n        \n        // export on mid segments\n"
		+ "        if(k==0 && n!=0) {\n            medianXfos.push(outXfo.linearInterpolate(result[result.size()-2], 0.5));\n           // ToDo Export defrobulated Euler Angles on segment Joints\n        }\n    }\n  }\n}  \"\n      },\n    \"Fabric.Core.Math.Add\" : {\n      \"objectType\" : \"Func\",\n      \"title\" : \"Add\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"lhs\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"$TYPE$\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"rhs\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"$TYPE$\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"result\",\n          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"$TYPE$\"\n          }\n        ],\n      \"extDeps\" : {},\n      \"presetGUID\" : \"8146B3E77857E24CAE33F8B5284585E7\",\n      \"code\" : \"\ndfgEntry {\n\tresult = lhs + rhs;\n}\n\"\n      },\n    \"Fabric.Exts.Geometry.Func.Size\" : {\n"
		+ "      \"objectType\" : \"Func\",\n      \"metadata\" : {\n        \"uiDocUrl\" : \"http://docs.fabric-engine.com/FabricEngine/2.0.1/HTML/KLExtensionsGuide/Geometry/GeometryAttribute.html\",\n        \"uiTooltip\" : \"Returns the size of the attribute array.\\n\\n Supported by GeometryAttribute,GeometryAttributes,BaseAttribute,SkinningAttributeData,Points\"\n        },\n      \"title\" : \"Size\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"this\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"$TYPE$\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"result\",\n          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"Size\"\n          }\n        ],\n      \"extDeps\" : {\n        \"Geometry\" : \"*\"\n        },\n      \"presetGUID\" : \"3426735D9D96DD0F52A2A961A393053A\",\n      \"code\" : \"require Geometry;\n\ndfgEntry {\n  result = this.size();\n}\n\"\n      },\n    \"Fabric.Core.Math.Sub\" : {\n      \"objectType\" : \"Func\",\n      \"title\" : \"Sub\",\n"
		+ "      \"ports\" : [\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"lhs\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"$TYPE$\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"rhs\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"$TYPE$\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"result\",\n          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"$TYPE$\"\n          }\n        ],\n      \"extDeps\" : {},\n      \"presetGUID\" : \"F9754B19F43BC017056B8BA291E7B8B4\",\n      \"code\" : \"\ndfgEntry {\n\tresult = lhs - rhs;\n}\n\"\n      },\n    \"Fabric.Core.Constants.UInt32\" : {\n      \"objectType\" : \"Func\",\n      \"metadata\" : {\n        \"uiAlwaysShowDaisyChainPorts\" : \"true\"\n        },\n      \"title\" : \"UInt32\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"value\",\n          \"execPortType\" : \"In\",\n"
		+ "          \"typeSpec\" : \"UInt32\"\n          }\n        ],\n      \"extDeps\" : {},\n      \"presetGUID\" : \"522214488375FF199C3D64A3DBF3C762\",\n      \"code\" : \"dfgEntry {\n}\n\"\n      }\n    },\n  \"args\" : [\n    {\n      \"type\" : \"Mat44\",\n      \"value\" : {\n        \"row0\" : {\n          \"x\" : 1,\n          \"y\" : 0,\n          \"z\" : 0,\n          \"t\" : 0\n          },\n        \"row1\" : {\n          \"x\" : 0,\n          \"y\" : 1,\n          \"z\" : 0,\n          \"t\" : 9\n          },\n        \"row2\" : {\n          \"x\" : 0,\n          \"y\" : 0,\n          \"z\" : 1,\n          \"t\" : 0\n          },\n        \"row3\" : {\n          \"x\" : 0,\n          \"y\" : 0,\n          \"z\" : 0,\n          \"t\" : 1\n          }\n        },\n      \"ext\" : \"Math\"\n      },\n    {\n      \"type\" : \"Mat44\",\n      \"value\" : {\n        \"row0\" : {\n          \"x\" : 1,\n          \"y\" : 0,\n          \"z\" : 0,\n          \"t\" : 0\n          },\n        \"row1\" : {\n          \"x\" : 0,\n          \"y\" : 1,\n          \"z\" : 0,\n          \"t\" : 10\n          },\n        \"row2\" : {\n          \"x\" : 0,\n          \"y\" : 0,\n"
		+ "          \"z\" : 1,\n          \"t\" : 0\n          },\n        \"row3\" : {\n          \"x\" : 0,\n          \"y\" : 0,\n          \"z\" : 0,\n          \"t\" : 1\n          }\n        },\n      \"ext\" : \"Math\"\n      },\n    {\n      \"type\" : \"Mat44\",\n      \"value\" : {\n        \"row0\" : {\n          \"x\" : 1,\n          \"y\" : 0,\n          \"z\" : 0,\n          \"t\" : 0\n          },\n        \"row1\" : {\n          \"x\" : 0,\n          \"y\" : 1,\n          \"z\" : 0,\n          \"t\" : 12\n          },\n        \"row2\" : {\n          \"x\" : 0,\n          \"y\" : 0,\n          \"z\" : 1,\n          \"t\" : 0\n          },\n        \"row3\" : {\n          \"x\" : 0,\n          \"y\" : 0,\n          \"z\" : 0,\n          \"t\" : 1\n          }\n        },\n      \"ext\" : \"Math\"\n      },\n    {\n      \"type\" : \"Mat44\",\n      \"value\" : {\n        \"row0\" : {\n          \"x\" : 1,\n          \"y\" : 0,\n          \"z\" : 0,\n          \"t\" : 0\n          },\n        \"row1\" : {\n          \"x\" : 0,\n          \"y\" : 1,\n          \"z\" : 0,\n          \"t\" : 14\n          },\n        \"row2\" : {\n          \"x\" : 0,\n          \"y\" : 0,\n"
		+ "          \"z\" : 1,\n          \"t\" : 0\n          },\n        \"row3\" : {\n          \"x\" : 0,\n          \"y\" : 0,\n          \"z\" : 0,\n          \"t\" : 1\n          }\n        },\n      \"ext\" : \"Math\"\n      },\n    {\n      \"type\" : \"Mat44\",\n      \"value\" : {\n        \"row0\" : {\n          \"x\" : 1,\n          \"y\" : 0,\n          \"z\" : 0,\n          \"t\" : 0\n          },\n        \"row1\" : {\n          \"x\" : 0,\n          \"y\" : 1,\n          \"z\" : 0,\n          \"t\" : 15\n          },\n        \"row2\" : {\n          \"x\" : 0,\n          \"y\" : 0,\n          \"z\" : 1,\n          \"t\" : 0\n          },\n        \"row3\" : {\n          \"x\" : 0,\n          \"y\" : 0,\n          \"z\" : 0,\n          \"t\" : 1\n          }\n        },\n      \"ext\" : \"Math\"\n      },\n    {\n      \"type\" : \"Float32\",\n      \"value\" : 1\n      },\n    {\n      \"type\" : \"Boolean\",\n      \"value\" : false\n      },\n    {\n      \"type\" : \"Mat44[]\",\n      \"value\" : null,\n      \"ext\" : \"Math\"\n      },\n    {\n      \"type\" : \"SInt32\",\n      \"value\" : 6\n      }\n    ]\n  }");
	setAttr ".evalID" 2;
	setAttr -k on ".pelvis" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 9 0 1;
	setAttr -k on ".torso" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 10 0 1;
	setAttr -k on ".chest" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 12 0 1;
	setAttr -k on ".upChest" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 14 0 1;
	setAttr -k on ".neck" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 15 0 1;
	setAttr -k on ".rigScale" 1;
	setAttr -k on ".drawDebug" no;
	setAttr -s 6 ".outputs";
	setAttr -k on ".numDeformers" 6;
createNode decomposeMatrix -n "decomposeMatrix1";
	rename -uid "7F5E2CF7-4759-36DE-2554-B59B33FCECB5";
	setAttr ".or" -type "double3" 180 0 90.000006830188354 ;
	setAttr ".os" -type "double3" 1.0000001192092967 1.0000001192092682 1.0000002384185791 ;
createNode decomposeMatrix -n "decomposeMatrix2";
	rename -uid "ADD16E9D-45CC-A765-694A-E98DCCCEDBD6";
	setAttr ".ot" -type "double3" 0 3.0372886657714844 0 ;
	setAttr ".or" -type "double3" 180 0 90.000006830188354 ;
	setAttr ".os" -type "double3" 1.0000001192092967 1.0000001192092682 1.0000002384185791 ;
createNode decomposeMatrix -n "decomposeMatrix3";
	rename -uid "B281AEA0-4886-BB80-9D59-EB802361818B";
	setAttr ".ot" -type "double3" 0 6.0044374465942383 0 ;
	setAttr ".or" -type "double3" 180 0 90.000006830188354 ;
	setAttr ".os" -type "double3" 1.0000001192092967 1.0000001192092682 1.0000002384185791 ;
createNode decomposeMatrix -n "decomposeMatrix4";
	rename -uid "C084CE2B-4193-D8AF-AF72-E1BA16710151";
	setAttr ".ot" -type "double3" 0 9.0244817733764648 0 ;
	setAttr ".or" -type "double3" 180 0 90.000006830188354 ;
	setAttr ".os" -type "double3" 1.0000001192092967 1.0000001192092682 1.0000002384185791 ;
createNode decomposeMatrix -n "decomposeMatrix5";
	rename -uid "2011A7B3-4476-2072-E596-A28672B24333";
	setAttr ".ot" -type "double3" 0 12 0 ;
	setAttr ".or" -type "double3" 180 0 90.000006830188354 ;
	setAttr ".os" -type "double3" 1.0000001192092967 1.0000001192092682 1.0000002384185791 ;
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
		"{\n  \"objectType\" : \"Graph\",\n  \"metadata\" : {\n    \"maya_id\" : \"156\"\n    },\n  \"title\" : \"\",\n  \"ports\" : [\n    {\n      \"objectType\" : \"Port\",\n      \"nodePortType\" : \"IO\",\n      \"name\" : \"solver\",\n      \"execPortType\" : \"IO\",\n      \"typeSpec\" : \"MultiPoseConstraintSolver\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"drawDebug\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Boolean\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"rigScale\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Scalar\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"constrainers\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Mat44[]\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"nodePortType\" : \"In\",\n      \"name\" : \"constrainees\",\n"
		+ "      \"execPortType\" : \"Out\",\n      \"typeSpec\" : \"Mat44[]\"\n      }\n    ],\n  \"extDeps\" : {\n    \"Kraken\" : \"*\"\n    },\n  \"nodes\" : [\n    {\n      \"objectType\" : \"Inst\",\n      \"metadata\" : {\n        \"uiGraphPos\" : \"{\\\"x\\\":100.0,\\\"y\\\":100.0}\"\n        },\n      \"name\" : \"spineDeformerKLOp\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"solver\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"drawDebug\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"rigScale\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"constrainers\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"constrainees\"\n          }\n        ],\n      \"definition\" : {\n        \"objectType\" : \"Func\",\n        \"title\" : \"spineDeformerKLOp\",\n"
		+ "        \"ports\" : [\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"IO\",\n            \"name\" : \"solver\",\n            \"execPortType\" : \"IO\",\n            \"typeSpec\" : \"MultiPoseConstraintSolver\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"Out\",\n            \"name\" : \"drawDebug\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"Boolean\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"Out\",\n            \"name\" : \"rigScale\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"Scalar\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"Out\",\n            \"name\" : \"constrainers\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"Mat44[]\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"In\",\n            \"name\" : \"constrainees\",\n            \"execPortType\" : \"Out\",\n            \"typeSpec\" : \"Mat44[]\"\n"
		+ "            }\n          ],\n        \"extDeps\" : {\n          \"Kraken\" : \"*\"\n          },\n        \"code\" : \"dfgEntry {\n  constrainees.resize(6);\n  if(solver == null)\n    solver = MultiPoseConstraintSolver();\n  solver.solve(\n    drawDebug,\n    rigScale,\n    constrainers,\n    constrainees\n  );\n}\n\"\n        }\n      }\n    ],\n  \"connections\" : {\n    \"solver\" : [\n      \"spineDeformerKLOp.solver\"\n      ],\n    \"drawDebug\" : [\n      \"spineDeformerKLOp.drawDebug\"\n      ],\n    \"rigScale\" : [\n      \"spineDeformerKLOp.rigScale\"\n      ],\n    \"constrainers\" : [\n      \"spineDeformerKLOp.constrainers\"\n      ],\n    \"spineDeformerKLOp.solver\" : [\n      \"solver\"\n      ],\n    \"spineDeformerKLOp.constrainees\" : [\n      \"constrainees\"\n      ]\n    },\n  \"metadata\" : {\n    \"maya_id\" : \"156\"\n    },\n  \"args\" : [\n    {\n      \"type\" : \"MultiPoseConstraintSolver\",\n      \"value\" : null,\n      \"ext\" : \"Kraken\"\n      },\n    {\n      \"type\" : \"Boolean\",\n      \"value\" : false\n      },\n    {\n      \"type\" : \"Float32\",\n      \"value\" : 1\n      },\n    {\n      \"type\" : \"Mat44[]\",\n"
		+ "      \"value\" : null,\n      \"ext\" : \"Math\"\n      },\n    {\n      \"type\" : \"Mat44[]\",\n      \"value\" : null,\n      \"ext\" : \"Math\"\n      }\n    ]\n  }");
	setAttr ".evalID" 1;
	setAttr -k on ".drawDebug" no;
	setAttr -k on ".rigScale" 1;
	setAttr -s 6 ".constrainers";
	setAttr -k on ".constrainers[0]" -type "matrix" -1.1920928977282503e-007 1.0000001192092896 0 0
		 1.0000001192092611 1.1920928955077701e-007 1.2246469451366022e-016 0 1.2246470911258943e-016 1.4598929226474285e-023 -1.0000002384185791 0
		 0 0 0 1;
	setAttr -k on ".constrainers[1]" -type "matrix" -1.1920928977282503e-007 1.0000001192092896 0 0
		 1.0000001192092611 1.1920928955077701e-007 1.2246469451366022e-016 0 1.2246470911258943e-016 1.4598929226474285e-023 -1.0000002384185791 0
		 0 3.0372886657714844 0 1;
	setAttr -k on ".constrainers[2]" -type "matrix" -1.1920928977282503e-007 1.0000001192092896 0 0
		 1.0000001192092611 1.1920928955077701e-007 1.2246469451366022e-016 0 1.2246470911258943e-016 1.4598929226474285e-023 -1.0000002384185791 0
		 0 6.0044374465942383 0 1;
	setAttr -k on ".constrainers[3]" -type "matrix" -1.1920928977282503e-007 1.0000001192092896 0 0
		 1.0000001192092611 1.1920928955077701e-007 1.2246469451366022e-016 0 1.2246470911258943e-016 1.4598929226474285e-023 -1.0000002384185791 0
		 0 9.0244817733764648 0 1;
	setAttr -k on ".constrainers[4]" -type "matrix" -1.1920928977282503e-007 1.0000001192092896 0 0
		 1.0000001192092611 1.1920928955077701e-007 1.2246469451366022e-016 0 1.2246470911258943e-016 1.4598929226474285e-023 -1.0000002384185791 0
		 0 12 0 1;
	setAttr -k on ".constrainers[5]" -type "matrix" -1.1920928977282503e-007 1.0000001192092896 0 0
		 1.0000001192092611 1.1920928955077701e-007 1.2246469451366022e-016 0 1.2246470911258943e-016 1.4598929226474285e-023 -1.0000002384185791 0
		 0 15 0 1;
	setAttr -k on ".constrainers";
	setAttr -s 6 ".constrainees";
createNode decomposeMatrix -n "decomposeMatrix7";
	rename -uid "94A62A72-435C-C265-80B6-33879658B6FA";
	setAttr ".or" -type "double3" 180 0 90.000006830188354 ;
	setAttr ".os" -type "double3" 1.0000001192092967 1.0000001192092967 1.0000002384185791 ;
createNode decomposeMatrix -n "decomposeMatrix8";
	rename -uid "19074499-46BE-C9B2-7A2C-709D42233844";
	setAttr ".ot" -type "double3" 0 3.0372886657714844 0 ;
	setAttr ".or" -type "double3" 180 0 90.000006830188354 ;
	setAttr ".os" -type "double3" 1.0000001192092967 1.0000001192092967 1.0000002384185791 ;
createNode decomposeMatrix -n "decomposeMatrix9";
	rename -uid "EA594E3E-4BD2-F93A-0DF1-73B12A86169A";
	setAttr ".ot" -type "double3" 0 6.0044374465942383 0 ;
	setAttr ".or" -type "double3" 180 0 90.000006830188354 ;
	setAttr ".os" -type "double3" 1.0000001192092967 1.0000001192092967 1.0000002384185791 ;
createNode decomposeMatrix -n "decomposeMatrix10";
	rename -uid "090E7EFD-4673-5E70-B371-A0BEC5EC5C3B";
	setAttr ".ot" -type "double3" 0 9.0244817733764648 0 ;
	setAttr ".or" -type "double3" 180 0 90.000006830188354 ;
	setAttr ".os" -type "double3" 1.0000001192092967 1.0000001192092967 1.0000002384185791 ;
createNode decomposeMatrix -n "decomposeMatrix11";
	rename -uid "73C8C030-4A5F-4B48-1261-90841D3A874A";
	setAttr ".ot" -type "double3" 0 12 0 ;
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
		+ "                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 472\n                -height 366\n                -sceneRenderFilter 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n            modelEditor -e \n"
		+ "                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n"
		+ "            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n"
		+ "            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 472\n            -height 366\n            -sceneRenderFilter 0\n            $editorName;\n"
		+ "        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"side\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n"
		+ "                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -rendererName \"vp2Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n"
		+ "                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n"
		+ "                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 472\n                -height 366\n                -sceneRenderFilter 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n            modelEditor -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n"
		+ "            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n"
		+ "            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n"
		+ "            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 472\n            -height 366\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"front\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n"
		+ "                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -rendererName \"vp2Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n"
		+ "                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n"
		+ "                -width 472\n                -height 366\n                -sceneRenderFilter 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n            modelEditor -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n"
		+ "            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n"
		+ "            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n"
		+ "            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 472\n            -height 366\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n"
		+ "                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -rendererName \"vp2Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n"
		+ "                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n"
		+ "                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 475\n                -height 777\n                -sceneRenderFilter 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n            modelEditor -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\t}\n\t} else {\n"
		+ "\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n"
		+ "            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n"
		+ "            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 475\n            -height 777\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n"
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
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"scriptEditorPanel\" -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\tif ($useSceneConfig) {\n\t\tscriptedPanel -e -to $panelName;\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"profilerPanel\" (localizedPanelLabel(\"Profiler Tool\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"profilerPanel\" -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"Stereo\" (localizedPanelLabel(\"Stereo\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"Stereo\" -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels `;\nstring $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -editorChanged \"updateModelPanelBar\" \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n"
		+ "                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -rendererOverrideName \"stereoOverrideVP2\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n"
		+ "                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n"
		+ "                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 0\n                -height 0\n                -sceneRenderFilter 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                -useCustomBackground 1\n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n            stereoCameraView -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels  $panelName;\nstring $editorName = ($panelName+\"Editor\");\n"
		+ "            stereoCameraView -e \n                -editorChanged \"updateModelPanelBar\" \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n"
		+ "                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -rendererOverrideName \"stereoOverrideVP2\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n"
		+ "                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n"
		+ "                -captureSequenceNumber -1\n                -width 0\n                -height 0\n                -sceneRenderFilter 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                -useCustomBackground 1\n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n            stereoCameraView -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperShadePanel\" -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"nodeEditorPanel\" -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -defaultPinnedState 0\n                -additiveGraphingMode 1\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n"
		+ "                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -activeTab -1\n                -editorMode \"default\" \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -defaultPinnedState 0\n                -additiveGraphingMode 1\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n"
		+ "                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -activeTab -1\n                -editorMode \"default\" \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"vertical2\\\" -ps 1 36 100 -ps 2 64 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Outliner\")) \n\t\t\t\t\t\"outlinerPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `outlinerPanel -unParent -l (localizedPanelLabel(\\\"Outliner\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\noutlinerEditor -e \\n    -docTag \\\"isolOutln_fromSeln\\\" \\n    -showShapes 0\\n    -showReferenceNodes 1\\n    -showReferenceMembers 1\\n    -showAttributes 0\\n    -showConnected 0\\n    -showAnimCurvesOnly 0\\n    -showMuteInfo 0\\n    -organizeByLayer 1\\n    -showAnimLayerWeight 1\\n    -autoExpandLayers 1\\n    -autoExpand 0\\n    -showDagOnly 0\\n    -showAssets 1\\n    -showContainedOnly 1\\n    -showPublishedAsConnected 0\\n    -showContainerContents 1\\n    -ignoreDagHierarchy 0\\n    -expandConnections 0\\n    -showUpstreamCurves 1\\n    -showUnitlessCurves 1\\n    -showCompounds 1\\n    -showLeafs 1\\n    -showNumericAttrsOnly 0\\n    -highlightActive 1\\n    -autoSelectNewObjects 0\\n    -doNotSelectNewObjects 0\\n    -dropIsParent 1\\n    -transmitFilters 0\\n    -setFilter \\\"defaultSetFilter\\\" \\n    -showSetMembers 1\\n    -allowMultiSelection 1\\n    -alwaysToggleSelect 0\\n    -directSelect 0\\n    -displayMode \\\"DAG\\\" \\n    -expandObjects 0\\n    -setsIgnoreFilters 1\\n    -containersIgnoreFilters 0\\n    -editAttrName 0\\n    -showAttrValues 0\\n    -highlightSecondary 0\\n    -showUVAttrsOnly 0\\n    -showTextureNodesOnly 0\\n    -attrAlphaOrder \\\"default\\\" \\n    -animLayerFilterOptions \\\"allAffecting\\\" \\n    -sortOrder \\\"none\\\" \\n    -longNames 0\\n    -niceNames 1\\n    -showNamespace 1\\n    -showPinIcons 0\\n    -mapMotionTrails 0\\n    -ignoreHiddenAttribute 0\\n    -ignoreOutlinerColor 0\\n    $editorName\"\n"
		+ "\t\t\t\t\t\"outlinerPanel -edit -l (localizedPanelLabel(\\\"Outliner\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\noutlinerEditor -e \\n    -docTag \\\"isolOutln_fromSeln\\\" \\n    -showShapes 0\\n    -showReferenceNodes 1\\n    -showReferenceMembers 1\\n    -showAttributes 0\\n    -showConnected 0\\n    -showAnimCurvesOnly 0\\n    -showMuteInfo 0\\n    -organizeByLayer 1\\n    -showAnimLayerWeight 1\\n    -autoExpandLayers 1\\n    -autoExpand 0\\n    -showDagOnly 0\\n    -showAssets 1\\n    -showContainedOnly 1\\n    -showPublishedAsConnected 0\\n    -showContainerContents 1\\n    -ignoreDagHierarchy 0\\n    -expandConnections 0\\n    -showUpstreamCurves 1\\n    -showUnitlessCurves 1\\n    -showCompounds 1\\n    -showLeafs 1\\n    -showNumericAttrsOnly 0\\n    -highlightActive 1\\n    -autoSelectNewObjects 0\\n    -doNotSelectNewObjects 0\\n    -dropIsParent 1\\n    -transmitFilters 0\\n    -setFilter \\\"defaultSetFilter\\\" \\n    -showSetMembers 1\\n    -allowMultiSelection 1\\n    -alwaysToggleSelect 0\\n    -directSelect 0\\n    -displayMode \\\"DAG\\\" \\n    -expandObjects 0\\n    -setsIgnoreFilters 1\\n    -containersIgnoreFilters 0\\n    -editAttrName 0\\n    -showAttrValues 0\\n    -highlightSecondary 0\\n    -showUVAttrsOnly 0\\n    -showTextureNodesOnly 0\\n    -attrAlphaOrder \\\"default\\\" \\n    -animLayerFilterOptions \\\"allAffecting\\\" \\n    -sortOrder \\\"none\\\" \\n    -longNames 0\\n    -niceNames 1\\n    -showNamespace 1\\n    -showPinIcons 0\\n    -mapMotionTrails 0\\n    -ignoreHiddenAttribute 0\\n    -ignoreOutlinerColor 0\\n    $editorName\"\n"
		+ "\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 475\\n    -height 777\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 475\\n    -height 777\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        setFocus `paneLayout -q -p1 $gMainPane`;\n        sceneUIReplacement -deleteRemaining;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "CFC7ACBE-4AD4-E98E-49E7-A4B823B9640F";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode ilrOptionsNode -s -n "TurtleRenderOptions";
	rename -uid "788F668F-4591-EA63-55DE-97A253D77BD6";
lockNode -l 1 ;
createNode ilrUIOptionsNode -s -n "TurtleUIOptions";
	rename -uid "6ECB3F0E-4ABC-8F72-6730-8396F7B40DA1";
lockNode -l 1 ;
createNode ilrBakeLayerManager -s -n "TurtleBakeLayerManager";
	rename -uid "41E35C7D-4FD2-BFC0-9F9B-2EB5B336777A";
lockNode -l 1 ;
createNode ilrBakeLayer -s -n "TurtleDefaultBakeLayer";
	rename -uid "55D059D7-4B87-ABD7-9BB0-CE9063665A6E";
lockNode -l 1 ;
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
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of ZSplineSpineComponent.ma
