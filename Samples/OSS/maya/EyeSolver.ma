//Maya ASCII 2016 scene
//Name: EyeSolver.ma
//Last modified: Thu, Feb 18, 2016 05:18:52 PM
//Codeset: 1252
requires maya "2016";
requires -nodeType "decomposeMatrix" "matrixNodes" "1.0";
requires -nodeType "dfgMayaNode" -nodeType "canvasNode" -dataType "FabricSpliceMayaData"
		 "FabricMaya" "2.0.1";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2016";
fileInfo "version" "2016";
fileInfo "cutIdentifier" "201508242200-969261";
fileInfo "osv" "Microsoft Windows 7 Enterprise Edition, 64-bit Windows 7 Service Pack 1 (Build 7601)\n";
createNode transform -s -n "persp";
	rename -uid "5AE40F1A-4964-6782-77D8-B590168DC2BE";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1.3040386943954578 23.112672885559071 19.932681634156356 ;
	setAttr ".r" -type "double3" -28.538352729606473 -2.9999999999991589 -1.9905746893448689e-016 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "AEF58BF7-41F0-C6B8-27BF-89A71D15F304";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 28.888794012014682;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 2 15 1.6653345369377348e-016 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "5E446E3B-4B50-4CE1-67DB-4490AF8B2736";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 100.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "B1037928-4DDB-7EFE-B727-9FA8E4B0B580";
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
	rename -uid "3A48AD37-4E5E-7D90-0872-E2AAD05B7298";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 100.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "336BAE4F-469C-CEC7-35B3-6C9C63323A08";
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
	rename -uid "DDEAECED-48B8-EED9-E582-3A8A653D73E8";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 100.1 0 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "90808956-4C2B-B4C6-9CA9-1EB9DAEE750F";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "pCube1";
	rename -uid "92E409FC-4A6A-EEF4-0C6A-B4930141BF0C";
	setAttr ".dla" yes;
createNode mesh -n "pCubeShape1" -p "pCube1";
	rename -uid "5E87F89C-4C26-79D7-0536-D580270E8AC0";
	setAttr -k off ".v";
	setAttr -s 6 ".iog[0].og";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
createNode transform -n "group1";
	rename -uid "B06836DA-4499-034F-8ADD-7694148C2284";
createNode transform -n "MyRig" -p "group1";
	rename -uid "26E3855A-49F3-835C-B919-E68A43EBBC2E";
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
	rename -uid "BDB9A675-4EE1-3C0C-5738-B5BC4BA20636";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "M_eyes_cmp" -p "MyRig_controls";
	rename -uid "0F335981-4B46-EC9B-6B17-689D4389585D";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "M_inputs_hrc" -p "|group1|MyRig|MyRig_controls|M_eyes_cmp";
	rename -uid "C983DDE2-4B24-E34D-59F3-C1B0DA9A763E";
	addAttr -ci true -k true -sn "inputs" -ln "inputs" -nn "inputs" -min 0 -max 0 -en 
		"-----" -at "enum";
	addAttr -ci true -k true -sn "drawDebug" -ln "drawDebug" -nn "drawDebug" -min 0 
		-max 1 -at "bool";
	addAttr -ci true -k true -sn "rigScale" -ln "rigScale" -nn "rigScale" -dv 1 -at "float";
	addAttr -ci true -k true -sn "rightSide" -ln "rightSide" -nn "rightSide" -min 0 
		-max 1 -at "bool";
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
createNode transform -n "M_globalSRT_cmpIn" -p "M_inputs_hrc";
	rename -uid "AD930305-42B7-3533-AEA1-CEAEA6A64B4A";
createNode locator -n "M_globalSRT_cmpInShape" -p "M_globalSRT_cmpIn";
	rename -uid "AB1922AC-4629-3277-2DA0-779597684626";
	setAttr -k off ".v" no;
createNode transform -n "M_parentSpace_cmpIn" -p "M_inputs_hrc";
	rename -uid "A198BC56-4D73-2C19-47FC-1B8B217EF578";
	setAttr ".t" -type "double3" 0 15 0 ;
createNode locator -n "M_parentSpace_cmpInShape" -p "M_parentSpace_cmpIn";
	rename -uid "4495FB16-4368-BA5A-54DC-268AB2C9ADA3";
	setAttr -k off ".v" no;
createNode transform -n "M_outputs_hrc" -p "|group1|MyRig|MyRig_controls|M_eyes_cmp";
	rename -uid "3F44EC9A-4921-E886-7818-6686F5139236";
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
createNode transform -n "M_eyes_cmpOut" -p "M_outputs_hrc";
	rename -uid "80833ABF-402D-33E6-42F2-0A82BADDAB4E";
createNode locator -n "M_eyes_cmpOutShape" -p "M_eyes_cmpOut";
	rename -uid "3D6603C9-4A4F-64B3-F940-3894E70A1EB7";
	setAttr -k off ".v" no;
createNode transform -n "M_eyesEnd_cmpOut" -p "M_outputs_hrc";
	rename -uid "18760716-48F1-D661-E022-D9BEF570B2B7";
	setAttr ".t" -type "double3" 0 15 10 ;
createNode locator -n "M_eyesEnd_cmpOutShape" -p "M_eyesEnd_cmpOut";
	rename -uid "399F715B-4B0A-2049-EBFB-B482ABBBE7E2";
	setAttr -k off ".v" no;
createNode transform -n "M_eyes_space" -p "|group1|MyRig|MyRig_controls|M_eyes_cmp";
	rename -uid "C3B410A0-49AC-65C8-32E4-789AF1EB7C91";
	setAttr ".t" -type "double3" 0 15 0 ;
createNode transform -n "M_L_Eye_fK_space" -p "M_eyes_space";
	rename -uid "1D9A8C76-4226-5658-ADBF-D383A03F6070";
	setAttr ".t" -type "double3" 2 0 0 ;
	setAttr ".r" -type "double3" 4.3803983886993958 26.917007817590296 3.5237460081958698 ;
createNode transform -n "M_L_Eye_fK_an" -p "M_L_Eye_fK_space";
	rename -uid "9518D00C-474C-0920-3A36-BBA1B4C1B6BA";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".t" -type "double3" 0 1.7763568394002505e-015 8.3266726846886741e-017 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr ".r" -type "double3" 13.130052260519381 -51.353104275508294 6.0509986670821965 ;
createNode nurbsCurve -n "M_L_Eye_fK_anShape" -p "M_L_Eye_fK_an";
	rename -uid "3444D9D1-4367-0337-D5F3-BCA7677CE798";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 12 0 no 3
		13 0 1 2 3 4 5 6 7 8 9 10 11 12
		13
		0.34999999403953552 0.34999999403953552 2
		0.49999997019767761 0 2
		0.34999999403953552 -0.34999999403953552 2
		0 -0.49999997019767761 2
		-0.34999999403953552 -0.34999999403953552 2
		-0.49999997019767761 0 2
		-0.34999999403953552 0.34999999403953552 2
		0 0.49999997019767761 2
		0 0 2
		0 0 1.1920928955078125e-007
		0 0 2
		0 0.49999997019767761 2
		0.34999999403953552 0.34999999403953552 2
		;
createNode transform -n "M_L_Eye_ik_space" -p "M_eyes_space";
	rename -uid "DF9B2188-436A-6A8C-85EE-AE8BD6D8C8E3";
	setAttr ".t" -type "double3" 2 0 0 ;
	setAttr ".r" -type "double3" 4.3803983886993958 26.917007817590296 3.5237460081958698 ;
createNode transform -n "M_R_Eye_fK_space" -p "M_eyes_space";
	rename -uid "5E72574A-4EBC-BEE9-FB47-8C9A9AB5C73B";
	setAttr ".t" -type "double3" -2 0 0 ;
createNode transform -n "M_R_Eye_fK_an" -p "M_R_Eye_fK_space";
	rename -uid "3A527750-419A-035A-2D4A-74804F6F9AFE";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
createNode nurbsCurve -n "M_R_Eye_fK_anShape" -p "M_R_Eye_fK_an";
	rename -uid "2D5BE177-4BCE-082F-FC7C-EFBE3D61FF53";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 12 0 no 3
		13 0 1 2 3 4 5 6 7 8 9 10 11 12
		13
		0.34999999403953552 0.34999999403953552 2
		0.49999997019767761 0 2
		0.34999999403953552 -0.34999999403953552 2
		0 -0.49999997019767761 2
		-0.34999999403953552 -0.34999999403953552 2
		-0.49999997019767761 0 2
		-0.34999999403953552 0.34999999403953552 2
		0 0.49999997019767761 2
		0 0 2
		0 0 1.1920928955078125e-007
		0 0 2
		0 0.49999997019767761 2
		0.34999999403953552 0.34999999403953552 2
		;
createNode transform -n "M_R_Eye_ik_space" -p "M_eyes_space";
	rename -uid "247E4F08-4EA8-898D-0805-8E8667BCF6FF";
	setAttr ".t" -type "double3" -2 0 0 ;
createNode transform -n "M_R_Yeakfdjs_fK_space" -p "M_eyes_space";
	rename -uid "7EAF45B4-425F-3C9C-B33B-339083796E0E";
	setAttr ".t" -type "double3" -4 0 0 ;
createNode transform -n "M_R_Yeakfdjs_fK_an" -p "M_R_Yeakfdjs_fK_space";
	rename -uid "9BF9709F-4956-0C06-E3B8-40B0D7A44336";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
createNode nurbsCurve -n "M_R_Yeakfdjs_fK_anShape" -p "M_R_Yeakfdjs_fK_an";
	rename -uid "2478DB44-47DE-5D35-03C8-CCA4F9FC74FC";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 12 0 no 3
		13 0 1 2 3 4 5 6 7 8 9 10 11 12
		13
		0.34999999403953552 0.34999999403953552 2
		0.49999997019767761 0 2
		0.34999999403953552 -0.34999999403953552 2
		0 -0.49999997019767761 2
		-0.34999999403953552 -0.34999999403953552 2
		-0.49999997019767761 0 2
		-0.34999999403953552 0.34999999403953552 2
		0 0.49999997019767761 2
		0 0 2
		0 0 1.1920928955078125e-007
		0 0 2
		0 0.49999997019767761 2
		0.34999999403953552 0.34999999403953552 2
		;
createNode transform -n "M_R_Yeakfdjs_ik_space" -p "M_eyes_space";
	rename -uid "6360B628-4CB9-9A71-05E0-FABB9830A511";
	setAttr ".t" -type "double3" -4 0 0 ;
createNode transform -n "M_eyesTarget_space" -p "|group1|MyRig|MyRig_controls|M_eyes_cmp";
	rename -uid "F7083461-40EF-2021-F4A3-508E638188B2";
	setAttr ".t" -type "double3" 0 15 10 ;
createNode transform -n "M_eyes_an" -p "M_eyesTarget_space";
	rename -uid "957DC8F4-4852-5509-9511-CCAF2665E511";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".t" -type "double3" 0.78275272547795449 -0.58991492160388148 0.36227173666144985 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
