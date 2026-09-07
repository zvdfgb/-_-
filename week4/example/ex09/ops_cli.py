import argparse

def main():
    p = argparse.ArgumentParser(prog="devops", description="开发运维综合管理工具")
    sub = p.add_subparsers(dest="cmd", required=True)
    
    deploy_p = sub.add_parser("deploy", help="部署服务")
    deploy_p.add_argument("--env", choices=["staging", "prod"], required=True)
    
    backup_p = sub.add_parser("backup", help="备份数据库")
    backup_p.add_argument("--compress", action="store_true")
    
    args = p.parse_args()
    print(f"执行子命令 [{args.cmd}]，参数: {vars(args)}")

if __name__ == "__main__":
    main()
