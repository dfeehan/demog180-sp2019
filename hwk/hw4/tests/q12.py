test = {
  'name': 'q12',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> round(np.mean(er_res.column(0)), 2)
          0.03
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(np.mean(er_res.column(1)), 2)
          2.88
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(np.corrcoef(er_res['cc'], er_res['apl'])[0,1],2)
          -0.1
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
