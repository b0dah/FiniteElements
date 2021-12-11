from task import Task

if __name__ == '__main__':
    task2 = Task()
    task2.configure_parameters(
        a=0,
        b=1,
        N=101,
        sigma1=0.1,
        sigma2=0.1,
        alpha=0.2,
        mu=0.15,
        lambda_=1.2,
        s=1,
        cond_left=0,
        cond_right_deriv=0.12
    )
    task2.execute()
    task2.show()
    task2.write_file('result.txt')
