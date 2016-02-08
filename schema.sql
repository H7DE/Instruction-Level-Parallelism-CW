CREATE TABLE simulation (
	config text not null,
	ss_problem_size integer not null,
	total_power float not null,
	fetch_ifqsize float not null,
	ruu_size float not null,
	lsq_size float not null,
	res_ialu float not null,
	res_imult float not null,
	res_fpalu float not null,
	res_fp_mult float not null
)
