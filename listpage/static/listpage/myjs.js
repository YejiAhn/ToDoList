$('#ChkBox').change(function(){
    cb = $(this);
    cb.val(cb.prop('checked'));
});

function gogogo(){
	var tmp = $('[name=completed]').prop('checked'); // 변수에 넣기
	alert(tmp);
}