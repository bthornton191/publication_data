robocopy using_machine_learning_to_identify_dem_soil_properties_from_bevameter_test_data\rpt rst\source\_static\using_machine_learning_to_identify_dem_soil_properties_from_bevameter_test_data\rpt /e /mir
cd rst
call make html
cd ..
robocopy rst\build\html docs /e /mir
