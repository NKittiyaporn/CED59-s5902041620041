<?php

namespace frontend\controllers;

use yii\web\Controller;

class TestController extends Controller 
{
    public function actionIndex() {
        echo 'index';
        return $this->render('index');
    }
    public function actionTest() {
        $data = 'data test';
        return $this->render('test', [
            'xdata' => $data         
        ]);
    }
}