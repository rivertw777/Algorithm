select distinct car_id,
    if (car_id in (
        select car_id
        from car_rental_company_rental_history
        where date(start_date) <= '2022-10-16' 
            and date(end_date) >= '2022-10-16'
    ), '대여중', '대여 가능') 'availability'
from car_rental_company_rental_history
order by car_id desc