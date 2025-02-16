from typing             import Callable
from jungo_sdk          import NodeError, RpcServer, add_args_worker_and_conf, mk_worker_from_args, serve_worker
from echo_subnet.api    import PingApi

import bittensor as bt
import traceback
import argparse


class RpcServerImpl(RpcServer, PingApi):
    def rpcs(self) -> list[Callable]:
        return [
            self.ping,
            self.echo,
        ]

    def ping(self) -> str:
        return "pong"

    def echo(self, msg: str) -> str:
        return msg

def main():
    parser = argparse.ArgumentParser()

    try:
        conf = add_args_worker_and_conf(parser)
        args = parser.parse_args()
        worker = mk_worker_from_args(args, conf)
        server = RpcServerImpl()
        serve_worker(worker.port, server)
    except NodeError as e:
        bt.logging.error("NodeError: " + str(e))
        traceback.print_exc()
    except Exception as e:
        bt.logging.error("Internal error: " + str(e))
        traceback.print_exc()

if __name__ == '__main__':
    main()