createNode nurbsCurve -n "M_eyes_anShape" -p "M_eyes_an";
	rename -uid "C7500C7F-459B-D223-5446-BD983A1A84C7";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 2 no 3
		5 0 1 2 3 4
		5
		0.49999997019767761 0.49999997019767761 0
		0.49999997019767761 -0.49999997019767761 0
		-0.49999997019767761 -0.49999997019767761 0
		-0.49999997019767761 0.49999997019767761 0
		0.49999997019767761 0.49999997019767761 0
		;
createNode transform -n "M_L_Eye_ik_space" -p "M_eyes_an";
	rename -uid "9E9EE311-4FD3-C1CB-B426-48AF13100264";
	setAttr ".t" -type "double3" 6.5521807670593262 -0.4849090576171875 -1.1094141006469727 ;
	setAttr ".r" -type "double3" 4.3803983886993958 26.917007817590296 3.5237460081958698 ;
createNode transform -n "M_L_Eye_ik_an" -p "|group1|MyRig|MyRig_controls|M_eyes_cmp|M_eyesTarget_space|M_eyes_an|M_L_Eye_ik_space";
	rename -uid "1E2661BD-4B2D-43D5-8F58-FB83F36654D4";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".t" -type "double3" 0 3.5527136788005009e-015 1.7763568394002505e-015 ;
	setAttr ".r" -type "double3" 9.9392333795734899e-016 6.3238372377536337e-015 -3.975693351829396e-016 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
createNode nurbsCurve -n "M_L_Eye_ik_anShape" -p "M_L_Eye_ik_an";
	rename -uid "7AA5B9B0-453F-6BD3-2E77-5885F1C90445";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 2 no 3
		5 0 1 2 3 4
		5
		0.24999998509883881 0.24999998509883881 0
		0.24999998509883881 -0.24999998509883881 0
		-0.24999998509883881 -0.24999998509883881 0
		-0.24999998509883881 0.24999998509883881 0
		0.24999998509883881 0.24999998509883881 0
		;
createNode transform -n "M_R_Eye_ik_space" -p "M_eyes_an";
	rename -uid "21A979B2-418A-7151-30AD-A9B73ADC2482";
	setAttr ".t" -type "double3" -2 0 0 ;
createNode transform -n "M_R_Eye_ik_an" -p "|group1|MyRig|MyRig_controls|M_eyes_cmp|M_eyesTarget_space|M_eyes_an|M_R_Eye_ik_space";
	rename -uid "3B2BC154-45C8-C616-2160-8D8E6D840565";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
createNode nurbsCurve -n "M_R_Eye_ik_anShape" -p "M_R_Eye_ik_an";
	rename -uid "D5BC2419-4F0F-2AA0-D87F-FFB08088E5CF";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 2 no 3
		5 0 1 2 3 4
		5
		0.24999998509883881 0.24999998509883881 0
		0.24999998509883881 -0.24999998509883881 0
		-0.24999998509883881 -0.24999998509883881 0
		-0.24999998509883881 0.24999998509883881 0
		0.24999998509883881 0.24999998509883881 0
		;
createNode transform -n "M_R_Yeakfdjs_ik_space" -p "M_eyes_an";
	rename -uid "1931344A-4645-BFEC-8EFF-459F33462CAE";
	setAttr ".t" -type "double3" -4 0 0 ;
createNode transform -n "M_R_Yeakfdjs_ik_an" -p "|group1|MyRig|MyRig_controls|M_eyes_cmp|M_eyesTarget_space|M_eyes_an|M_R_Yeakfdjs_ik_space";
	rename -uid "86948D3E-4465-F795-C2BD-AFB79FA8EEE2";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
createNode nurbsCurve -n "M_R_Yeakfdjs_ik_anShape" -p "M_R_Yeakfdjs_ik_an";
	rename -uid "262650E2-4ABD-1F74-F661-B3953CE243C3";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 2 no 3
		5 0 1 2 3 4
		5
		0.24999998509883881 0.24999998509883881 0
		0.24999998509883881 -0.24999998509883881 0
		-0.24999998509883881 -0.24999998509883881 0
		-0.24999998509883881 0.24999998509883881 0
		0.24999998509883881 0.24999998509883881 0
		;
createNode transform -n "MyRig_deformers" -p "MyRig";
	rename -uid "E6B9060E-49B9-54A8-A105-E5B63960F420";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "M_eyes_cmp" -p "MyRig_deformers";
	rename -uid "B2D88F7C-43DF-76A1-A7F9-C59527FCFF5A";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode joint -n "M_L_Eye_fK_def" -p "|group1|MyRig|MyRig_deformers|M_eyes_cmp";
	rename -uid "9C6CC792-4E66-CFD4-B13F-279F9770886C";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".pa" -type "double3" 4.3803985734781543 26.917008974573104 3.5237460915167769 ;
createNode joint -n "M_L_Eye_ik_def" -p "|group1|MyRig|MyRig_deformers|M_eyes_cmp";
	rename -uid "9050E407-4EA3-9025-8A7C-ACA7D040192C";
	setAttr ".v" no;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "M_R_Eye_fK_def" -p "|group1|MyRig|MyRig_deformers|M_eyes_cmp";
	rename -uid "BFA0E8A7-4485-272F-35AB-15821E735A53";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "M_R_Eye_ik_def" -p "|group1|MyRig|MyRig_deformers|M_eyes_cmp";
	rename -uid "259CC25D-4BFE-6764-55FB-F3887ADD302A";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "M_R_Yeakfdjs_fK_def" -p "|group1|MyRig|MyRig_deformers|M_eyes_cmp";
	rename -uid "72DD3FD3-40B1-058F-DAAF-1E9C483C8D1F";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "M_R_Yeakfdjs_ik_def" -p "|group1|MyRig|MyRig_deformers|M_eyes_cmp";
	rename -uid "40D1FCEF-4EBC-5BC8-2367-C3A90715C452";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "A75F99CF-442A-05E0-974E-6699D619261F";
	setAttr -s 4 ".lnk";
	setAttr -s 4 ".slnk";
createNode displayLayerManager -n "layerManager";
	rename -uid "23D6C138-4602-E707-D8CC-53A9B731DD1A";
createNode displayLayer -n "defaultLayer";
	rename -uid "DAF94455-47FF-EFB7-2CA5-45880CC56547";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "7D908D02-464D-38E8-D24E-FD87A4086ED1";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "AA273391-47FB-BE20-9051-ECB82464E66F";
	setAttr ".g" yes;
createNode dfgMayaNode -n "MeyesL_EyeDeformerJointsKLOp";
	rename -uid "867EF281-45F7-0A70-F3BC-968B84416B0C";
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
		"{\n  \"objectType\" : \"Graph\",\n  \"metadata\" : {\n    \"maya_id\" : \"1\"\n    },\n  \"title\" : \"\",\n  \"ports\" : [\n    {\n      \"objectType\" : \"Port\",\n      \"nodePortType\" : \"IO\",\n      \"name\" : \"solver\",\n      \"execPortType\" : \"IO\",\n      \"typeSpec\" : \"MultiPoseConstraintSolver\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"drawDebug\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Boolean\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"rigScale\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Scalar\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"constrainers\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Mat44[]\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"nodePortType\" : \"In\",\n      \"name\" : \"constrainees\",\n"
		+ "      \"execPortType\" : \"Out\",\n      \"typeSpec\" : \"Mat44[]\"\n      }\n    ],\n  \"extDeps\" : {\n    \"Kraken\" : \"*\"\n    },\n  \"nodes\" : [\n    {\n      \"objectType\" : \"Inst\",\n      \"metadata\" : {\n        \"uiGraphPos\" : \"{\\\"x\\\":100.0,\\\"y\\\":100.0}\"\n        },\n      \"name\" : \"MeyesL_EyeDeformerJointsKLOp\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"solver\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"drawDebug\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"rigScale\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"constrainers\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"constrainees\"\n          }\n        ],\n      \"definition\" : {\n        \"objectType\" : \"Func\",\n        \"title\" : \"MeyesL_EyeDeformerJointsKLOp\",\n"
		+ "        \"ports\" : [\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"IO\",\n            \"name\" : \"solver\",\n            \"execPortType\" : \"IO\",\n            \"typeSpec\" : \"MultiPoseConstraintSolver\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"Out\",\n            \"name\" : \"drawDebug\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"Boolean\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"Out\",\n            \"name\" : \"rigScale\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"Scalar\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"Out\",\n            \"name\" : \"constrainers\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"Mat44[]\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"In\",\n            \"name\" : \"constrainees\",\n            \"execPortType\" : \"Out\",\n            \"typeSpec\" : \"Mat44[]\"\n"
		+ "            }\n          ],\n        \"extDeps\" : {\n          \"Kraken\" : \"*\"\n          },\n        \"code\" : \"dfgEntry {\n  constrainees.resize(2);\n  if(solver == null)\n    solver = MultiPoseConstraintSolver();\n  solver.solve(\n    drawDebug,\n    rigScale,\n    constrainers,\n    constrainees\n  );\n}\n\"\n        }\n      }\n    ],\n  \"connections\" : {\n    \"solver\" : [\n      \"MeyesL_EyeDeformerJointsKLOp.solver\"\n      ],\n    \"drawDebug\" : [\n      \"MeyesL_EyeDeformerJointsKLOp.drawDebug\"\n      ],\n    \"rigScale\" : [\n      \"MeyesL_EyeDeformerJointsKLOp.rigScale\"\n      ],\n    \"constrainers\" : [\n      \"MeyesL_EyeDeformerJointsKLOp.constrainers\"\n      ],\n    \"MeyesL_EyeDeformerJointsKLOp.solver\" : [\n      \"solver\"\n      ],\n    \"MeyesL_EyeDeformerJointsKLOp.constrainees\" : [\n      \"constrainees\"\n      ]\n    },\n  \"metadata\" : {\n    \"maya_id\" : \"1\"\n    },\n  \"args\" : [\n    {\n      \"type\" : \"MultiPoseConstraintSolver\",\n      \"value\" : null,\n      \"ext\" : \"Kraken\"\n      },\n    {\n      \"type\" : \"Boolean\",\n      \"value\" : false\n      },\n    {\n"
		+ "      \"type\" : \"Float32\",\n      \"value\" : 1\n      },\n    {\n      \"type\" : \"Mat44[]\",\n      \"value\" : null,\n      \"ext\" : \"Math\"\n      },\n    {\n      \"type\" : \"Mat44[]\",\n      \"value\" : null,\n      \"ext\" : \"Math\"\n      }\n    ]\n  }");
	setAttr ".evalID" 1;
	setAttr -k on ".drawDebug" no;
	setAttr -k on ".rigScale" 1;
	setAttr -s 2 ".constrainers";
	setAttr -k on ".constrainers[0]" -type "matrix" 0.90647833100972375 0.061819673354486182 0.41770248191286874 0
		 -0.20922496883447106 0.92500867951754617 0.31714957864298043 0 -0.36677233786920266 -0.37488300948902714 0.85143454320952328 0
		 2 15.000000000000002 1.9500490166819629e-016 1;
	setAttr -k on ".constrainers[1]" -type "matrix" 0.88997742022344106 0.054803587717456581 -0.45269941270750902 0
		 -0.026771802756216302 0.99731900630698034 0.068103379035401271 0 0.45521803794402826 -0.048490890197565202 0.88905858721359687 0
		 7.3349334925372816 13.925176020778935 9.252857636014479 1;
	setAttr -k on ".constrainers";
	setAttr -s 2 ".constrainees";
