%%%%%%%%%%%%%%% FACTS %%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%course100a(X): X is a 100 Level Alpha Semester Course
course100a("acc111").
course100a("csc111").
course100a("ecn111").
course100a("mat111").
course100a("mat112").
course100a("phy111").
course100a("cst111").
course100a("gst111").
course100a("cit111").
course100a("eds111").
course100a("tmc111").
course100a("tmc112").

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%course200a(X): X is a 200 Level Alpha Semester Course
course200a("bfn211").
course200a("bus211").
course200a("cit211").
course200a("csc211").
course200a("csc213").
course200a("csc214").
course200a("cbs111").
course200a("mat214").
course200a("gst211").
course200a("dld111").
course200a("eds211").
course200a("tmc211").
course200a("tmc212").
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%credit(X, 1): course X has a credit of 1
%100 Level Alpha Semester Courses
credit("acc111", 2).
credit("csc111", 3).
credit("ecn111", 3).
credit("mat111", 3).
credit("mat112", 2).
credit("phy111", 2).
credit("cst111", 2).
credit("gst111", 2).
credit("cit111", 0).
credit("eds111", 1).
credit("tmc111", 1).
credit("tmc112", 0).
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%200 Level Alpha Semester Courses
credit("bfn211", 2).
credit("bus211", 2).
credit("cit211", 0).
credit("csc211", 3).
credit("csc213", 3).
credit("csc214", 3).
credit("cbs111", 3).
credit("mat214", 2).
credit("gst211", 2).
credit("dld111", 0).
credit("eds211", 1).
credit("tmc211", 1).
credit("tmc212", 0).
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%compulsory(X): course X is compulsory
compulsory("acc111").
compulsory("csc111").
compulsory("ecn111").
compulsory("mat111").
compulsory("mat112").
compulsory("phy111").
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
compulsory("bfn211").
compulsory("bus211").
compulsory("cit211").
compulsory("csc211").
compulsory("csc213").
compulsory("csc214").
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%elective("cbs111").
%elective("mat214").
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
nuc_course("cst111").
nuc_course("gst111").
nuc_course("gst211").
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
uni_course("cit111").
uni_course("eds111").
uni_course("tmc111").
uni_course("tmc112").
uni_course("dld111").
uni_course("cit111").
uni_course("eds211").
uni_course("tmc211").
uni_course("tmc212").
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% RULES

elective(X):-
(\+ compulsory(X), \+ uni_course(X), \+ nuc_course(X)).


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% recommendCourse if the course is of 100 level and failed or 


recommendCourse(X):-
(failed(X), course100a(X)) ; (course200a(X), (compulsory(X); nuc_course(X); uni_course(X))).

