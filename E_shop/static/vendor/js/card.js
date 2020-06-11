/////////////////// product +/-
$(document).ready(function() {
    $('.num-in span').click(function() {
        var $input = $(this).parents('.num-block').find('input.in-num');
        if ($(this).hasClass('minus')) {
            var count = parseFloat($input.val()) - 1;
            count = count < 1 ? 1 : count;
            if (count < 2) {
                $(this).addClass('dis');
            } else {
                $(this).removeClass('dis');
            }
            $input.val(count);
        } else {
            var count = parseFloat($input.val()) + 1
            $input.val(count);
            if (count > 1) {
                $(this).parents('.num-block').find(('.minus')).removeClass('dis');
            }
        }

        $input.change();
        return false;
    });

});
// product +/-