createNode decomposeMatrix -n "decomposeMatrix1";
	rename -uid "AA2DF0AE-457D-F3FB-398A-9C9BF4356550";
	setAttr ".ot" -type "double3" 2 15 1.9500490449873029e-016 ;
	setAttr ".or" -type "double3" 20.429784508215867 -24.689620709928217 3.9013953602805476 ;
	setAttr ".os" -type "double3" 1.0000000188974203 0.99999997729135459 0.99999997758581571 ;
createNode decomposeMatrix -n "decomposeMatrix2";
	rename -uid "F9CCCD31-4351-6CBF-F60C-798ABD612A89";
	setAttr ".ot" -type "double3" 7.3349332809448242 13.925175666809082 9.2528572082519531 ;
	setAttr ".or" -type "double3" 4.3803985734781543 26.917008974573104 3.5237460915167764 ;
	setAttr ".os" -type "double3" 0.99999998260059197 0.99999997692507081 1.0000000064582111 ;
	setAttr ".osh" -type "double3" -1.9181410583399138e-009 -1.3446171311696332e-008 
		3.3370707578785105e-009 ;
	setAttr ".oqx" 0.029999278925381751;
	setAttr ".oqy" 0.23360384055990982;
	setAttr ".oqz" 0.020989048712661419;
	setAttr ".oqw" 0.97164229466082563;
createNode dfgMayaNode -n "MeyesR_EyeDeformerJointsKLOp";
	rename -uid "2A298D9C-4D98-CFDB-02C5-F68C298446F1";
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
		+ "      \"execPortType\" : \"Out\",\n      \"typeSpec\" : \"Mat44[]\"\n      }\n    ],\n  \"extDeps\" : {\n    \"Kraken\" : \"*\"\n    },\n  \"nodes\" : [\n    {\n      \"objectType\" : \"Inst\",\n      \"metadata\" : {\n        \"uiGraphPos\" : \"{\\\"x\\\":100.0,\\\"y\\\":100.0}\"\n        },\n      \"name\" : \"MeyesR_EyeDeformerJointsKLOp\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"solver\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"drawDebug\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"rigScale\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"constrainers\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"constrainees\"\n          }\n        ],\n      \"definition\" : {\n        \"objectType\" : \"Func\",\n        \"title\" : \"MeyesR_EyeDeformerJointsKLOp\",\n"
		+ "        \"ports\" : [\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"IO\",\n            \"name\" : \"solver\",\n            \"execPortType\" : \"IO\",\n            \"typeSpec\" : \"MultiPoseConstraintSolver\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"Out\",\n            \"name\" : \"drawDebug\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"Boolean\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"Out\",\n            \"name\" : \"rigScale\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"Scalar\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"Out\",\n            \"name\" : \"constrainers\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"Mat44[]\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"In\",\n            \"name\" : \"constrainees\",\n            \"execPortType\" : \"Out\",\n            \"typeSpec\" : \"Mat44[]\"\n"
		+ "            }\n          ],\n        \"extDeps\" : {\n          \"Kraken\" : \"*\"\n          },\n        \"code\" : \"dfgEntry {\n  constrainees.resize(2);\n  if(solver == null)\n    solver = MultiPoseConstraintSolver();\n  solver.solve(\n    drawDebug,\n    rigScale,\n    constrainers,\n    constrainees\n  );\n}\n\"\n        }\n      }\n    ],\n  \"connections\" : {\n    \"solver\" : [\n      \"MeyesR_EyeDeformerJointsKLOp.solver\"\n      ],\n    \"drawDebug\" : [\n      \"MeyesR_EyeDeformerJointsKLOp.drawDebug\"\n      ],\n    \"rigScale\" : [\n      \"MeyesR_EyeDeformerJointsKLOp.rigScale\"\n      ],\n    \"constrainers\" : [\n      \"MeyesR_EyeDeformerJointsKLOp.constrainers\"\n      ],\n    \"MeyesR_EyeDeformerJointsKLOp.solver\" : [\n      \"solver\"\n      ],\n    \"MeyesR_EyeDeformerJointsKLOp.constrainees\" : [\n      \"constrainees\"\n      ]\n    },\n  \"metadata\" : {\n    \"maya_id\" : \"2\"\n    },\n  \"args\" : [\n    {\n      \"type\" : \"MultiPoseConstraintSolver\",\n      \"value\" : null,\n      \"ext\" : \"Kraken\"\n      },\n    {\n      \"type\" : \"Boolean\",\n      \"value\" : false\n      },\n    {\n"
		+ "      \"type\" : \"Float32\",\n      \"value\" : 1\n      },\n    {\n      \"type\" : \"Mat44[]\",\n      \"value\" : null,\n      \"ext\" : \"Math\"\n      },\n    {\n      \"type\" : \"Mat44[]\",\n      \"value\" : null,\n      \"ext\" : \"Math\"\n      }\n    ]\n  }");
	setAttr ".evalID" 1;
	setAttr -k on ".drawDebug" no;
	setAttr -k on ".rigScale" 1;
	setAttr -s 2 ".constrainers";
	setAttr -k on ".constrainers[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -2 15 0 1;
	setAttr -k on ".constrainers[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -1.2172472745220455 14.410085078396119 10.36227173666145 1;
	setAttr -k on ".constrainers";
	setAttr -s 2 ".constrainees";
createNode decomposeMatrix -n "decomposeMatrix3";
	rename -uid "06DCCFD9-404A-BF02-3517-E1B571761AA5";
	setAttr ".ot" -type "double3" -2 15 0 ;
	setAttr ".os" -type "double3" 1 1 1 ;
createNode decomposeMatrix -n "decomposeMatrix4";
	rename -uid "9327362F-4C5E-F8C3-CF18-06A1D4035131";
	setAttr ".ot" -type "double3" -1.2172472476959229 14.41008472442627 10.362271308898926 ;
	setAttr ".os" -type "double3" 1 1 1 ;
createNode dfgMayaNode -n "MeyesR_YeakfdjsDeformerJointsKLOp";
	rename -uid "176032C5-4651-56EA-DBA8-9FB45E55F597";
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
		"{\n  \"objectType\" : \"Graph\",\n  \"metadata\" : {\n    \"maya_id\" : \"3\"\n    },\n  \"title\" : \"\",\n  \"ports\" : [\n    {\n      \"objectType\" : \"Port\",\n      \"nodePortType\" : \"IO\",\n      \"name\" : \"solver\",\n      \"execPortType\" : \"IO\",\n      \"typeSpec\" : \"MultiPoseConstraintSolver\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"drawDebug\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Boolean\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"rigScale\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Scalar\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"constrainers\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Mat44[]\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"nodePortType\" : \"In\",\n      \"name\" : \"constrainees\",\n"
		+ "      \"execPortType\" : \"Out\",\n      \"typeSpec\" : \"Mat44[]\"\n      }\n    ],\n  \"extDeps\" : {\n    \"Kraken\" : \"*\"\n    },\n  \"nodes\" : [\n    {\n      \"objectType\" : \"Inst\",\n      \"metadata\" : {\n        \"uiGraphPos\" : \"{\\\"x\\\":100.0,\\\"y\\\":100.0}\"\n        },\n      \"name\" : \"MeyesR_YeakfdjsDeformerJointsKLOp\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"solver\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"drawDebug\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"rigScale\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"constrainers\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"constrainees\"\n          }\n        ],\n      \"definition\" : {\n        \"objectType\" : \"Func\",\n        \"title\" : \"MeyesR_YeakfdjsDeformerJointsKLOp\",\n"
		+ "        \"ports\" : [\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"IO\",\n            \"name\" : \"solver\",\n            \"execPortType\" : \"IO\",\n            \"typeSpec\" : \"MultiPoseConstraintSolver\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"Out\",\n            \"name\" : \"drawDebug\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"Boolean\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"Out\",\n            \"name\" : \"rigScale\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"Scalar\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"Out\",\n            \"name\" : \"constrainers\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"Mat44[]\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"In\",\n            \"name\" : \"constrainees\",\n            \"execPortType\" : \"Out\",\n            \"typeSpec\" : \"Mat44[]\"\n"
		+ "            }\n          ],\n        \"extDeps\" : {\n          \"Kraken\" : \"*\"\n          },\n        \"code\" : \"dfgEntry {\n  constrainees.resize(2);\n  if(solver == null)\n    solver = MultiPoseConstraintSolver();\n  solver.solve(\n    drawDebug,\n    rigScale,\n    constrainers,\n    constrainees\n  );\n}\n\"\n        }\n      }\n    ],\n  \"connections\" : {\n    \"solver\" : [\n      \"MeyesR_YeakfdjsDeformerJointsKLOp.solver\"\n      ],\n    \"drawDebug\" : [\n      \"MeyesR_YeakfdjsDeformerJointsKLOp.drawDebug\"\n      ],\n    \"rigScale\" : [\n      \"MeyesR_YeakfdjsDeformerJointsKLOp.rigScale\"\n      ],\n    \"constrainers\" : [\n      \"MeyesR_YeakfdjsDeformerJointsKLOp.constrainers\"\n      ],\n    \"MeyesR_YeakfdjsDeformerJointsKLOp.solver\" : [\n      \"solver\"\n      ],\n    \"MeyesR_YeakfdjsDeformerJointsKLOp.constrainees\" : [\n      \"constrainees\"\n      ]\n    },\n  \"metadata\" : {\n    \"maya_id\" : \"3\"\n    },\n  \"args\" : [\n    {\n      \"type\" : \"MultiPoseConstraintSolver\",\n      \"value\" : null,\n      \"ext\" : \"Kraken\"\n      },\n    {\n      \"type\" : \"Boolean\",\n      \"value\" : false\n"
		+ "      },\n    {\n      \"type\" : \"Float32\",\n      \"value\" : 1\n      },\n    {\n      \"type\" : \"Mat44[]\",\n      \"value\" : null,\n      \"ext\" : \"Math\"\n      },\n    {\n      \"type\" : \"Mat44[]\",\n      \"value\" : null,\n      \"ext\" : \"Math\"\n      }\n    ]\n  }");
	setAttr ".evalID" 1;
	setAttr -k on ".drawDebug" no;
	setAttr -k on ".rigScale" 1;
	setAttr -s 2 ".constrainers";
	setAttr -k on ".constrainers[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -4 15 0 1;
	setAttr -k on ".constrainers[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -3.2172472745220455 14.410085078396119 10.36227173666145 1;
	setAttr -k on ".constrainers";
	setAttr -s 2 ".constrainees";
createNode decomposeMatrix -n "decomposeMatrix5";
	rename -uid "C2605DF9-454F-57EE-5192-0C95C6D40DA6";
	setAttr ".ot" -type "double3" -4 15 0 ;
	setAttr ".os" -type "double3" 1 1 1 ;
createNode decomposeMatrix -n "decomposeMatrix6";
	rename -uid "FE1EBD6E-45B3-10B9-D741-AC84BAC8FD31";
	setAttr ".ot" -type "double3" -3.2172472476959229 14.41008472442627 10.362271308898926 ;
	setAttr ".os" -type "double3" 1 1 1 ;
