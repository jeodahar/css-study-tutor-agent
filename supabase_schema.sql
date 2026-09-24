-- Run this once in the Supabase SQL editor (Project > SQL Editor > New query)

create table if not exists assessments (
    id uuid default gen_random_uuid() primary key,
    student_id text not null,
    subject text not null,
    question text,
    answer_text text,
    assessment jsonb,
    created_at timestamp with time zone default now()
);

create index if not exists idx_assessments_student on assessments (student_id);
