import logging

def logging_msg_request(status_code=200):

    logging.basicConfig(filename='./pvc.log'
                        , filemode='a'
                        , format='%(asctime)s  %(levelname)s  %(message)s'
                        , datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    if f.status == status_code:
        logger.info(msg='GET http://localhost:%d/proxies' % port + " the status code is %d" % f.status)
    else:

        logger.error(msg='GET http://localhost:%d/proxies' % port + " the status code is %d" % f.status)


def common_info(msg):
    logging.basicConfig(filename='./pvc.log'
                        , filemode='a'
                        , format='%(asctime)s  %(levelname)s  %(message)s'
                        , datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.info(msg)






