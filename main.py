def get_order_set_by_team_type_and_stage(self, course_or_group, request):
    # .filter(user__nickname__icontains='梁向上')
    # 默认团队
    team_id = self.get_team_id()
    # 登录用户所属团队
    team_list = []
    user_team_id = request.user.current_team.id
    team_list.append(user_team_id)
    substeam = request.user.current_team.child_teams.all()
    for team in substeam:
        teamid = team.id
        team_list.append(teamid)
    consume_set = Consume.objects.filter(team_id__in=team_list)
    stage_id_list = []
    for consume in consume_set:
        stage_id = consume.stage_id
        stage_id_list.append(stage_id)
    if course_or_group:
        if user_team_id == team_id:
            order_set = course_or_group.courseorder_set.filter(
                Q(channel__team_id__in=team_list) | Q(stage_id__in=stage_id_list) | Q(channel__isnull=True,
                                                                                      stage__isnull=True))
        else:
            order_set = course_or_group.courseorder_set.filter(
                Q(channel__team_id__in=team_list) | Q(stage_id__in=stage_id_list))
    else:
        if user_team_id == team_id:
            course_id_list = [course.id for course in Course.objects.filter(team_id=team_id, status=1)]
            course_group_id_list = [group.id for group in CourseGroup.objects.filter(team_id=team_id)]
            order_set = CourseOrder.objects.filter(
                Q(course_id__in=course_id_list) | Q(course_group_id__in=course_group_id_list))
        else:
            order_set = CourseOrder.objects.filter(Q(channel__team_id__in=team_list) | Q(stage_id__in=stage_id_list))

    int_stage_id = request.data.get('stage')
    str_stage_id = request.data.get('stage_id')
    if int_stage_id or str_stage_id:
        validated_stage_id_list = SaleTeamService().get_validate_stage_id_list(request)
        user_id_list = StudentCard.objects.filter(stage_id__in=validated_stage_id_list).values_list('student_id',
                                                                                                    flat=True)
        order_set = order_set.filter(user_id__in=user_id_list)
    return order_set
