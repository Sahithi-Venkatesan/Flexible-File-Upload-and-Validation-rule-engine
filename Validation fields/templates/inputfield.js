$(document).ready(function()

    {
	var x = 0; 
	var max_fields = 10; 
	
       
	$('.list_add_button').click(function()
	    {
	   
	    if(x < max_fields){ 
	        x++; 
            var input_field = '<div class="row"><div class="col-xs-4 col-sm-4 col-md-4"><div class="form-group"><input name="list['+x+'][]" type="text" placeholder="Column name" class="form-control"/></div></div><div class="col-xs-4col-sm-4 col-md-4"><div class="form-group"><input name="list['+x+'][]" type="text" placeholder="Data type" class="form-control"/></div></div><div class="col-xs-4 col-sm-4 col-md-4"><div class="form-group"><input name="list['+x+'][]" type="text" placeholder="Length" class="form-control"/></div></div><div class="col-xs-1 col-sm-7 col-md-1"><a href="javascript:void(0);" class="list_remove_button btn btn-danger">Remove</a></div></div>';  
	        $('.list_wrapper').append(input_field); 
	    }
        });
    
        
        $('.list_wrapper').on('click', '.list_remove_button', function()
        {
           $(this).closest('div.row').remove(); 
           x--; 
        });
});