createNode canvasNode -n "canvasNode2";
	rename -uid "E7CE6DDC-4ED6-CFC4-C8DF-6292705BF1BC";
	addAttr -r false -ci true -k true -sn "up" -ln "up" -at "matrix";
	addAttr -r false -ci true -k true -sn "ik" -ln "ik" -at "matrix";
	addAttr -r false -ci true -k true -sn "drawDebug" -ln "drawDebug" -min 0 -max 1 
		-at "bool";
	addAttr -r false -ci true -k true -sn "rigScale" -ln "rigScale" -at "double";
	addAttr -w false -s false -ci true -sn "result" -ln "result" -at "matrix";
	addAttr -r false -ci true -k true -sn "fk" -ln "fk" -at "matrix";
	addAttr -r false -ci true -k true -sn "Blend" -ln "Blend" -min 0 -max 1 -at "double";
	setAttr ".cch" no;
	setAttr ".ihi" 2;
	setAttr ".nds" 0;
	setAttr ".fzn" no;
	setAttr ".svd" -type "string" (
		"{\n  \"objectType\" : \"Graph\",\n  \"metadata\" : {\n    \"maya_id\" : \"4\"\n    },\n  \"title\" : \"DirectionConstraintSolver\",\n  \"ports\" : [\n    {\n      \"objectType\" : \"Port\",\n      \"nodePortType\" : \"In\",\n      \"name\" : \"result\",\n      \"execPortType\" : \"Out\",\n      \"typeSpec\" : \"Mat44\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"up\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Mat44\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"fk\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Mat44\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"ik\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Mat44\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n"
		+ "      \"nodePortType\" : \"Out\",\n      \"name\" : \"drawDebug\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Boolean\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"metadata\" : {\n        \"uiPersistValue\" : \"true\"\n        },\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"rigScale\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Float32\"\n      },\n    {\n      \"objectType\" : \"Port\",\n      \"nodePortType\" : \"Out\",\n      \"name\" : \"Blend\",\n      \"execPortType\" : \"In\",\n      \"typeSpec\" : \"Scalar\"\n      }\n    ],\n  \"extDeps\" : {},\n  \"presetGUID\" : \"7CA3C89284C11CF21B616C075C007AE4\",\n  \"nodes\" : [\n    {\n      \"objectType\" : \"Inst\",\n      \"metadata\" : {\n        \"uiGraphPos\" : \"{\\\"x\\\":455.251,\\\"y\\\":153.353}\"\n        },\n      \"name\" : \"Translation_2\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"this\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"result\"\n          }\n        ],\n      \"executable\" : \"Fabric.Exts.Math.Mat44.Translation\",\n"
		+ "      \"presetGUID\" : \"35DC8AE364F6509754699978B97928A7\"\n      },\n    {\n      \"objectType\" : \"Inst\",\n      \"metadata\" : {\n        \"uiGraphPos\" : \"{\\\"x\\\":451.635,\\\"y\\\":236.096}\"\n        },\n      \"name\" : \"Translation_3\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"this\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"result\"\n          }\n        ],\n      \"executable\" : \"Fabric.Exts.Math.Mat44.Translation\",\n      \"presetGUID\" : \"35DC8AE364F6509754699978B97928A7\"\n      },\n    {\n      \"objectType\" : \"Inst\",\n      \"metadata\" : {\n        \"uiGraphPos\" : \"{\\\"x\\\":1078.35,\\\"y\\\":394.58}\"\n        },\n      \"name\" : \"Xfo\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"ori\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"tr\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n"
		+ "          \"nodePortType\" : \"In\",\n          \"name\" : \"sc\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"result\"\n          }\n        ],\n      \"executable\" : \"Fabric.Exts.Math.Xfo.Xfo\",\n      \"presetGUID\" : \"A0F6CD63A2069530481F214C62A069AA\"\n      },\n    {\n      \"objectType\" : \"Inst\",\n      \"metadata\" : {\n        \"uiGraphPos\" : \"{\\\"x\\\":1229.82,\\\"y\\\":425.195}\"\n        },\n      \"name\" : \"ToMat44\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"this\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"result\"\n          }\n        ],\n      \"executable\" : \"Fabric.Exts.Math.Xfo.ToMat44\",\n      \"presetGUID\" : \"3EB232DB6FF4BEE162E1D62ABFBE8C3A\"\n      },\n    {\n      \"objectType\" : \"Inst\",\n      \"metadata\" : {\n        \"uiGraphPos\" : \"{\\\"x\\\":808.523,\\\"y\\\":301.924}\"\n        },\n      \"name\" : \"SetFromDirectionAndUpvector\",\n      \"ports\" : [\n"
		+ "        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"direction\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"upvector\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"result\"\n          }\n        ],\n      \"executable\" : \"Fabric.Exts.Math.Quat.SetFromDirectionAndUpvector\",\n      \"presetGUID\" : \"249D3B1274A5895F6E1D8C7DA49E7772\"\n      },\n    {\n      \"objectType\" : \"Inst\",\n      \"metadata\" : {\n        \"uiGraphPos\" : \"{\\\"x\\\":657.0,\\\"y\\\":141.053}\"\n        },\n      \"name\" : \"Sub\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"lhs\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"rhs\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"result\"\n          }\n"
		+ "        ],\n      \"executable\" : \"Fabric.Core.Math.Sub\",\n      \"presetGUID\" : \"F9754B19F43BC017056B8BA291E7B8B4\"\n      },\n    {\n      \"objectType\" : \"Inst\",\n      \"metadata\" : {\n        \"uiGraphPos\" : \"{\\\"x\\\":658.449,\\\"y\\\":243.502}\"\n        },\n      \"name\" : \"Sub_2\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"lhs\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"rhs\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"result\"\n          }\n        ],\n      \"executable\" : \"Fabric.Core.Math.Sub\",\n      \"presetGUID\" : \"F9754B19F43BC017056B8BA291E7B8B4\"\n      },\n    {\n      \"objectType\" : \"Inst\",\n      \"metadata\" : {\n        \"uiGraphPos\" : \"{\\\"x\\\":457.313,\\\"y\\\":316.069}\"\n        },\n      \"name\" : \"Boolean\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"value\"\n"
		+ "          }\n        ],\n      \"executable\" : \"Fabric.Core.Constants.Boolean\",\n      \"presetGUID\" : \"AC57A4CE7AD2AF05FAECFA35F4E8C2F6\"\n      },\n    {\n      \"objectType\" : \"Inst\",\n      \"metadata\" : {\n        \"uiGraphPos\" : \"{\\\"x\\\":460.972,\\\"y\\\":360.468}\"\n        },\n      \"name\" : \"Float32\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"value\"\n          }\n        ],\n      \"executable\" : \"Fabric.Core.Constants.Float32\",\n      \"presetGUID\" : \"E30A52C7E85FC891AF9B748E73406E66\"\n      },\n    {\n      \"objectType\" : \"Inst\",\n      \"metadata\" : {\n        \"uiGraphPos\" : \"{\\\"x\\\":858.478,\\\"y\\\":524.229}\"\n        },\n      \"name\" : \"SphericalLinearInterpolate_1\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"this\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"q2\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n"
		+ "          \"nodePortType\" : \"In\",\n          \"defaultValues\" : {\n            \"Float32\" : 0\n            },\n          \"name\" : \"t\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"result\"\n          }\n        ],\n      \"executable\" : \"Fabric.Exts.Math.Quat.SphericalLinearInterpolate\",\n      \"presetGUID\" : \"8F8A88A5073927972931DF1FB8D01172\"\n      },\n    {\n      \"objectType\" : \"Inst\",\n      \"metadata\" : {\n        \"uiGraphPos\" : \"{\\\"x\\\":71.56,\\\"y\\\":289.936}\"\n        },\n      \"name\" : \"SetFromMat44_1\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"this\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"m\"\n          }\n        ],\n      \"executable\" : \"Fabric.Exts.Math.Xfo.SetFromMat44\",\n      \"presetGUID\" : \"59B1B738E9402F3006B2516B14A43848\"\n      },\n    {\n      \"objectType\" : \"Inst\",\n      \"metadata\" : {\n        \"uiGraphPos\" : \"{\\\"x\\\":257.82,\\\"y\\\":345.033}\"\n"
		+ "        },\n      \"name\" : \"DecomposeXfo_1\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"value\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"ori\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"tr\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"sc\"\n          }\n        ],\n      \"executable\" : \"Fabric.Exts.Math.Xfo.DecomposeXfo\",\n      \"presetGUID\" : \"F1CE36998E153872EE926747BEB0E7A6\"\n      },\n    {\n      \"objectType\" : \"Inst\",\n      \"metadata\" : {\n        \"uiGraphPos\" : \"{\\\"x\\\":898.1180000000001,\\\"y\\\":411.894}\"\n        },\n      \"name\" : \"orientXfo_1\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"defaultValues\" : {\n            \"UInt32\" : 6\n            },\n          \"name\" : \"atAxis\"\n"
		+ "          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"defaultValues\" : {\n            \"UInt32\" : 2\n            },\n          \"name\" : \"upAxis\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"this\"\n          }\n        ],\n      \"definition\" : {\n        \"objectType\" : \"Func\",\n        \"title\" : \"orientXfo\",\n        \"ports\" : [\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"Out\",\n            \"defaultValues\" : {\n              \"UInt32\" : 1\n              },\n            \"name\" : \"atAxis\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"UInt32\"\n            },\n          {\n            \"objectType\" : \"Port\",\n            \"nodePortType\" : \"Out\",\n            \"defaultValues\" : {\n              \"UInt32\" : 2\n              },\n            \"name\" : \"upAxis\",\n            \"execPortType\" : \"In\",\n            \"typeSpec\" : \"UInt32\"\n            },\n          {\n            \"objectType\" : \"Port\",\n"
		+ "            \"nodePortType\" : \"IO\",\n            \"name\" : \"this\",\n            \"execPortType\" : \"IO\",\n            \"typeSpec\" : \"Quat\"\n            }\n          ],\n        \"extDeps\" : {},\n        \"origPresetGUID\" : \"53A2FC56A2BACEC95035D5ED3610B859\",\n        \"code\" : \"// Gotta be a better way\nfunction Vec3 getAxisAsVector(in UInt32 axisIndex)\n{\n  Vec3 vec;\n  switch (axisIndex)\n  {\n    case 0:\n      return Vec3(1.0, 0.0, 0.0);\n    case 1:\n      return Vec3(0.0, 1.0, 0.0);\n    case 2:\n      return Vec3(0.0, 0.0, 1.0);\n    case 3:\n      return Vec3(-1.0, 0.0, 0.0);\n    case 4:\n      return Vec3(0.0, -1.0, 0.0);\n    case 5:\n      return Vec3(0.0, 0.0, -1.0);\n  }\n  report(\\\"OSS_TwoBoneIKSolver:getAxisAsVector() invalid axisIndex\\\");\n  return Vec3(1.0, 0.0, 0.0);\n}\n\nfunction Vec3 getAxis(in Quat ori, in UInt32 axisIndex)\n{\n  switch (axisIndex)\n  {\n    case 0:\n      return ori.getXaxis();\n    case 1:\n      return ori.getYaxis();\n    case 2:\n      return ori.getZaxis();\n    case 3:\n      return ori.getXaxis().negate();\n    case 4:\n"
		+ "      return ori.getYaxis().negate();\n    case 5:\n      return ori.getZaxis().negate();\n  }\n  report(\\\"OSS_TwoBoneIKSolver:getAxis() invalid axisIndex\\\");\n  return ori.getXaxis();\n}\n\n\n// Make this take in a specific aim and upvector later\n// Hard-coded to aim pos +X and use +Z as normal\ndfgEntry {\n  Vec3 atAxisVec = getAxis(this, atAxis).unit();\n  Vec3 upAxisVec = getAxis(this, upAxis).unit();\n  Vec3 normalAxisVec = upAxisVec.cross(atAxisVec).unit();\n  Mat33 mat(atAxisVec, normalAxisVec, upAxisVec);\n  this.setFromMat33(mat.transpose());\n}\n\"\n        }\n      },\n    {\n      \"objectType\" : \"Inst\",\n      \"metadata\" : {\n        \"uiGraphPos\" : \"{\\\"x\\\":611.0,\\\"y\\\":359.0}\"\n        },\n      \"name\" : \"Vec3_1\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"x\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"defaultValues\" : {\n            \"Float32\" : 1\n            },\n          \"name\" : \"y\"\n          },\n"
		+ "        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"z\"\n          },\n        {\n          \"objectType\" : \"InstPort\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"result\"\n          }\n        ],\n      \"executable\" : \"Fabric.Exts.Math.Vec3.Vec3\",\n      \"presetGUID\" : \"A59E49949F21CFCB14B5711D52330BA7\"\n      }\n    ],\n  \"connections\" : {\n    \"up\" : [\n      \"Translation_2.this\"\n      ],\n    \"fk\" : [\n      \"SetFromMat44_1.m\"\n      ],\n    \"ik\" : [\n      \"Translation_3.this\"\n      ],\n    \"drawDebug\" : [\n      \"Boolean.value\"\n      ],\n    \"rigScale\" : [\n      \"Float32.value\"\n      ],\n    \"Blend\" : [\n      \"SphericalLinearInterpolate_1.t\"\n      ],\n    \"Translation_2.result\" : [\n      \"Sub.lhs\"\n      ],\n    \"Translation_3.result\" : [\n      \"Sub_2.lhs\"\n      ],\n    \"Xfo.result\" : [\n      \"ToMat44.this\"\n      ],\n    \"ToMat44.result\" : [\n      \"result\"\n      ],\n    \"SetFromDirectionAndUpvector.result\" : [\n      \"orientXfo_1.this\"\n      ],\n    \"Sub_2.result\" : [\n      \"SetFromDirectionAndUpvector.direction\"\n"
		+ "      ],\n    \"SphericalLinearInterpolate_1.result\" : [\n      \"Xfo.ori\"\n      ],\n    \"SetFromMat44_1.this\" : [\n      \"DecomposeXfo_1.value\"\n      ],\n    \"DecomposeXfo_1.ori\" : [\n      \"SphericalLinearInterpolate_1.q2\"\n      ],\n    \"DecomposeXfo_1.tr\" : [\n      \"Sub.rhs\",\n      \"Sub_2.rhs\",\n      \"Xfo.tr\"\n      ],\n    \"orientXfo_1.this\" : [\n      \"SphericalLinearInterpolate_1.this\"\n      ],\n    \"Vec3_1.result\" : [\n      \"SetFromDirectionAndUpvector.upvector\"\n      ]\n    },\n  \"metadata\" : {\n    \"maya_id\" : \"4\"\n    },\n  \"requiredPresets\" : {\n    \"Fabric.Exts.Math.Mat44.Translation\" : {\n      \"objectType\" : \"Func\",\n      \"metadata\" : {\n        \"uiNodeColor\" : \"{\\n  \\\"r\\\" : 99,\\n  \\\"g\\\" : 129,\\n  \\\"b\\\" : 92\\n  }\",\n        \"uiDocUrl\" : \"http://docs.fabric-engine.com/FabricEngine/2.0.1/HTML/KLExtensionsGuide/Math/Mat44.html\",\n        \"uiTooltip\" : \"Returns the translation components of\\nthis matrix as a Vec3\\n\\n Supported by Mat44\"\n        },\n      \"title\" : \"Translation\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"Port\",\n"
		+ "          \"metadata\" : {\n            \"uiColor\" : \"{\\n  \\\"r\\\" : 249,\\n  \\\"g\\\" : 157,\\n  \\\"b\\\" : 28\\n  }\"\n            },\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"this\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Mat44\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {\n            \"uiColor\" : \"{\\n  \\\"r\\\" : 255,\\n  \\\"g\\\" : 242,\\n  \\\"b\\\" : 0\\n  }\"\n            },\n          \"nodePortType\" : \"In\",\n          \"name\" : \"result\",\n          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"Vec3\"\n          }\n        ],\n      \"extDeps\" : {\n        \"Math\" : \"*\"\n        },\n      \"presetGUID\" : \"35DC8AE364F6509754699978B97928A7\",\n      \"code\" : \"require Math;\n\ndfgEntry {\n  result = this.translation();\n}\n\"\n      },\n    \"Fabric.Exts.Math.Xfo.Xfo\" : {\n      \"objectType\" : \"Func\",\n      \"metadata\" : {\n        \"uiNodeColor\" : \"{\\n  \\\"r\\\" : 99,\\n  \\\"g\\\" : 129,\\n  \\\"b\\\" : 92\\n  }\",\n        \"uiDocUrl\" : \"http://docs.fabric-engine.com/FabricEngine/2.0.1/HTML/KLExtensionsGuide/Math/Xfo.html\",\n"
		+ "        \"uiTooltip\" : \"Constructor from the orientation, translation and scaling\\n\\n Supported by Xfo\"\n        },\n      \"title\" : \"Xfo\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {\n            \"uiColor\" : \"{\\n  \\\"r\\\" : 0,\\n  \\\"g\\\" : 191,\\n  \\\"b\\\" : 232\\n  }\"\n            },\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"ori\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Quat\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {\n            \"uiColor\" : \"{\\n  \\\"r\\\" : 255,\\n  \\\"g\\\" : 242,\\n  \\\"b\\\" : 0\\n  }\"\n            },\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"tr\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Vec3\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {\n            \"uiColor\" : \"{\\n  \\\"r\\\" : 255,\\n  \\\"g\\\" : 242,\\n  \\\"b\\\" : 0\\n  }\"\n            },\n          \"nodePortType\" : \"Out\",\n          \"defaultValues\" : {\n            \"Vec3\" : {\n              \"x\" : 1,\n              \"y\" : 1,\n"
		+ "              \"z\" : 1\n              }\n            },\n          \"name\" : \"sc\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Vec3\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {\n            \"uiColor\" : \"{\\n  \\\"r\\\" : 249,\\n  \\\"g\\\" : 157,\\n  \\\"b\\\" : 28\\n  }\"\n            },\n          \"nodePortType\" : \"In\",\n          \"name\" : \"result\",\n          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"Xfo\"\n          }\n        ],\n      \"extDeps\" : {\n        \"Math\" : \"*\"\n        },\n      \"presetGUID\" : \"A0F6CD63A2069530481F214C62A069AA\",\n      \"code\" : \"require Math;\n\ndfgEntry {\n  result = Xfo(ori, tr, sc);\n}\n\"\n      },\n    \"Fabric.Exts.Math.Xfo.ToMat44\" : {\n      \"objectType\" : \"Func\",\n      \"metadata\" : {\n        \"uiNodeColor\" : \"{\\n  \\\"r\\\" : 99,\\n  \\\"g\\\" : 129,\\n  \\\"b\\\" : 92\\n  }\",\n        \"uiDocUrl\" : \"http://docs.fabric-engine.com/FabricEngine/2.0.1/HTML/KLExtensionsGuide/Math/Xfo.html\",\n        \"uiTooltip\" : \"Returns this xfo as a Mat44\\n\\n Supported by Xfo\"\n        },\n      \"title\" : \"ToMat44\",\n"
		+ "      \"ports\" : [\n        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {\n            \"uiColor\" : \"{\\n  \\\"r\\\" : 249,\\n  \\\"g\\\" : 157,\\n  \\\"b\\\" : 28\\n  }\"\n            },\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"this\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Xfo\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {\n            \"uiColor\" : \"{\\n  \\\"r\\\" : 249,\\n  \\\"g\\\" : 157,\\n  \\\"b\\\" : 28\\n  }\"\n            },\n          \"nodePortType\" : \"In\",\n          \"name\" : \"result\",\n          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"Mat44\"\n          }\n        ],\n      \"extDeps\" : {\n        \"Math\" : \"*\"\n        },\n      \"presetGUID\" : \"3EB232DB6FF4BEE162E1D62ABFBE8C3A\",\n      \"code\" : \"require Math;\n\ndfgEntry {\n  result = this.toMat44();\n}\n\"\n      },\n    \"Fabric.Exts.Math.Quat.SetFromDirectionAndUpvector\" : {\n      \"objectType\" : \"Func\",\n      \"metadata\" : {\n        \"uiNodeColor\" : \"{\\n  \\\"r\\\" : 99,\\n  \\\"g\\\" : 129,\\n  \\\"b\\\" : 92\\n  }\",\n        \"uiDocUrl\" : \"http://docs.fabric-engine.com/FabricEngine/2.0.1/HTML/KLExtensionsGuide/Math/Quat.html\",\n"
		+ "        \"uiTooltip\" : \"Set the quat to represent the direction as the Z axis\\nand the upvector pointing along the XY plane.\\n\\n Supported by Quat\"\n        },\n      \"title\" : \"SetFromDirectionAndUpvector\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {\n            \"uiColor\" : \"{\\n  \\\"r\\\" : 255,\\n  \\\"g\\\" : 242,\\n  \\\"b\\\" : 0\\n  }\"\n            },\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"direction\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Vec3\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {\n            \"uiColor\" : \"{\\n  \\\"r\\\" : 255,\\n  \\\"g\\\" : 242,\\n  \\\"b\\\" : 0\\n  }\"\n            },\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"upvector\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Vec3\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {\n            \"uiColor\" : \"{\\n  \\\"r\\\" : 0,\\n  \\\"g\\\" : 191,\\n  \\\"b\\\" : 232\\n  }\"\n            },\n          \"nodePortType\" : \"In\",\n          \"name\" : \"result\",\n"
		+ "          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"Quat\"\n          }\n        ],\n      \"extDeps\" : {\n        \"Math\" : \"*\"\n        },\n      \"presetGUID\" : \"249D3B1274A5895F6E1D8C7DA49E7772\",\n      \"code\" : \"require Math;\n\ndfgEntry {\n  result.setFromDirectionAndUpvector(direction, upvector);\n}\n\"\n      },\n    \"Fabric.Core.Math.Sub\" : {\n      \"objectType\" : \"Func\",\n      \"title\" : \"Sub\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"lhs\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"$TYPE$\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"rhs\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"$TYPE$\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"In\",\n          \"name\" : \"result\",\n          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"$TYPE$\"\n          }\n        ],\n      \"extDeps\" : {},\n      \"presetGUID\" : \"F9754B19F43BC017056B8BA291E7B8B4\",\n"
		+ "      \"code\" : \"\ndfgEntry {\n\tresult = lhs - rhs;\n}\n\"\n      },\n    \"Fabric.Core.Constants.Boolean\" : {\n      \"objectType\" : \"Func\",\n      \"metadata\" : {\n        \"uiAlwaysShowDaisyChainPorts\" : \"true\"\n        },\n      \"title\" : \"Boolean\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"value\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Boolean\"\n          }\n        ],\n      \"extDeps\" : {},\n      \"presetGUID\" : \"AC57A4CE7AD2AF05FAECFA35F4E8C2F6\",\n      \"code\" : \"dfgEntry {\n}\n\"\n      },\n    \"Fabric.Core.Constants.Float32\" : {\n      \"objectType\" : \"Func\",\n      \"metadata\" : {\n        \"uiAlwaysShowDaisyChainPorts\" : \"true\"\n        },\n      \"title\" : \"Float32\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"value\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Float32\"\n          }\n        ],\n      \"extDeps\" : {},\n      \"presetGUID\" : \"E30A52C7E85FC891AF9B748E73406E66\",\n"
		+ "      \"code\" : \"dfgEntry {\n}\n\"\n      },\n    \"Fabric.Exts.Math.Quat.SphericalLinearInterpolate\" : {\n      \"objectType\" : \"Func\",\n      \"metadata\" : {\n        \"uiNodeColor\" : \"{\\n  \\\"r\\\" : 99,\\n  \\\"g\\\" : 129,\\n  \\\"b\\\" : 92\\n  }\",\n        \"uiDocUrl\" : \"http://docs.fabric-engine.com/FabricEngine/2.0.1/HTML/KLExtensionsGuide/Math/Quat.html\",\n        \"uiTooltip\" : \"interpolates two quaternions spherically (slerp)\\ngiven a scalar blend value (0.0 to 1.0).\\n\\n Supported by Quat\"\n        },\n      \"title\" : \"SphericalLinearInterpolate\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {\n            \"uiColor\" : \"{\\n  \\\"r\\\" : 0,\\n  \\\"g\\\" : 191,\\n  \\\"b\\\" : 232\\n  }\"\n            },\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"this\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Quat\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {\n            \"uiColor\" : \"{\\n  \\\"r\\\" : 0,\\n  \\\"g\\\" : 191,\\n  \\\"b\\\" : 232\\n  }\"\n            },\n          \"nodePortType\" : \"Out\",\n"
		+ "          \"name\" : \"q2\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Quat\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"t\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Scalar\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {\n            \"uiColor\" : \"{\\n  \\\"r\\\" : 0,\\n  \\\"g\\\" : 191,\\n  \\\"b\\\" : 232\\n  }\"\n            },\n          \"nodePortType\" : \"In\",\n          \"name\" : \"result\",\n          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"Quat\"\n          }\n        ],\n      \"extDeps\" : {\n        \"Math\" : \"*\"\n        },\n      \"presetGUID\" : \"8F8A88A5073927972931DF1FB8D01172\",\n      \"code\" : \"require Math;\n\ndfgEntry {\n  result = this.sphericalLinearInterpolate(q2, t);\n}\n\"\n      },\n    \"Fabric.Exts.Math.Xfo.SetFromMat44\" : {\n      \"objectType\" : \"Func\",\n      \"metadata\" : {\n        \"uiNodeColor\" : \"{\\n  \\\"r\\\" : 99,\\n  \\\"g\\\" : 129,\\n  \\\"b\\\" : 92\\n  }\",\n        \"uiDocUrl\" : \"http://docs.fabric-engine.com/FabricEngine/2.0.1/HTML/KLExtensionsGuide/Math/Xfo.html\",\n"
		+ "        \"uiTooltip\" : \"Sets this transform from a given Mat44\\n\\n Supported by Xfo\"\n        },\n      \"title\" : \"SetFromMat44\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {\n            \"uiColor\" : \"{\\n  \\\"r\\\" : 249,\\n  \\\"g\\\" : 157,\\n  \\\"b\\\" : 28\\n  }\"\n            },\n          \"nodePortType\" : \"IO\",\n          \"name\" : \"this\",\n          \"execPortType\" : \"IO\",\n          \"typeSpec\" : \"Xfo\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {\n            \"uiColor\" : \"{\\n  \\\"r\\\" : 249,\\n  \\\"g\\\" : 157,\\n  \\\"b\\\" : 28\\n  }\"\n            },\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"m\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Mat44\"\n          }\n        ],\n      \"extDeps\" : {\n        \"Math\" : \"*\"\n        },\n      \"presetGUID\" : \"59B1B738E9402F3006B2516B14A43848\",\n      \"code\" : \"require Math;\n\ndfgEntry {\n  this.setFromMat44(m);\n}\n\"\n      },\n    \"Fabric.Exts.Math.Xfo.DecomposeXfo\" : {\n      \"objectType\" : \"Func\",\n      \"metadata\" : {\n"
		+ "        \"uiNodeColor\" : \"{\\n  \\\"r\\\" : 99,\\n  \\\"g\\\" : 129,\\n  \\\"b\\\" : 92\\n  }\",\n        \"uiDocUrl\" : \"http://docs.fabric-engine.com/FabricEngine/2.0.1/HTML/KLExtensionsGuide/Math/Xfo.html\"\n        },\n      \"title\" : \"Xfo ->\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {\n            \"uiColor\" : \"{\\n  \\\"r\\\" : 249,\\n  \\\"g\\\" : 157,\\n  \\\"b\\\" : 28\\n  }\"\n            },\n          \"nodePortType\" : \"Out\",\n          \"defaultValues\" : {\n            \"Xfo\" : {\n              \"ori\" : {\n                \"v\" : {\n                  \"x\" : 0,\n                  \"y\" : 0,\n                  \"z\" : 0\n                  },\n                \"w\" : 1\n                },\n              \"tr\" : {\n                \"x\" : 0,\n                \"y\" : 0,\n                \"z\" : 0\n                },\n              \"sc\" : {\n                \"x\" : 1,\n                \"y\" : 1,\n                \"z\" : 1\n                }\n              }\n            },\n          \"name\" : \"value\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Xfo\"\n"
		+ "          },\n        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {\n            \"uiColor\" : \"{\\n  \\\"r\\\" : 0,\\n  \\\"g\\\" : 191,\\n  \\\"b\\\" : 232\\n  }\"\n            },\n          \"nodePortType\" : \"In\",\n          \"name\" : \"ori\",\n          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"Quat\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {\n            \"uiColor\" : \"{\\n  \\\"r\\\" : 255,\\n  \\\"g\\\" : 242,\\n  \\\"b\\\" : 0\\n  }\"\n            },\n          \"nodePortType\" : \"In\",\n          \"name\" : \"tr\",\n          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"Vec3\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {\n            \"uiColor\" : \"{\\n  \\\"r\\\" : 255,\\n  \\\"g\\\" : 242,\\n  \\\"b\\\" : 0\\n  }\"\n            },\n          \"nodePortType\" : \"In\",\n          \"name\" : \"sc\",\n          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"Vec3\"\n          }\n        ],\n      \"extDeps\" : {\n        \"Math\" : \"*\"\n        },\n      \"presetGUID\" : \"F1CE36998E153872EE926747BEB0E7A6\",\n      \"code\" : \"require Math;\n"
		+ "dfgEntry {\n  ori = value.ori;\n  tr = value.tr;\n  sc = value.sc;\n}\n\"\n      },\n    \"Fabric.Exts.Math.Vec3.Vec3\" : {\n      \"objectType\" : \"Func\",\n      \"metadata\" : {\n        \"uiNodeColor\" : \"{\\n  \\\"r\\\" : 99,\\n  \\\"g\\\" : 129,\\n  \\\"b\\\" : 92\\n  }\",\n        \"uiDocUrl\" : \"http://docs.fabric-engine.com/FabricEngine/2.0.1/HTML/KLExtensionsGuide/Math/Vec3.html\",\n        \"uiTooltip\" : \"Constructor from scalar components\\n\\n Supported by Vec3\"\n        },\n      \"title\" : \"Vec3\",\n      \"ports\" : [\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"x\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Scalar\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"y\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Scalar\"\n          },\n        {\n          \"objectType\" : \"Port\",\n          \"nodePortType\" : \"Out\",\n          \"name\" : \"z\",\n          \"execPortType\" : \"In\",\n          \"typeSpec\" : \"Scalar\"\n          },\n"
		+ "        {\n          \"objectType\" : \"Port\",\n          \"metadata\" : {\n            \"uiColor\" : \"{\\n  \\\"r\\\" : 255,\\n  \\\"g\\\" : 242,\\n  \\\"b\\\" : 0\\n  }\"\n            },\n          \"nodePortType\" : \"In\",\n          \"name\" : \"result\",\n          \"execPortType\" : \"Out\",\n          \"typeSpec\" : \"Vec3\"\n          }\n        ],\n      \"extDeps\" : {\n        \"Math\" : \"*\"\n        },\n      \"presetGUID\" : \"A59E49949F21CFCB14B5711D52330BA7\",\n      \"code\" : \"require Math;\n\ndfgEntry {\n  result = Vec3(x, y, z);\n}\n\"\n      }\n    },\n  \"args\" : [\n    {\n      \"type\" : \"Mat44\",\n      \"value\" : null,\n      \"ext\" : \"Math\"\n      },\n    {\n      \"type\" : \"Mat44\",\n      \"value\" : {\n        \"row0\" : {\n          \"x\" : 1,\n          \"y\" : 0,\n          \"z\" : 0,\n          \"t\" : 0\n          },\n        \"row1\" : {\n          \"x\" : 0,\n          \"y\" : 1,\n          \"z\" : 0,\n          \"t\" : 0\n          },\n        \"row2\" : {\n          \"x\" : 0,\n          \"y\" : 0,\n          \"z\" : 1,\n          \"t\" : 0\n          },\n        \"row3\" : {\n          \"x\" : 0,\n          \"y\" : 0,\n"
		+ "          \"z\" : 0,\n          \"t\" : 1\n          }\n        },\n      \"ext\" : \"Math\"\n      },\n    {\n      \"type\" : \"Mat44\",\n      \"value\" : {\n        \"row0\" : {\n          \"x\" : 0.9064783453941345,\n          \"y\" : -0.2092249691486359,\n          \"z\" : -0.366772323846817,\n          \"t\" : 2\n          },\n        \"row1\" : {\n          \"x\" : 0.06181967258453369,\n          \"y\" : 0.9250086545944214,\n          \"z\" : -0.3748829960823059,\n          \"t\" : 15\n          },\n        \"row2\" : {\n          \"x\" : 0.4177024960517883,\n          \"y\" : 0.3171495795249939,\n          \"z\" : 0.8514345288276672,\n          \"t\" : 1.950049044987303e-16\n          },\n        \"row3\" : {\n          \"x\" : 0,\n          \"y\" : 0,\n          \"z\" : 0,\n          \"t\" : 1\n          }\n        },\n      \"ext\" : \"Math\"\n      },\n    {\n      \"type\" : \"Mat44\",\n      \"value\" : {\n        \"row0\" : {\n          \"x\" : 0.8899773955345154,\n          \"y\" : -0.02677180245518684,\n          \"z\" : 0.4552180469036102,\n          \"t\" : 7.334933280944824\n          },\n        \"row1\" : {\n"
		+ "          \"x\" : 0.05480358749628067,\n          \"y\" : 0.9973189830780029,\n          \"z\" : -0.04849088937044144,\n          \"t\" : 13.92517566680908\n          },\n        \"row2\" : {\n          \"x\" : -0.4526994228363037,\n          \"y\" : 0.06810338050127029,\n          \"z\" : 0.8890585899353027,\n          \"t\" : 9.252857208251953\n          },\n        \"row3\" : {\n          \"x\" : 0,\n          \"y\" : 0,\n          \"z\" : 0,\n          \"t\" : 1\n          }\n        },\n      \"ext\" : \"Math\"\n      },\n    {\n      \"type\" : \"Boolean\",\n      \"value\" : false\n      },\n    {\n      \"type\" : \"Float32\",\n      \"value\" : 0\n      },\n    {\n      \"type\" : \"Float32\",\n      \"value\" : null\n      }\n    ]\n  }");
	setAttr ".evalID" 1074;
	setAttr -k on ".up" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr -k on ".ik" -type "matrix" 0.88997742022344106 0.054803587717456581 -0.45269941270750902 0
		 -0.026771802756216302 0.99731900630698034 0.068103379035401271 0 0.45521803794402826 -0.048490890197565202 0.88905858721359687 0
		 7.3349334925372816 13.925176020778935 9.252857636014479 1;
	setAttr -k on ".drawDebug" no;
	setAttr -k on ".rigScale" 0;
	setAttr -k on ".fk" -type "matrix" 0.90647834539413463 0.061819672584533705 0.41770249605178816 0
		 -0.20922496851886724 0.92500865463737025 0.31714957981518926 0 -0.36677233390398778 -0.37488301096607207 0.85143451794208191 0
		 2 15 1.9500490449873029e-016 1;
	setAttr -k on ".Blend" 0;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "BE0BE589-47EA-BC37-3FF9-3F9FE1F3834C";
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
		+ "            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n"
		+ "                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -rendererName \"vp2Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n"
		+ "                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n"
		+ "                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 0\n                -height 777\n                -sceneRenderFilter 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n            modelEditor -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\t}\n\t} else {\n"
		+ "\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n"
		+ "            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n"
		+ "            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 0\n            -height 777\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n"
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
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperShadePanel\" -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"nodeEditorPanel\" -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n"
		+ "                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -defaultPinnedState 0\n                -additiveGraphingMode 1\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -activeTab 0\n                -editorMode \"default\" \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n"
		+ "                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -defaultPinnedState 0\n                -additiveGraphingMode 1\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -activeTab 0\n                -editorMode \"default\" \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\tif ($useSceneConfig) {\n\t\tscriptedPanel -e -to $panelName;\n"
		+ "\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"vertical2\\\" -ps 1 97 100 -ps 2 1 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Outliner\")) \n\t\t\t\t\t\"outlinerPanel\"\n\t\t\t\t\t\"$panelName = `outlinerPanel -unParent -l (localizedPanelLabel(\\\"Outliner\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\noutlinerEditor -e \\n    -docTag \\\"isolOutln_fromSeln\\\" \\n    -showShapes 0\\n    -showReferenceNodes 1\\n    -showReferenceMembers 1\\n    -showAttributes 0\\n    -showConnected 0\\n    -showAnimCurvesOnly 0\\n    -showMuteInfo 0\\n    -organizeByLayer 1\\n    -showAnimLayerWeight 1\\n    -autoExpandLayers 1\\n    -autoExpand 0\\n    -showDagOnly 0\\n    -showAssets 1\\n    -showContainedOnly 1\\n    -showPublishedAsConnected 0\\n    -showContainerContents 1\\n    -ignoreDagHierarchy 0\\n    -expandConnections 0\\n    -showUpstreamCurves 1\\n    -showUnitlessCurves 1\\n    -showCompounds 1\\n    -showLeafs 1\\n    -showNumericAttrsOnly 0\\n    -highlightActive 1\\n    -autoSelectNewObjects 0\\n    -doNotSelectNewObjects 0\\n    -dropIsParent 1\\n    -transmitFilters 0\\n    -setFilter \\\"defaultSetFilter\\\" \\n    -showSetMembers 1\\n    -allowMultiSelection 1\\n    -alwaysToggleSelect 0\\n    -directSelect 0\\n    -displayMode \\\"DAG\\\" \\n    -expandObjects 0\\n    -setsIgnoreFilters 1\\n    -containersIgnoreFilters 0\\n    -editAttrName 0\\n    -showAttrValues 0\\n    -highlightSecondary 0\\n    -showUVAttrsOnly 0\\n    -showTextureNodesOnly 0\\n    -attrAlphaOrder \\\"default\\\" \\n    -animLayerFilterOptions \\\"allAffecting\\\" \\n    -sortOrder \\\"none\\\" \\n    -longNames 0\\n    -niceNames 1\\n    -showNamespace 1\\n    -showPinIcons 0\\n    -mapMotionTrails 0\\n    -ignoreHiddenAttribute 0\\n    -ignoreOutlinerColor 0\\n    $editorName\"\n"
		+ "\t\t\t\t\t\"outlinerPanel -edit -l (localizedPanelLabel(\\\"Outliner\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\noutlinerEditor -e \\n    -docTag \\\"isolOutln_fromSeln\\\" \\n    -showShapes 0\\n    -showReferenceNodes 1\\n    -showReferenceMembers 1\\n    -showAttributes 0\\n    -showConnected 0\\n    -showAnimCurvesOnly 0\\n    -showMuteInfo 0\\n    -organizeByLayer 1\\n    -showAnimLayerWeight 1\\n    -autoExpandLayers 1\\n    -autoExpand 0\\n    -showDagOnly 0\\n    -showAssets 1\\n    -showContainedOnly 1\\n    -showPublishedAsConnected 0\\n    -showContainerContents 1\\n    -ignoreDagHierarchy 0\\n    -expandConnections 0\\n    -showUpstreamCurves 1\\n    -showUnitlessCurves 1\\n    -showCompounds 1\\n    -showLeafs 1\\n    -showNumericAttrsOnly 0\\n    -highlightActive 1\\n    -autoSelectNewObjects 0\\n    -doNotSelectNewObjects 0\\n    -dropIsParent 1\\n    -transmitFilters 0\\n    -setFilter \\\"defaultSetFilter\\\" \\n    -showSetMembers 1\\n    -allowMultiSelection 1\\n    -alwaysToggleSelect 0\\n    -directSelect 0\\n    -displayMode \\\"DAG\\\" \\n    -expandObjects 0\\n    -setsIgnoreFilters 1\\n    -containersIgnoreFilters 0\\n    -editAttrName 0\\n    -showAttrValues 0\\n    -highlightSecondary 0\\n    -showUVAttrsOnly 0\\n    -showTextureNodesOnly 0\\n    -attrAlphaOrder \\\"default\\\" \\n    -animLayerFilterOptions \\\"allAffecting\\\" \\n    -sortOrder \\\"none\\\" \\n    -longNames 0\\n    -niceNames 1\\n    -showNamespace 1\\n    -showPinIcons 0\\n    -mapMotionTrails 0\\n    -ignoreHiddenAttribute 0\\n    -ignoreOutlinerColor 0\\n    $editorName\"\n"
		+ "\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 0\\n    -height 777\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 0\\n    -height 777\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        setFocus `paneLayout -q -p1 $gMainPane`;\n        sceneUIReplacement -deleteRemaining;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "A37CEFAA-4DB7-D8A7-5943-18A29D7B14DB";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode polyCube -n "polyCube1";
	rename -uid "E5726A59-4B7F-B45D-D7FD-FDAC47DDEA01";
	setAttr ".cuv" 4;
createNode decomposeMatrix -n "decomposeMatrix7";
	rename -uid "5F1B3BBF-44DA-642B-345A-93AAEA30A4EB";
	setAttr ".ot" -type "double3" 2 15 1.9500490449873029e-016 ;
	setAttr ".or" -type "double3" 5.7464783624639253 29.966531640362554 1.2319008504750235e-007 ;
	setAttr ".os" -type "double3" 1.0000000106618239 0.99999999833087561 1.000000007809412 ;
	setAttr ".osh" -type "double3" -1.0008692565063542e-008 -1.0717202319614708e-008 
		6.4757313727449348e-009 ;
	setAttr ".oqx" 0.048422237444818161;
	setAttr ".oqy" 0.2582119071145545;
	setAttr ".oqz" -0.012959542702733777;
	setAttr ".oqw" 0.96478699628365561;
createNode lambert -n "lambert2";
	rename -uid "CB37DE61-46DD-4655-D87F-80A661456C34";
	setAttr ".c" -type "float3" 0.5 0 0 ;
createNode shadingEngine -n "lambert2SG";
	rename -uid "BFB3DC38-4022-DB31-3C0A-E18DC28279C5";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo1";
	rename -uid "5CE45F9B-4866-E0A3-9DA9-4CB554BF1291";
createNode groupId -n "groupId1";
	rename -uid "BEEB89EF-48EA-2A37-F573-51943F17E57E";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts1";
	rename -uid "8B8B071D-45B2-3D96-6E55-13B38B604F89";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "f[1:4]";
	setAttr ".irc" -type "componentList" 2 "f[0]" "f[5]";
createNode groupId -n "groupId2";
	rename -uid "ECDAE419-486E-287A-370B-DEBC2A9CFF99";
	setAttr ".ihi" 0;
createNode groupId -n "groupId3";
	rename -uid "F9A8757B-4968-D62A-D91A-71B758871C58";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts2";
	rename -uid "4DECC7D0-4902-0D3D-8247-F4AA45090478";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "f[0]";
createNode lambert -n "lambert3";
	rename -uid "3B4A0198-4D5B-E06C-4D6B-62A8800EE815";
	setAttr ".c" -type "float3" 1 1 0 ;
createNode shadingEngine -n "lambert3SG";
	rename -uid "B2E1B04E-4823-6DC2-F9E3-91A0B6309A8F";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo2";
	rename -uid "B94C4818-4C41-1F3D-4744-7C825F9D07B7";
createNode groupId -n "groupId4";
	rename -uid "75020CD2-499D-F95B-E70B-3781ACA01E4F";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts3";
	rename -uid "E6C9989C-4B41-09F0-1874-B89450DD8065";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "f[5]";
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "218C5428-48F6-8CCB-E975-9F9381DFBD2E";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -485.71426641373489 -171.42856461661233 ;
	setAttr ".tgi[0].vh" -type "double2" 464.28569583665836 177.38094533246689 ;
	setAttr -s 4 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" 1.4285714626312256;
	setAttr ".tgi[0].ni[0].y" -1.4285714626312256;
	setAttr ".tgi[0].ni[0].nvs" 1923;
	setAttr ".tgi[0].ni[1].x" 262.85714721679687;
	setAttr ".tgi[0].ni[1].y" -70;
	setAttr ".tgi[0].ni[1].nvs" 1923;
	setAttr ".tgi[0].ni[2].x" 1.4285714626312256;
	setAttr ".tgi[0].ni[2].y" -1.4285714626312256;
	setAttr ".tgi[0].ni[2].nvs" 1923;
	setAttr ".tgi[0].ni[3].x" 262.85714721679687;
	setAttr ".tgi[0].ni[3].y" -70;
	setAttr ".tgi[0].ni[3].nvs" 1923;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "7E0FA673-46CC-5062-7B24-CB81D4D8D203";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -254.28769682997972 -674.97588298885773 ;
	setAttr ".tgi[0].vh" -type "double2" 1432.590679639733 568.17496567887849 ;
	setAttr -s 13 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" 1.4285714626312256;
	setAttr ".tgi[0].ni[0].y" -98.571426391601563;
	setAttr ".tgi[0].ni[0].nvs" 18304;
	setAttr ".tgi[0].ni[1].x" 490.07418823242187;
	setAttr ".tgi[0].ni[1].y" -329.35733032226562;
	setAttr ".tgi[0].ni[1].nvs" 18304;
	setAttr ".tgi[0].ni[2].x" 895.74853515625;
	setAttr ".tgi[0].ni[2].y" 289.9808349609375;
	setAttr ".tgi[0].ni[2].nvs" 18306;
	setAttr ".tgi[0].ni[3].x" 176.2523193359375;
	setAttr ".tgi[0].ni[3].y" 341.4373779296875;
	setAttr ".tgi[0].ni[3].nvs" 18306;
	setAttr ".tgi[0].ni[4].x" 516.81103515625;
	setAttr ".tgi[0].ni[4].y" 257.9530029296875;
	setAttr ".tgi[0].ni[4].nvs" 18306;
	setAttr ".tgi[0].ni[5].x" -202.96647644042969;
	setAttr ".tgi[0].ni[5].y" 266.3114013671875;
	setAttr ".tgi[0].ni[5].nvs" 18304;
	setAttr ".tgi[0].ni[6].x" 1124.2857666015625;
	setAttr ".tgi[0].ni[6].y" -380;
	setAttr ".tgi[0].ni[6].nvs" 18304;
	setAttr ".tgi[0].ni[7].x" -189.05259704589844;
	setAttr ".tgi[0].ni[7].y" 81.877685546875;
	setAttr ".tgi[0].ni[7].nvs" 18304;
	setAttr ".tgi[0].ni[8].x" 1721.4285888671875;
	setAttr ".tgi[0].ni[8].y" -400;
	setAttr ".tgi[0].ni[8].nvs" 18304;
	setAttr ".tgi[0].ni[9].x" 1982.857177734375;
	setAttr ".tgi[0].ni[9].y" -400;
	setAttr ".tgi[0].ni[9].nvs" 18304;
	setAttr ".tgi[0].ni[10].x" 1721.4285888671875;
	setAttr ".tgi[0].ni[10].y" -400;
	setAttr ".tgi[0].ni[10].nvs" 18304;
	setAttr ".tgi[0].ni[11].x" 1982.857177734375;
	setAttr ".tgi[0].ni[11].y" -400;
	setAttr ".tgi[0].ni[11].nvs" 18304;
	setAttr ".tgi[0].ni[12].x" 1124.2857666015625;
	setAttr ".tgi[0].ni[12].y" -187.14285278320312;
	setAttr ".tgi[0].ni[12].nvs" 18304;
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -s 4 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 6 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr -s 2 ".dsm";
	setAttr ".ro" yes;
	setAttr -s 2 ".gn";
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
connectAttr "decomposeMatrix7.or" "pCube1.r";
connectAttr "decomposeMatrix7.os" "pCube1.s";
connectAttr "decomposeMatrix7.ot" "pCube1.t";
connectAttr "groupId1.id" "pCubeShape1.iog.og[0].gid";
connectAttr ":initialShadingGroup.mwc" "pCubeShape1.iog.og[0].gco";
connectAttr "groupId3.id" "pCubeShape1.iog.og[1].gid";
connectAttr "lambert2SG.mwc" "pCubeShape1.iog.og[1].gco";
connectAttr "groupId4.id" "pCubeShape1.iog.og[2].gid";
connectAttr "lambert3SG.mwc" "pCubeShape1.iog.og[2].gco";
connectAttr "groupParts3.og" "pCubeShape1.i";
connectAttr "groupId2.id" "pCubeShape1.ciog.cog[0].cgid";
connectAttr "decomposeMatrix1.or" "M_L_Eye_fK_def.r";
connectAttr "decomposeMatrix1.os" "M_L_Eye_fK_def.s";
connectAttr "decomposeMatrix1.ot" "M_L_Eye_fK_def.t";
connectAttr "decomposeMatrix2.or" "M_L_Eye_ik_def.r";
connectAttr "decomposeMatrix2.os" "M_L_Eye_ik_def.s";
connectAttr "decomposeMatrix2.ot" "M_L_Eye_ik_def.t";
connectAttr "decomposeMatrix3.or" "M_R_Eye_fK_def.r";
connectAttr "decomposeMatrix3.os" "M_R_Eye_fK_def.s";
connectAttr "decomposeMatrix3.ot" "M_R_Eye_fK_def.t";
connectAttr "decomposeMatrix4.or" "M_R_Eye_ik_def.r";
connectAttr "decomposeMatrix4.os" "M_R_Eye_ik_def.s";
connectAttr "decomposeMatrix4.ot" "M_R_Eye_ik_def.t";
connectAttr "decomposeMatrix5.or" "M_R_Yeakfdjs_fK_def.r";
connectAttr "decomposeMatrix5.os" "M_R_Yeakfdjs_fK_def.s";
connectAttr "decomposeMatrix5.ot" "M_R_Yeakfdjs_fK_def.t";
connectAttr "decomposeMatrix6.or" "M_R_Yeakfdjs_ik_def.r";
connectAttr "decomposeMatrix6.os" "M_R_Yeakfdjs_ik_def.s";
connectAttr "decomposeMatrix6.ot" "M_R_Yeakfdjs_ik_def.t";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert2SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert3SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert2SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert3SG.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "M_inputs_hrc.drawDebug" "MeyesL_EyeDeformerJointsKLOp.drawDebug";
connectAttr "M_inputs_hrc.rigScale" "MeyesL_EyeDeformerJointsKLOp.rigScale";
connectAttr "M_L_Eye_fK_an.wm" "MeyesL_EyeDeformerJointsKLOp.constrainers[0]";
connectAttr "M_L_Eye_ik_an.wm" "MeyesL_EyeDeformerJointsKLOp.constrainers[1]";
connectAttr "MeyesL_EyeDeformerJointsKLOp.constrainees[0]" "decomposeMatrix1.imat"
		;
connectAttr "MeyesL_EyeDeformerJointsKLOp.constrainees[1]" "decomposeMatrix2.imat"
		;
connectAttr "M_inputs_hrc.drawDebug" "MeyesR_EyeDeformerJointsKLOp.drawDebug";
connectAttr "M_inputs_hrc.rigScale" "MeyesR_EyeDeformerJointsKLOp.rigScale";
connectAttr "M_R_Eye_fK_an.wm" "MeyesR_EyeDeformerJointsKLOp.constrainers[0]";
connectAttr "M_R_Eye_ik_an.wm" "MeyesR_EyeDeformerJointsKLOp.constrainers[1]";
connectAttr "MeyesR_EyeDeformerJointsKLOp.constrainees[0]" "decomposeMatrix3.imat"
		;
connectAttr "MeyesR_EyeDeformerJointsKLOp.constrainees[1]" "decomposeMatrix4.imat"
		;
connectAttr "M_inputs_hrc.drawDebug" "MeyesR_YeakfdjsDeformerJointsKLOp.drawDebug"
		;
connectAttr "M_inputs_hrc.rigScale" "MeyesR_YeakfdjsDeformerJointsKLOp.rigScale"
		;
connectAttr "M_R_Yeakfdjs_fK_an.wm" "MeyesR_YeakfdjsDeformerJointsKLOp.constrainers[0]"
		;
connectAttr "M_R_Yeakfdjs_ik_an.wm" "MeyesR_YeakfdjsDeformerJointsKLOp.constrainers[1]"
		;
connectAttr "MeyesR_YeakfdjsDeformerJointsKLOp.constrainees[0]" "decomposeMatrix5.imat"
		;
connectAttr "MeyesR_YeakfdjsDeformerJointsKLOp.constrainees[1]" "decomposeMatrix6.imat"
		;
connectAttr "M_L_Eye_fK_def.wm" "canvasNode2.fk";
connectAttr "M_L_Eye_ik_an.wm" "canvasNode2.ik";
connectAttr "canvasNode2.result" "decomposeMatrix7.imat";
connectAttr "lambert2.oc" "lambert2SG.ss";
connectAttr "pCubeShape1.iog.og[1]" "lambert2SG.dsm" -na;
connectAttr "groupId3.msg" "lambert2SG.gn" -na;
connectAttr "lambert2SG.msg" "materialInfo1.sg";
connectAttr "lambert2.msg" "materialInfo1.m";
connectAttr "polyCube1.out" "groupParts1.ig";
connectAttr "groupId1.id" "groupParts1.gi";
connectAttr "groupParts1.og" "groupParts2.ig";
connectAttr "groupId3.id" "groupParts2.gi";
connectAttr "lambert3.oc" "lambert3SG.ss";
connectAttr "pCubeShape1.iog.og[2]" "lambert3SG.dsm" -na;
connectAttr "groupId4.msg" "lambert3SG.gn" -na;
connectAttr "lambert3SG.msg" "materialInfo2.sg";
connectAttr "lambert3.msg" "materialInfo2.m";
connectAttr "groupParts2.og" "groupParts3.ig";
connectAttr "groupId4.id" "groupParts3.gi";
connectAttr "lambert2.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo.tgi[0].ni[0].dn"
		;
connectAttr "lambert2SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo.tgi[0].ni[1].dn"
		;
connectAttr "lambert3.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo.tgi[0].ni[2].dn"
		;
connectAttr "lambert3SG.msg" "hyperShadePrimaryNodeEditorSavedTabsInfo.tgi[0].ni[3].dn"
		;
connectAttr "polyCube1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[0].dn";
connectAttr "pCubeShape1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[1].dn";
connectAttr "pCube1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[2].dn";
connectAttr "canvasNode2.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[3].dn";
connectAttr "decomposeMatrix7.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[4].dn"
		;
connectAttr "M_L_Eye_fK_def.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[5].dn";
connectAttr "M_L_Eye_ik_anShape.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[6].dn"
		;
connectAttr "M_L_Eye_ik_an.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[7].dn";
connectAttr "lambert2.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[8].dn";
connectAttr "lambert2SG.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[9].dn";
connectAttr "lambert3.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[10].dn";
connectAttr "lambert3SG.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[11].dn";
connectAttr "group1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[12].dn";
connectAttr "lambert2SG.pa" ":renderPartition.st" -na;
connectAttr "lambert3SG.pa" ":renderPartition.st" -na;
connectAttr "lambert2.msg" ":defaultShaderList1.s" -na;
connectAttr "lambert3.msg" ":defaultShaderList1.s" -na;
connectAttr "decomposeMatrix7.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "pCubeShape1.iog.og[0]" ":initialShadingGroup.dsm" -na;
connectAttr "pCubeShape1.ciog.cog[0]" ":initialShadingGroup.dsm" -na;
connectAttr "groupId1.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId2.msg" ":initialShadingGroup.gn" -na;
// End of EyeSolver.ma
