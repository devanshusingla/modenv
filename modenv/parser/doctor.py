from modenv.commands.doctor import check, fix


def register_doctor(subparsers):
    doctor_parser = subparsers.add_parser("doctor", help="Check and fix environment issues")
    doctor_sub = doctor_parser.add_subparsers(dest="doctor_command", required=True)

    check_parser = doctor_sub.add_parser("check", help="Run checks")
    check.register(check_parser)

    fix_parser = doctor_sub.add_parser("fix", help="Auto-fix issues")
    fix.register(fix_parser)

