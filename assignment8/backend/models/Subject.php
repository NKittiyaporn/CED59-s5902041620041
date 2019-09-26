<?php
namespace backend\models;


use yii\behaviors\TimestampBehavior;
use yii\behaviors\BlameableBehavior;
class Subject extends \common\models\Subject 
{
    public function behaviors()
    {
        return [
            TimestampBehavior::class,
            BlameableBehavior::class
        ];
    }
}
?>