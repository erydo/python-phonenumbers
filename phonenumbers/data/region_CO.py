"""Auto-generated file, do not edit by hand. CO metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_CO = PhoneMetadata(id='CO', country_code=57, international_prefix='00[579]|#555|#999',
    general_desc=PhoneNumberDesc(national_number_pattern='(?:[13]\\d{0,3}|[24-8])\\d{7}', possible_number_pattern='\\d{7,11}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='[124-8][2-9]\\d{6}', possible_number_pattern='\\d{8}', example_number='12345678'),
    mobile=PhoneNumberDesc(national_number_pattern='3(?:0[0-24]|1[0-8]|2[01])\\d{7}', possible_number_pattern='\\d{10}', example_number='3211234567'),
    toll_free=PhoneNumberDesc(national_number_pattern='1800\\d{7}', possible_number_pattern='\\d{11}', example_number='18001234567'),
    premium_rate=PhoneNumberDesc(national_number_pattern='19(?:0[01]|4[78])\\d{7}', possible_number_pattern='\\d{11}', example_number='19001234567'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0([3579]|4(?:44|56))?',
    number_format=[NumberFormat(pattern='(\\d)(\\d{7})', format=u'\\1 \\2', leading_digits_pattern=['1(?:8[2-9]|9[0-3]|[2-7])|[24-8]', '1(?:8[2-9]|9(?:09|[1-3])|[2-7])|[24-8]'], national_prefix_formatting_rule=u'(\\1)', domestic_carrier_code_formatting_rule=u'0$CC \\1'),
        NumberFormat(pattern='(\\d{3})(\\d{7})', format=u'\\1 \\2', leading_digits_pattern=['3'], domestic_carrier_code_formatting_rule=u'0$CC \\1'),
        NumberFormat(pattern='(1)(\\d{3})(\\d{7})', format=u'\\1-\\2-\\3', leading_digits_pattern=['1(?:80|9[04])', '1(?:800|9(?:0[01]|4[78]))'], national_prefix_formatting_rule=u'0\\1')],
    intl_number_format=[NumberFormat(pattern='(\\d)(\\d{7})', format=u'\\1 \\2', leading_digits_pattern=['1(?:8[2-9]|9[0-3]|[2-7])|[24-8]', '1(?:8[2-9]|9(?:09|[1-3])|[2-7])|[24-8]']),
        NumberFormat(pattern='(\\d{3})(\\d{7})', format=u'\\1 \\2', leading_digits_pattern=['3']),
        NumberFormat(pattern='(1)(\\d{3})(\\d{7})', format=u'\\1 \\2 \\3', leading_digits_pattern=['1(?:80|9[04])', '1(?:800|9(?:0[01]|4[78]))'])])
