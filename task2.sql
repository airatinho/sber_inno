--task 2.1
select
       app.id_app as id_app,
       app.id_client as id_client,
       app.product as product,
       qq.id_question as id_question,
       quest.question as question,
       qq.answer as answer


from app
left join qq
    on app.id_client=qq.id_client
left join "Question" quest on quest.id_question=qq.id_question


--task 2.2
with otch as (
    select answer as otches
    from qq
             left join "Question" Q on qq.id_question = Q.id_question
    where question = 'Отчество'
),
 fam as (
    select answer as familia
    from qq
             left join "Question" Q on qq.id_question = Q.id_question
    where question = 'Фамилия'
),
 names as (
    select answer as name
    from qq
             left join "Question" Q on qq.id_question = Q.id_question
    where question = 'Имя'
)
select id_app,
       id_client,
       product,
       fam.familia as Фамилия,
       names.name as Имя,
       otch.otches as Отчество
from app
cross join fam
cross join names
cross join otch
